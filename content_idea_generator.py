def generate_ideas(social_data):
    ideas = []
    for item in social_data:
        company = item["name"]
        ideas.append({
            "name": company,
            "ideas": [
                f"{company}: Behind-the-scenes Instagram Reel",
                f"{company}: Customer success story video",
                f"{company}: Tips carousel for niche audience",
                f"{company}: Team member spotlight post"
            ]
        })
    return ideas
