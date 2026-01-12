##📰 RootX News Agent (Telegram Bot)

A simple, fast, modular Telegram bot that delivers:
Categorized news (India, Tech, Economy, Sports, etc.)
Weather
AQI (Air Quality Index)
Crypto prices in INR
Optional 9AM daily digest

Built using Python, RSS feeds, and python-telegram-bot.

🚀 Features
/india — India news
/technology — Tech news
/economy — Business/market news
/sports — Sports updates
/world — International headlines
/business — Business section
/science — Science updates
/liverpool — Liverpool FC news

Additional features:
🌤 Weather
🌫 AQI
₿ Crypto (BTC + ETH in INR)
⏰ Automatic 9AM Daily Digest (optional)
✨ Fully sanitized messages (Telegram-safe)

🛠️ Tech Stack
Python 3
python-telegram-bot
RSS feeds (Google News, BBC, ESPN, TechCrunch, The Verge, etc.)

📦 Setup

1. Clone the repository

    git clone https://github.com/<your-username>/rootx-news-bot.git
    cd rootx-news-bot

2. Install dependencies

  pip install -r requirements.txt
  pip install "python-telegram-bot[job-queue]"

4. Create a .env file

  BOT_TOKEN=your_telegram_bot_token
  CHAT_ID=your_chat_id

5. ▶️ Run the Bot
 
   python bot.py

6. Open Telegram → search for your bot → try commands like:

  /start
  /india
  /technology
  /liverpool

  Your bot will respond instantly.

📁 Project Structure
      rootx-news-bot/
        bot.py
        agents/
          news_agent.py
        tools/
          fetch_rss.py
          weather.py
          aqi.py
          crypto.py
          clean_text.py
        memory/
          topics.json
        requirements.txt
        .env.example
        README.md


🎯 Demo Instructions (For Viewers)

>Clone the project
>Add your own Telegram bot token
>Run the bot locally
>Send commands in Telegram
>No paid services or deployments required.

Requests + Feedparser

Dotenv for secrets


<img width="1392" height="799" alt="image" src="https://github.com/user-attachments/assets/739c7fab-1f7d-4af9-aec3-5bf0b4611e0f" />

