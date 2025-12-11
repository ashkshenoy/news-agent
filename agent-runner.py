import json
from agents.news_agent import NewsAgent

def load_topics():
    with open("memory/topics.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    topics = load_topics()

    feeds = [
        "https://news.google.com/rss",
        "https://www.thehindu.com/news/national/feeder/default.rss",
        "https://www.theguardian.com/world/rss",
        "https://www.espnfc.com/rss",
        "https://techcrunch.com/feed/"
    ]

    agent = NewsAgent()
    digest = agent.run(topics, feeds)

    print("\n------ ROOTX NEWS LINKS ------\n")
    for item in digest:
        print(f"• {item['title']}")
        print(f"  {item['preview'][:150]}...")
        print(f"  Read: {item['link']}\n")
