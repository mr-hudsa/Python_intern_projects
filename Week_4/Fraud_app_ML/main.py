from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI(title="Week 4 - Chat + Fraud Detection")

# Load trained model
model = joblib.load("fraud_model.pkl")

@app.post("/fraud-detect-ml/")
def fraud_detect_ml(amount: float, location: int):
    features = np.array([[amount, location]])
    prediction = model.predict(features)[0]
    return {
        "amount": amount,
        "location": location,
        "fraud": bool(prediction)
    }
