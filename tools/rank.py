def rank_articles(articles, topics):
    scored = []
    for art in articles:
        score = sum(t.lower() in art["title"].lower() for t in topics)
        if score > 0:
            scored.append((score, art))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [a for score, a in scored]
