import logging
import json
import datetime
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from agents.news_agent import NewsAgent
from tools.weather import get_weather
from tools.aqi import get_aqi
from tools.crypto import get_crypto
from dotenv import load_dotenv
load_dotenv()

# --------------------- CONFIG ---------------------


BOT_TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = int(os.getenv("CHAT_ID"))
print("DEBUG TOKEN:", BOT_TOKEN)
print("DEBUG CHAT:", CHAT_ID)

logging.basicConfig(level=logging.INFO)


# --------------------- TOPIC FEEDS ---------------------

TOPIC_FEEDS = {
    "india": [
        "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    ],
    "technology": [
        "https://techcrunch.com/feed/",
        "https://www.theverge.com/tech/rss/index.xml"
    ],
    "economy": [
        "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"
    ],
    "sports": [
        "https://www.espn.com/espn/rss/news"
    ],
    "world": [
        "http://feeds.bbci.co.uk/news/world/rss.xml"
    ],
    "business": [
        "https://www.thehindu.com/business/feeder/default.rss"
    ],
    "science": [
        "https://www.nasa.gov/rss/dyn/breaking_news.rss"
    ],
    "liverpool": [
        "https://www.thisisanfield.com/feed/",
        "https://www.liverpoolfc.com/news/feed"
    ]
}


# --------------------- INITIALIZE NEWS AGENT ---------------------

agent = NewsAgent()


# --------------------- SAFE TEXT SANITIZER ---------------------

def safe_text(s: str) -> str:
    """Clean text to avoid Telegram parse exceptions."""
    return (
        s.replace("&", "and")
         .replace("<", "")
         .replace(">", "")
         .replace("_", " ")
         .replace("*", "")
         .replace("[", "")
         .replace("]", "")
         .replace("\n", " ")
         .strip()
    )


# --------------------- SAFE REPLY ---------------------

async def reply(target, text):
    """Send text safely, splitting if needed."""
    from telegram import Update

    try:
        if isinstance(target, Update):
            await target.message.reply_text(text)
        else:
            await target.bot.send_message(CHAT_ID, text)
    except Exception as e:
        print("TELEGRAM ERROR:", e)
        # Split message if too large or invalid
        chunks = [text[i:i+3500] for i in range(0, len(text), 3500)]
        for c in chunks:
            try:
                if isinstance(target, Update):
                    await target.message.reply_text(c)
                else:
                    await target.bot.send_message(CHAT_ID, c)
            except Exception as e2:
                print("SECOND TELEGRAM ERROR:", e2)


# --------------------- SEND NEWS ---------------------

async def send_news(update_or_context, topic):
    feeds = TOPIC_FEEDS[topic]

    print("DEBUG: Calling NewsAgent for topic:", topic)
    print("DEBUG: Using feeds:", feeds)

    articles = agent.run([topic], feeds)

    print("DEBUG: articles returned:", len(articles))

    if not articles:
        await reply(update_or_context, f"No news found for {topic.title()}")
        return

    msg = f"{topic.title()} News:\n\n"

    # Limit to top 5 to avoid long messages
    for item in articles[:5]:
        title = safe_text(item["title"])
        link = item["link"]
        msg += f"• {title}\n{link}\n\n"

    await reply(update_or_context, msg)


# --------------------- USER COMMANDS ---------------------

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hey Ash! I'm your RootX News Bot.\n\n"
        "Categories:\n"
        "/india /technology /economy /sports /world\n"
        "/business /science /liverpool\n\n"
        "Daily digest sent at 9 AM ☕"
    )

async def india(update, ctx):     await send_news(update, "india")
async def technology(update, ctx): await send_news(update, "technology")
async def economy(update, ctx):   await send_news(update, "economy")
async def sports(update, ctx):    await send_news(update, "sports")
async def world(update, ctx):     await send_news(update, "world")
async def business(update, ctx):  await send_news(update, "business")
async def science(update, ctx):   await send_news(update, "science")
async def liverpool(update, ctx): await send_news(update, "liverpool")


# --------------------- DAILY DIGEST ---------------------

async def daily_digest(context: ContextTypes.DEFAULT_TYPE):
    weather = get_weather("Bangalore")
    aqi = get_aqi("Bangalore")
    crypto = get_crypto()

    msg = f"""🌅 Good Morning Ash!

🌤 Weather: {weather}
🌫 AQI: {aqi}
₿ Crypto: {crypto}

Top Headlines:
"""

    top_articles = agent.run(["india"], TOPIC_FEEDS["india"])

    for item in top_articles[:5]:
        title = safe_text(item["title"])
        msg += f"• {title}\n{item['link']}\n\n"

    await context.bot.send_message(CHAT_ID, msg)


# --------------------- BOT SETUP ---------------------

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("india", india))
    app.add_handler(CommandHandler("technology", technology))
    app.add_handler(CommandHandler("economy", economy))
    app.add_handler(CommandHandler("sports", sports))
    app.add_handler(CommandHandler("world", world))
    app.add_handler(CommandHandler("business", business))
    app.add_handler(CommandHandler("science", science))
    app.add_handler(CommandHandler("liverpool", liverpool))

    # Daily 9AM job
    job_queue = app.job_queue
    job_queue.run_daily(
        daily_digest,
        time=datetime.time(
            hour=9,
            minute=0,
            tzinfo=datetime.timezone(datetime.timedelta(hours=5, minutes=30))
        )
    )

    print("🤖 RootX News Bot running...")
    app.run_polling()


if __name__ == "__main__":
    run_bot()
