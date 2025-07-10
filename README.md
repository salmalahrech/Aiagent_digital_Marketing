# AI Digital Agent

# 🤖 AI Digital Marketing Agent

An automated Python agent that performs digital competitor research and content planning based on your target industry or keyword. This project simulates how digital marketers gather insights from competitor websites and social media  and turns that into a ready-to-use content strategy report.

---

## 🚀 Features

- 🔍 Finds top competitors for a given keyword
- 🛠 Analyzes tech stacks using Wappalyzer (or simulated)
- 📈 Simulates traffic metrics (monthly visits, bounce rate)
- 🎯 Audits UX (CTAs, video usage, layout depth)
- 📱 Simulates social media presence
- 💡 Generates content ideas based on top formats
- 📝 Outputs a full report as `report.txt`

---

## 📁 Project Structure

```

ai-digital-agent/
│
├── agent.py                    # Main runner script
├── competitor\_finder.py        # Scrapes top competitors from Google
├── tech\_analyzer.py            # (Optional) Uses Wappalyzer API
├── traffic\_analyzer.py         # Simulated traffic stats
├── ux\_audit.py                 # Scrapes homepage for UX insights
├── social\_scraper.py           # Simulated social metrics
├── content\_idea\_generator.py   # Generates content ideas
├── report\_generator.py         # Builds the final report
├── config.py                   # Central settings/API keys
├── requirements.txt
└── README.md

````

---

## 🧪 How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/salmalahrech/Aiagent_digital_Marketing.git
   cd Aiagent_digital_Marketing
````

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   # or
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the agent**:

   ```bash
   python agent.py
   ```

5. **View your report** in `report.txt`.

---

## 🔑 API Keys (Optional)

* You can use the free tier of [Wappalyzer](https://www.wappalyzer.com/) to get tech stack data.
* Add your API keys in `config.py` like this:

```python
WAPPALYZER_API_KEY = "your-key-here"
```

Or leave blank to use simulated data.

---

## 📌 Example Use Case

You want to understand what competitors in **"marketing automation tools"** are doing:

```python
run_agent("marketing automation tools")
```

You'll get:

* Competitor names and URLs
* Tech stacks
* UX insights (CTAs, layout)
* Simulated traffic
* Social presence
* Content ideas

---

## 🤖 Built With

* Python 3.10+
* Requests + BeautifulSoup (web scraping)
* Pandas (report formatting)
* Simulated APIs (or optional real integrations)

---

## 📄 License

MIT License — free to use, modify, and share.

---

## 🙋‍♀️ Author

Made with ❤️ by [@salmalahrech](https://github.com/salmalahrech)

```

Would you like me to add a **badge** or link to deploy it with Streamlit or Hugging Face Spaces?
```
