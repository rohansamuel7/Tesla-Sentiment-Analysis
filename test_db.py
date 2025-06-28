import psycopg2
from utils.config import postgres_host, postgres_db, postgres_user, postgres_password

try:
    conn = psycopg2.connect(
        host=postgres_host,
        database=postgres_db,
        user=postgres_user,
        password=postgres_password
    )
    print("✅ Database connection successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
