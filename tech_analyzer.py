import requests
from config import WAPPALYZER_API_KEY

def analyze_tech_stack(companies):
    url = "https://api.wappalyzer.com/v2/lookup/"
    headers = {
        "x-api-key": WAPPALYZER_API_KEY,
        "Content-Type": "application/json"
    }

    tech_data = []
    for company in companies:
        try:
            res = requests.post(url, headers=headers, json={"urls": [company["url"]]})
            tech = res.json()[0] if res.ok else {}
            tech_data.append({
                "name": company["name"],
                "url": company["url"],
                "technologies": tech.get("technologies", [])
            })
        except Exception as e:
            tech_data.append({"name": company["name"], "url": company["url"], "technologies": [], "error": str(e)})
    return tech_data
