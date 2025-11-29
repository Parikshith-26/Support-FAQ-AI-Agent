📘 Support FAQ AI Agent — README

🧠 Overview

The Support FAQ AI Agent is a lightweight customer-support assistant that instantly answers frequently asked questions.

It uses:

FAQ matching (from faqs.json)

Groq LLM (llama-3.1-8b-instant) for smart AI responses

A clean Streamlit UI

Completely free & easy to deploy

This was built for the AI Agent Development Challenge.

⭐ Features
🔹 FAQ Matching

Returns a predefined answer if the user’s question matches any FAQ.

🔹 AI-Generated Answer

If no FAQ matches, the Groq AI model responds with a helpful answer.

🔹 Smart Escalation

If the model cannot answer, it replies:
"Escalating to human support."

🔹 Simple UI

Streamlit interface for quick use and easy interaction.

🔹 Free to Run

Uses Groq API → no paid tokens needed.

🛠️ Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
AI Model	Groq llama-3.1-8b-instant
Storage	faqs.json
Environment	.env
📂 Project Structure
support-faq-agent/
│── app.py
│── faqs.json
│── requirements.txt
│── README.md
│── .env

📥 Installation & Setup (VS Code)
✔ Step 1: Open Folder

Open VS Code → File → Open Folder → Select support-faq-agent

✔ Step 2: Create Virtual Environment (optional)

Open VS Code terminal:

python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

✔ Step 3: Install Dependencies
pip install -r requirements.txt

✔ Step 4: Add Groq API Key

Create a .env file in the same folder:

GROQ_API_KEY=your_api_key_here


Get a free key here:
https://console.groq.com/keys

▶️ Run the Application

In VS Code terminal:

streamlit run app.py


Browser will open:

http://localhost:8501

🤖 How It Works

User types a question

Script checks in faqs.json

If matched → return answer

If not → ask Groq AI

If AI cannot answer → escalate

📘 Example faqs.json
{
  "What are your working hours?": "We operate from 9 AM to 6 PM, Monday to Saturday.",
  "How can I reset my password?": "Click on 'Forgot Password' and follow the instructions.",
  "Do you offer refunds?": "Yes, refunds are available within 7 days of purchase."
}

🚀 Deploy on Streamlit Cloud

Push code to GitHub

Visit https://share.streamlit.io

Click Deploy app

Select repo

Add API key in:
Settings → Secrets

🔮 Future Improvements

Add vector search for better accuracy

Multi-language support

Admin panel to edit FAQs

Analytics for queries

Integrate with CRMs like Zoho/Freshdesk

👨‍💻 Author

Developed as part of the AI Agent Development Challenge.