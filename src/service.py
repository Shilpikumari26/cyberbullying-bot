import joblib
from preprocess import clean_text

# Load saved model and vectorizer
model = joblib.load("../models/model.pkl")
vectorizer = joblib.load("../models/vectorizer.pkl")

def predict(text: str) -> str:
    """
    Predict whether a text is bullying or safe.
    """
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    return pred

if __name__ == "__main__":
    # Test examples
    samples = [
        "You are such a loser!",
        "Have a great day my friend!"
    ]
    for s in samples:
        print(f"{s} --> {predict(s)}")