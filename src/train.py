import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from preprocess import clean_text

# 1. Load dataset
df = pd.read_csv("../data/cyberbullying_tweets.csv")

print("Columns in dataset:", df.columns)
print(df.head())

# 2. Adjust column names based on dataset
# If your dataset has different names, change them here:
text_col = "tweet_text"          # column with tweet text
label_col = "cyberbullying_type" # column with labels

# 3. Convert to binary (bullying vs safe)
def map_label(lbl):
    if str(lbl).lower().strip() in ["not_cyberbullying", "none", "safe", "no cyberbullying"]:
        return "safe"
    else:
        return "bullying"

df["label"] = df[label_col].apply(map_label)

# 4. Clean text
df["clean_text"] = df[text_col].apply(clean_text)

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    df["clean_text"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

# 6. TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 7. Train Logistic Regression model
model = LogisticRegression(max_iter=300, class_weight="balanced")
model.fit(X_train_vec, y_train)

# 8. Evaluate
y_pred = model.predict(X_test_vec)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))