import mysql.connector
import json
import os
from dotenv import load_dotenv
load_dotenv()

def load_json_to_db():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            role VARCHAR(255),
            city VARCHAR(255)
        )
    """)

    # Load JSON file
    with open("data.json", "r") as f:
        data = json.load(f)

    # Prepare rows
    rows = [(p["id"], p["name"], p["age"], p["role"], p["city"]) for p in data]

    # Insert or update
    sql = """
    INSERT INTO people (id, name, age, role, city)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    age = VALUES(age),
    role = VALUES(role),
    city = VALUES(city)
    """

    cur.executemany(sql, rows)
    conn.commit()

    print(f"✅ {cur.rowcount} rows inserted or updated successfully!")

    cur.close()
    conn.close()

if __name__ == "__main__":
    load_json_to_db()
