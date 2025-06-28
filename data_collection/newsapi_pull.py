import requests
from utils.config import news_api_key
from data_storage.db_connection import connect_db

def get_news_data(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={news_api_key}"
    response = requests.get(url).json()

    conn = connect_db()
    cursor = conn.cursor()

    for article in response.get('articles', []):
        # use URL as a unique ID
        article_id  = article.get('url')
        title       = article.get('title')
        description = article.get('description')
        content     = article.get('content')
        published_at= article.get('publishedAt')
        source_name = article.get('source', {}).get('name')
        author      = article.get('author')

        cursor.execute("""
            INSERT INTO news_data
              (article_id, title, description, content, published_at, source_name, author, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (article_id) DO NOTHING
        """, (
            article_id, title, description, content,
            published_at, source_name, author, article_id
        ))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    get_news_data('Tesla')
