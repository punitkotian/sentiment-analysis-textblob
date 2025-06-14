import pandas as pd
from textblob import TextBlob

# Load reviews
df = pd.read_csv("reviews.csv")

# Sentiment analysis
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["sentiment"] = df["review"].apply(get_sentiment)

# Display results
print(df)
