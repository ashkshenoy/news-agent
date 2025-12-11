# agents/news_agent.py

from tools.fetch_rss import fetch_news
from tools.clean_text import clean

class NewsAgent:
    name = "NewsAgent"
    goal = "Fetch and return raw news articles."

    def run(self, topics, feed_urls):
        """
        topics     : ["india"], ["technology"], etc (not used here)
        feed_urls  : list of RSS feed URLs provided by bot.py
        """
        print("DEBUG: NewsAgent.run called with feeds:", feed_urls)
        articles = fetch_news(feed_urls)
        print("DEBUG: NewsAgent.run got count:", len(articles))
        cleaned = []
        for a in articles:
            cleaned.append({
                "title": clean(a.get("title", "")),
                "summary": clean(a.get("summary", "")),
                "link": a.get("link", "")
            })

        return cleaned
