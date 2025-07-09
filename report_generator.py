def generate_report(companies, tech, traffic, ux, social, ideas):
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("📊 AI DIGITAL MARKETING REPORT\n\n")

        for i, company in enumerate(companies):
            f.write(f"--- {company['name']} ({company['url']}) ---\n")
            f.write("Tech Stack:\n")
            for t in tech[i]["technologies"]:
                f.write(f" - {t.get('name', 'Unknown')}\n")

            f.write(f"Traffic:\n - Monthly Visits: {traffic[i]['monthly_visits']}\n")
            f.write(f" - Bounce Rate: {traffic[i]['bounce_rate']}%\n")
            f.write(f" - Avg Duration: {traffic[i]['avg_duration']}\n")

            f.write("UX:\n")
            f.write(f" - Layout Blocks: {ux[i]['layout_blocks']}\n")
            f.write(f" - CTAs: {ux[i]['cta_count']}\n")
            f.write(f" - Has Video: {ux[i]['has_video']}\n")

            f.write("Social Media:\n")
            for p, followers in social[i]["followers"].items():
                f.write(f" - {p}: {followers} followers\n")
            f.write("Content Ideas:\n")
            for idea in ideas[i]["ideas"]:
                f.write(f" - {idea}\n")
            f.write("\n")
    print("✅ Report saved to report.txt")
