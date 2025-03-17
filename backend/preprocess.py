import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load dataset
dataset_path = "../addata.csv"
df = pd.read_csv(dataset_path)

# Drop unnecessary columns
df = df.drop(["City", "Country", "Timestamp"], axis=1)

# Convert categorical column 'Gender' to numerical
df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})

# Convert 'Ad Topic Line' to numerical using TF-IDF
vectorizer = TfidfVectorizer(max_features=10)  # Adjust based on dataset
ad_topic_features = vectorizer.fit_transform(df["Ad Topic Line"]).toarray()
ad_topic_df = pd.DataFrame(ad_topic_features, columns=[f"Ad_Topic_{i}" for i in range(ad_topic_features.shape[1])])

# Merge new Ad Topic features and drop original column
df = pd.concat([df.drop("Ad Topic Line", axis=1), ad_topic_df], axis=1)

# Define features (X) and target (y)
X = df.drop("Clicked on Ad", axis=1)
y = df["Clicked on Ad"]

# Normalize numerical columns
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save the scaler & vectorizer for future use
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Save processed data
with open("processed_data.pkl", "wb") as f:
    pickle.dump((X_train, X_test, y_train, y_test), f)

print("✅ Data preprocessing completed and saved successfully.")
