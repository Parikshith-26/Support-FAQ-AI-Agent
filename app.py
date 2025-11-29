import json
import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Debug line to verify key loading (You can remove later)
st.write("DEBUG KEY LOADED:", GROQ_API_KEY)

# ---------------------------------------------
# Groq API Call (Direct HTTPS - Works 100%)
# ---------------------------------------------
def groq_generate(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a helpful customer support AI agent."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    # Handle API errors safely
    if response.status_code != 200:
        return "Error contacting AI service. Please try again."

    json_res = response.json()

    return json_res["choices"][0]["message"]["content"]


# ---------------------------------------------
# Streamlit UI
# ---------------------------------------------
st.title("Support FAQ AI Agent")

# Load FAQs
with open("faqs.json", "r") as f:
    faqs = json.load(f)

user_question = st.text_input("Ask your question:")

if user_question:
    # Check FAQ match
    found = None
    for q, a in faqs.items():
        if user_question.lower() in q.lower():
            found = a
            break

    if found:
        st.success(found)
    else:
        prompt = f"""
        You are a customer support AI agent.
        If the answer is known, respond clearly.
        If unknown, reply ONLY with: "Escalating to human support."

        User question: {user_question}
        """

        answer = groq_generate(prompt)
        st.info(answer)

