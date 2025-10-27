import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "raise_on_warnings": True,
    "autocommit": False
}

def get_conn():
    return mysql.connector.connect(**CONFIG)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        role VARCHAR(255),
        city VARCHAR(255)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
