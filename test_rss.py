from agents.news_agent import NewsAgent

agent = NewsAgent()
feeds = [
    "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
]

res = agent.run(["india"], feeds)

print(len(res))
print(res[:3])
