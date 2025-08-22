import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Step 1: Generate fake dataset
np.random.seed(42)
data = pd.DataFrame({
    "amount": np.random.randint(10, 1000, 500),   # transaction amount
    "location": np.random.randint(0, 2, 500),     # 0 = local, 1 = foreign
    "is_fraud": np.random.randint(0, 2, 500)      # 0 = normal, 1 = fraud
})

X = data[["amount", "location"]]
y = data["is_fraud"]

# Step 2: Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 4: Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Step 5: Save the model
joblib.dump(model, "fraud_model.pkl")
print("✅ Fraud detection model saved as fraud_model.pkl")
