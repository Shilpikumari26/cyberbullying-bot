import pandas as pd

# Load the CSV
df = pd.read_csv("data/cyberbullying_tweets.csv")

# Show first few rows
print("First 5 rows:")
print(df.head())

# Check column names
print("\nColumns:")
print(df.columns)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check unique labels
label_col = "label"
print("\nLabel counts:")
print(df[label_col].value_counts())

# Optional: check any empty tweet text
text_col = "text"
empty_texts = df[df[text_col].isnull()]
print("\nRows with empty tweet text:", len(empty_texts))