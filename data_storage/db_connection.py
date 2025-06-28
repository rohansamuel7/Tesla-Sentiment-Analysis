import psycopg2
from utils.config import postgres_host, postgres_db, postgres_user, postgres_password

def connect_db():
    conn = psycopg2.connect(
        host=postgres_host,
        database=postgres_db,
        user=postgres_user,
        password=postgres_password
    )
    return conn
