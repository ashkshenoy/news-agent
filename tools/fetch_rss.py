import feedparser
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_news(feed_urls):
    articles = []

    for url in feed_urls:
        print("DEBUG: fetch_rss requesting:", url)  # <---- DEBUG

        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            print("DEBUG: HTTP status =", r.status_code)  # <---- DEBUG
            print("DEBUG: Response length =", len(r.text))  # <---- DEBUG

            feed = feedparser.parse(r.text)
            print("DEBUG: feedparser entries =", len(feed.entries))  # <---- DEBUG

            for entry in feed.entries:
                articles.append({
                    "title": entry.get("title", ""),
                    "summary": entry.get("summary", ""),
                    "link": entry.get("link", "")
                })

        except Exception as e:
            print("DEBUG ERROR in fetch_rss:", e)

    print("DEBUG: fetch_news returning count:", len(articles))  # <---- DEBUG
    return articles
