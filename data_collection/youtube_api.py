from googleapiclient.discovery import build
from utils.config import youtube_api_key
from data_storage.db_connection import connect_db

def get_youtube_data(keyword):
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    request = youtube.search().list(q=keyword, part='snippet', maxResults=5)
    response = request.execute()

    conn = connect_db()
    cursor = conn.cursor()

    for item in response['items']:
        video_id = item['id'].get('videoId')
        if not video_id:
            continue
        title = item['snippet']['title']
        description = item['snippet']['description']
        published_at = item['snippet']['publishedAt']
        print(f"Inserting video_id={video_id}, title={title}")

        cursor.execute("""
            INSERT INTO youtube_data (video_id, title, description, published_at)
            VALUES (%s, %s, %s, %s)
        """, (video_id, title, description, published_at))
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    get_youtube_data('Tesla')

