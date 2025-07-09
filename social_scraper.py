import random

def analyze_social(companies):
    platforms = ["LinkedIn", "Instagram", "Twitter"]
    social_data = []

    for company in companies:
        stats = {
            "name": company["name"],
            "followers": {p: random.randint(1000, 50000) for p in platforms},
            "top_content_types": ["carousel", "video", "case study"]
        }
        social_data.append(stats)

    return social_data
