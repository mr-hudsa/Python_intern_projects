from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Fraud Detection API")

# -------------------------
# Input Schema
# -------------------------
class Transaction(BaseModel):
    amount: float
    location: str
    device: str
    past_fraud: bool

# -------------------------
# Fraud Detection Logic
# -------------------------
@app.post("/predict_fraud/")
async def predict_fraud(tx: Transaction):
    score = 0

    # Rule 1: Very high amount
    if tx.amount > 10000:
        score += 3

    # Rule 2: Suspicious location
    if tx.location.lower() not in ["india", "usa", "uk"]:
        score += 2

    # Rule 3: New or risky device
    if tx.device.lower() in ["unknown", "emulator", "vpn"]:
        score += 2

    # Rule 4: If user had past fraud cases
    if tx.past_fraud:
        score += 3

    # Decision
    if score >= 5:
        return {"fraud": True, "risk_score": score, "message": "⚠️ High Fraud Risk"}
    elif score >= 3:
        return {"fraud": True, "risk_score": score, "message": "Suspicious Transaction"}
    else:
        return {"fraud": False, "risk_score": score, "message": "✅ Safe Transaction"}
