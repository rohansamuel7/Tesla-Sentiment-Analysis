from nltk.sentiment.vader import SentimentIntensityAnalyzer
from data_storage.db_connection import connect_db

def analyze_sentiment():
    conn = connect_db()
    cursor = conn.cursor()
    sid = SentimentIntensityAnalyzer()

    # For Analyzing YouTube descriptions
    cursor.execute("SELECT id, description FROM youtube_data WHERE sentiment_score IS NULL")
    rows = cursor.fetchall()
    for row in rows:
        sentiment = sid.polarity_scores(row[1])['compound'] if row[1] else 0
        cursor.execute("UPDATE youtube_data SET sentiment_score=%s WHERE id=%s", (sentiment, row[0]))

    # For Analyzing Reddit posts
    cursor.execute("SELECT id, title FROM reddit_data WHERE sentiment_score IS NULL")
    rows = cursor.fetchall()
    print("Rows to update:", len(rows))     # How many rows will you process?

    for rec_id, text in rows:
        print(f"Processing id={rec_id!r} text_length={len(text or '')}")  # Debug
        score = sid.polarity_scores(text or "")["compound"]
        cursor.execute(
            "UPDATE reddit_data SET sentiment_score = %s WHERE id = %s",
            (score, rec_id)
        )

    # For Analyzing News descriptions
    cursor.execute("SELECT id, description FROM news_data WHERE sentiment_score IS NULL")
    rows = cursor.fetchall()
    for row in rows:
        sentiment = sid.polarity_scores(row[1])['compound'] if row[1] else 0
        cursor.execute("UPDATE news_data SET sentiment_score=%s WHERE id=%s", (sentiment, row[0]))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    analyze_sentiment()


