import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load preprocessed data
with open("processed_data.pkl", "rb") as f:
    X_train, X_test, y_train, y_test = pickle.load(f)

# Initialize and train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Test model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained successfully with accuracy: {accuracy:.4f}")

# Save the trained model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved as model.pkl")
