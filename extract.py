from bs4 import BeautifulSoup

def extract_articles(html):
    soup = BeautifulSoup(html, "lxml")

    articles = []

    for tag in soup.find_all(["article"]):
        text = tag.get_text(" ", strip=True)

        if len(text) > 50:
            articles.append(text)

    return articles
