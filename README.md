<h1 align="center">🚨 Explainable Fraud Alert System</h1>

<p align="center">
  💡 Transparent AI-based fraud detection using behavioral modeling + Gemini-powered natural language explanations.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.12-blue?logo=python">
  <img src="https://img.shields.io/badge/ML-IsolationForest-success?logo=scikit-learn">
  <img src="https://img.shields.io/badge/NLP-GeminiPro-lightblue?logo=google">
  <img src="https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit">
</p>

---

## 🧾 Project Overview

Traditional fraud detection systems often flag transactions without context, leaving users confused. This project solves that by combining:

- 🔍 **Behavioral-based Anomaly Detection** (Isolation Forest)
- 💬 **Natural Language Justification** (Gemini Pro)
- ⚖️ **Trust Scoring** for risk prioritization
- 🖥️ **Streamlit Dashboard** for visual interaction

> 🛡️ **Goal:** Increase trust, transparency, and user understanding in AI-powered fraud systems.

---

## 🎯 Key Features

- 📈 Detects unusual financial transactions per user
- 🤖 Generates clear explanations using Gemini LLM
- 🔐 Trust score identifies severity of flagged alerts
- 🖥️ Easy-to-use web interface (Streamlit)
- 📤 One-click PDF report generation

---

## 🛠️ Tech Stack

| Layer          | Tool / Library           |
|----------------|--------------------------|
| Language       | Python 3.12              |
| ML Detection   | Scikit-learn (Isolation Forest) |
| NLP Explainability | Gemini Pro (Google Generative AI) |
| Frontend       | Streamlit                |
| PDF Export     | FPDF                     |
| Data Handling  | Pandas, NumPy            |

---

## 🗂️ Project Structure

```bash
explainable-fraud-alert-system/
├── app.py                  # Streamlit UI
├── fraud_detector.py       # ML model logic
├── explain_with_gemini.py  # Gemini Pro integration
├── trust_score.py          # Trust score logic
├── report_generator.py     # PDF creation
├── sample_data.csv         # Sample transaction input
├── requirements.txt        # Dependencies
└── .env                    # Gemini API key
```
## 🚀 How It Works

📂 User uploads a transaction CSV
⚙️ ML model identifies anomalies
💬 Gemini API explains each flagged transaction
🔐 Trust score is calculated
📊 Results + PDF shown in dashboard

📥 Sample Input Format
  ## 📥 Sample Input Format

| user_id | amount | category | timestamp           |
|---------|--------|----------|---------------------|
| 101     | 599.99 | shopping | 2025-05-10 14:30:45 |
| 102     | 25000  | transfer | 2025-05-10 15:00:00 |

💬 Gemini Explanation Samples

“🔍 This transaction is flagged because it is significantly larger than your average and was made at an unusual hour.”

“⚠️ This transfer is to a new account not seen before in your transaction history.”

## 🧪 Setup Instructions

### Clone the repo
git clone https://github.com/yourusername/explainable-fraud-alert-system
cd explainable-fraud-alert-system

### Install dependencies
pip install -r requirements.txt

### Add Gemini API key to .env file
echo "GEMINI_API_KEY=your-key-here" > .env

### Launch the app
streamlit run app.py

## 📌 Future Enhancements

  - 🌐 Real-time fraud monitoring via bank APIs
  - 🗣️ Multilingual explanation support
  - 📉 Advanced behavioral graph visualization
  - 🔄 Auto-learning from user feedback

## 📄 License
  - This project is licensed under the MIT License – feel free to use and contribute!

## 👨‍💻 Author
  - Made with ❤️ by Rohith K
  - 📧 worksbyrohith@gmail.com

