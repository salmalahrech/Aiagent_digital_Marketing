import requests
from bs4 import BeautifulSoup
from config import HEADERS

def find_competitors(keyword):
    print(f"🔍 Finding top competitors for: {keyword}")
    search_url = f"https://www.google.com/search?q=top+{keyword.replace(' ', '+')}"
    response = requests.get(search_url, headers=HEADERS)

    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    
    for g in soup.select("div.tF2Cxc")[:5]:
        title = g.select_one("h3")
        link = g.select_one("a")
        if title and link:
            results.append({"name": title.text, "url": link["href"]})

    return results
