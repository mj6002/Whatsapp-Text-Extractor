# 💬 WhatsApp Web Message Extractor (Python + Chrome)

A Python-based automation tool that **extracts chat messages directly from WhatsApp Web in Google Chrome**. It scrapes real-time conversations by controlling the browser using Selenium and organizes the data into a clean format for analysis or export.

---

## 🔍 Features

- 💻 Automates Chrome to extract messages from WhatsApp Web
- 🕓 Captures timestamp, sender, and message content
- 📊 Supports structured data export via CSV/Excel (with Pandas + OpenPyXL)
- 🔧 Easily extendable for chat analytics, NLP, or GUI
- ⚡ Works in real time or batch mode

---

## 📸 Sample Output

```json
[
  {
    "timestamp": "2025-06-24 10:45:00",
    "sender": "John Doe",
    "message": "Hey, what's up?"
  },
  ...
]
```
⚙️ Requirements
  - Python 3.7+
  - Google Chrome browser
  - ChromeDriver matching your browser version
  - Selenium (or pyppeteer / other lib, depending on your implementation)

Install dependencies:
  - pip install -r requirements.txt

🧠 How It Works
  - Uses Selenium to control Chrome and access WhatsApp Web.
  - Locates message DOM elements using XPath or CSS selectors.
  - Parses message blocks to extract:
      ⏰ Timestamp
      🧑 Sender name
      💬 Message content

🧪 Possible Extensions
  - Extract from multiple chats (auto-switch)
  - Save chat histories by contact name
  - Real-time monitoring for new incoming messages
  - Build a GUI using Tkinter or Streamlit
  - Add keyword alerts or NLP features

⚠️ Disclaimer
This tool is intended for educational and personal use only. Respect user privacy and WhatsApp’s Terms of Service.

📬 Contact
Questions or suggestions?
Reach out via GitHub Issues or [mjain942006@gmail.com].
