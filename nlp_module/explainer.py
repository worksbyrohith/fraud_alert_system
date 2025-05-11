import google.generativeai as genai
import os

# Set Gemini API key
# GEMINI_API_KEY = os.getenv("AIzaSyAsl8NtDt9CtcRaESWY2t5fZ_cIbnWBffQ", "AIzaSyAsl8NtDt9CtcRaESWY2t5fZ_cIbnWBffQ")
genai.configure(api_key='AIzaSyAsl8NtDt9CtcRaESWY2t5fZ_cIbnWBffQ')

# Load Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_explanation(transaction):
    prompt = f"""
    A customer made a transaction with the following details:
    Amount: ${transaction['amount']}
    Location: {transaction['location']}
    Time: {transaction['timestamp']}

    Explain in simple terms why this transaction might be suspicious.
    """
    response = model.generate_content(prompt)
    return response.text