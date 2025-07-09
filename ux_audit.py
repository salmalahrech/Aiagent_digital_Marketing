import requests
from bs4 import BeautifulSoup
from config import HEADERS

def audit_ux(companies):
    results = []
    for company in companies:
        try:
            response = requests.get(company["url"], headers=HEADERS, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            layout = len(soup.find_all(["section", "div"]))
            ctas = len(soup.find_all(string=lambda s: "sign up" in s.lower() or "get started" in s.lower()))
            has_video = bool(soup.find("video"))
            services = len(soup.find_all("li"))

            results.append({
                "name": company["name"],
                "layout_blocks": layout,
                "cta_count": ctas,
                "has_video": has_video,
                "listed_services": services
            })
        except Exception as e:
            results.append({"name": company["name"], "error": str(e)})
    return results
