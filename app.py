from flask import Flask, request, jsonify
from db_mysql import get_conn

app = Flask(__name__)

@app.route("/")
def home():
    return "API is working!"

@app.route("/people", methods=["GET"])
def get_people():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    offset = (page - 1) * per_page

    conn = get_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM people LIMIT %s OFFSET %s", (per_page, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route("/people/search", methods=["GET"])
def search_people():
    name = request.args.get("name")
    role = request.args.get("role")
    city = request.args.get("city")

    query = "SELECT * FROM people WHERE 1=1"
    params = []

    if name:
        query += " AND name LIKE %s"
        params.append(f"%{name}%")
    if role:
        query += " AND role LIKE %s"
        params.append(f"%{role}%")
    if city:
        query += " AND city LIKE %s"
        params.append(f"%{city}%")

    conn = get_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute(query, params)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
