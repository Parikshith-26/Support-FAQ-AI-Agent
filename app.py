import json
import streamlit as st
import httpx
from groq import Groq
from dotenv import load_dotenv
import os
import streamlit as st
st.write("DEBUG KEY LOADED:", os.getenv("GROQ_API_KEY"))


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("Support FAQ AI Agent")

# Load FAQs
with open("faqs.json", "r") as f:
    faqs = json.load(f)

user_question = st.text_input("Ask your question:")

if user_question:
    # Check FAQ
    found = None
    for q, a in faqs.items():
        if user_question.lower() in q.lower():
            found = a
            break

    if found:
        st.success(found)
    else:
        prompt = (
            "You are a customer support AI agent. "
            "If you know the answer, respond clearly. "
            "If not, reply ONLY: 'Escalating to human support.'\n\n"
            f"User question: {user_question}"
        )

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            # ✅ Correct way to extract text (works with new Groq API)
            answer = response.choices[0].message.content

            st.info(answer)

        except Exception as e:
            st.error(f"AI Error: {e}")











