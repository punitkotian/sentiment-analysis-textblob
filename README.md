# Sentiment Analysis Using TextBlob

## Overview

This is a simple Natural Language Processing (NLP) project that performs **sentiment analysis** on textual data using **Python** and the **TextBlob** library. The goal is to classify text (such as movie reviews or tweets) as **Positive**, **Negative**, or **Neutral** based on the overall sentiment expressed.

This beginner-friendly project demonstrates how to:

- Preprocess and load review data
- Analyze sentiment using `TextBlob`
- Apply sentiment classification
- Optionally evaluate performance with labeled datasets

---

## Features

- Automatically detects sentiment polarity
- Classifies reviews into `Positive`, `Negative`, or `Neutral`
- Uses TextBlob's built-in sentiment engine (no model training required)
- Works with CSV files like IMDb reviews or any custom data

---

## Technologies Used

- Python 3.x
- [TextBlob](https://textblob.readthedocs.io/en/dev/) – for sentiment polarity
- Pandas – for data loading and manipulation

---

## File Structure

```
sentiment-analysis-textblob/
├── reviews.csv                # Sample input data (one review per line)
├── sentiment_analysis.py      # Python script to process and classify sentiment
└── README.md                  # Project documentation
```

---

## How It Works

1. The script reads reviews from a `CSV` file (`reviews.csv`).
2. Each review is passed to TextBlob for polarity scoring.
3. Based on polarity:

   - `> 0` → Positive
   - `< 0` → Negative
   - `== 0` → Neutral

4. Results are stored in a new column and printed/displayed.

---

## Sample Output

| Review                               | Sentiment |
| ------------------------------------ | --------- |
| I loved the movie. It was fantastic! | Positive  |
| The plot was boring and predictable. | Negative  |
| It was an okay experience. Not bad.  | Neutral   |

---

## How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-textblob.git
   cd sentiment-analysis-textblob
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   python -m textblob.download_corpora
   ```

3. Add your own reviews in `reviews.csv` or use the sample.

4. Run the script:

   ```bash
   python sentiment_analysis.py
   ```
