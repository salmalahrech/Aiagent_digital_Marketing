from competitor_finder import find_competitors
from tech_analyzer import analyze_tech_stack
from traffic_analyzer import get_traffic_data
from ux_audit import audit_ux
from social_scraper import analyze_social
from content_idea_generator import generate_ideas
from report_generator import generate_report

def run_agent(keyword):
    competitors = find_competitors(keyword)
    tech = analyze_tech_stack(competitors)
    traffic = get_traffic_data(competitors)
    ux = audit_ux(competitors)
    social = analyze_social(competitors)
    ideas = generate_ideas(social)

    generate_report(competitors, tech, traffic, ux, social, ideas)

if __name__ == "__main__":
    run_agent("marketing automation tools")
