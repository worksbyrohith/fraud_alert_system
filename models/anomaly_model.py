import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

def train_model(csv_path):
    df = pd.read_csv(csv_path)
    features = pd.get_dummies(df[['amount', 'location']])
    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(features)
    joblib.dump(model, 'models/fraud_model.pkl')

if __name__ == '__main__':
    train_model('data/sample_transactions.csv')