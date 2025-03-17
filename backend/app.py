from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model, scaler, and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        ad_topic_text = [data["Ad Topic Line"]]

        # Convert Ad Topic Line using the trained vectorizer
        ad_topic_features = vectorizer.transform(ad_topic_text).toarray()

        # Extract numerical features
        features = np.array([
            float(data["Daily Time Spent on Site"]),
            int(data["Age"]),
            float(data["Area Income"]),
            float(data["Daily Internet Usage"]),
            int(data["Gender"])
        ]).reshape(1, -1)

        # Combine numerical features with Ad Topic features
        final_features = np.hstack((features, ad_topic_features))

        # Standardize features using the same scaler
        final_features_scaled = scaler.transform(final_features)

        # Predict
        prediction = model.predict(final_features_scaled)[0]

        return jsonify({"prediction": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
