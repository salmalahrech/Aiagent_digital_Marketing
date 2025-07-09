import random

def get_traffic_data(companies):
    traffic_data = []
    for company in companies:
        traffic_data.append({
            "name": company["name"],
            "url": company["url"],
            "monthly_visits": random.randint(10000, 500000),
            "bounce_rate": round(random.uniform(30, 70), 2),
            "avg_duration": f"{random.randint(1, 5)}:{random.randint(0, 59):02d}"
        })
    return traffic_data
