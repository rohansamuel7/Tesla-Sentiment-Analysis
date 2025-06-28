import praw
from utils.config import reddit_client_id, reddit_client_secret, reddit_username, reddit_password
from data_storage.db_connection import connect_db

def get_reddit_data(subreddit_name, keyword):
    reddit = praw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        username=reddit_username,
        password=reddit_password,
        user_agent='brand_sentiment_app'
    )

    conn = connect_db()
    cursor = conn.cursor()

    for submission in reddit.subreddit(subreddit_name).search(keyword, limit=5):
        post_id = submission.id
        title = submission.title
        post_text = submission.selftext
        created_at = submission.created_utc
        upvotes = submission.score

        cursor.execute("""
            INSERT INTO reddit_data (post_id, title, post_text, created_at, upvotes)
            VALUES (%s, %s, %s, to_timestamp(%s), %s)
        """, (post_id, title, post_text, created_at, upvotes))
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    get_reddit_data('technology', 'Tesla')
