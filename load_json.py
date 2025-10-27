import json
from db_mysql import init_db, get_conn
def load_json_to_db(json_path="data.json"):
    init_db()

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    selected = ["id","name","age","role","city"]
    rows = []
    for item in data:
        row = (
            int(item.get("id")),
            item.get("name"),
            int(item.get("age")) if item.get("age") is not None else None,
            item.get("role"),
            item.get("city")
        )
        rows.append(row)

    conn = get_conn()
    cur = conn.cursor()
    sql = "INSERT INTO people (id, name, age, role, city) VALUES (%s, %s, %s, %s, %s)"
    cur.executemany(sql, rows)
    conn.commit()
    print(f"Inserted/Updated {cur.rowcount} rows.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    load_json_to_db()