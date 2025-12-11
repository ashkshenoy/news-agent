# debug_send.py
from agents.news_agent import NewsAgent
from pprint import pprint
from tools.fetch_rss import fetch_news

TOPIC_FEEDS = {
    "india": ["https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"],
    "technology": ["https://techcrunch.com/feed/"]
}

agent = NewsAgent()

topic = "india"
feeds = TOPIC_FEEDS[topic]
print("send_news simulation for topic:", topic)
print("Feeds being used:", feeds)

articles = agent.run([topic], feeds)
print("Articles returned by agent.run():", len(articles))

# If you previously had additional filtering, show what passes matches_topic
from bot import TOPIC_KEYWORDS  # only if present, else skip
kw = TOPIC_KEYWORDS.get(topic, [])
print("Topic keywords:", kw)
filtered = []
for a in articles:
    title = a.get("title","").lower()
    summary = a.get("summary","").lower()
    # same matching logic as your bot
    hit = any(k in title or k in summary for k in kw) if kw else True
    if hit:
        filtered.append(a)
print("Filtered count (matching keywords):", len(filtered))
if filtered:
    print("\nFirst filtered item:")
    pprint(filtered[0])
