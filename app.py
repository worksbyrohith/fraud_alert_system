import streamlit as st
import pandas as pd
from utils import load_model, preprocess, compute_trust_score
from nlp_module.explainer import generate_explanation

st.title("🔍 Explainable Fraud Alert System")

uploaded_file = st.file_uploader("Upload transaction CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    model = load_model()
    X = preprocess(df)
    preds = model.predict(X)
    df['flagged'] = preds == -1
    df['trust_score'] = df['flagged'].apply(compute_trust_score)

    st.write("### Results:")
    st.dataframe(df)

    for idx, row in df[df['flagged']].iterrows():
        explanation = generate_explanation(row)
        st.write(f"#### Explanation for Transaction {row['transaction_id']}:")
        st.info(explanation)