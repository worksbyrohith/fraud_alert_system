import pandas as pd
import joblib

def load_model():
    return joblib.load('models/fraud_model.pkl')

def preprocess(transaction_df):
    return pd.get_dummies(transaction_df[['amount', 'location']])

def compute_trust_score(is_flagged):
    return 2.0 if is_flagged else 8.5