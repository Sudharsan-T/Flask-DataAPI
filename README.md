# Flask MySQL Data API

A simple Flask-based REST API that connects to a MySQL database, allowing you to fetch, search, and manage people data efficiently.  
This project demonstrates clean modular design, environment-based configuration, and data upsertion from JSON files.

---

## 📂 Project Structure

The project is organized as follows:

```

.
├── app.py              # Main Flask application (API endpoints)
├── db_mysql.py         # Database connection and initialization logic
├── load_json.py        # Script to load sample data from JSON into MySQL
├── data.json           # Sample dataset to populate the database
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (DB credentials)
└── **pycache**/        # Auto-generated compiled Python files

```

---

## 🏗️ Architecture Overview

**Textual Representation of Architecture:**

```

```
    ┌──────────────────────────────┐
    │         Client (User)        │
    │  (Browser / API Consumer)    │
    └──────────────┬───────────────┘
                   │
                   ▼
          ┌───────────────────┐
          │     Flask API     │
          │     (app.py)      │
          │-------------------│
          │ - Defines routes  │
          │ - Handles requests│
          │ - Returns JSON    │
          └────────┬──────────┘
                   │
                   ▼
          ┌───────────────────┐
          │   Database Layer  │
          │   (db_mysql.py)   │
          │-------------------│
          │ - Connects to MySQL│
          │ - Manages schema   │
          │ - Handles queries  │
          └────────┬──────────┘
                   │
                   ▼
          ┌───────────────────┐
          │   MySQL Database  │
          │  (people table)   │
          └───────────────────┘

                   ▲
                   │
           ┌─────────────────┐
           │ load_json.py    │
           │ Reads data.json │
           │ Inserts/Updates │
           └─────────────────┘
```

````

---

## ⚙️ Features

- ✅ **REST API** with Flask  
- ✅ **MySQL Integration** using `mysql-connector-python`  
- ✅ **Environment Variables** via `.env`  
- ✅ **Pagination** for efficient data retrieval  
- ✅ **Upsert Logic** (`ON DUPLICATE KEY UPDATE`) for seamless data loading  
- ✅ **Modular Design** — separate files for app, DB, and data loading  

---

## 🚀 API Endpoints

### 1. Health Check  
**GET /**  
Returns a simple message to confirm the API is running.

**Example Response:**
```json
{"message": "API is running!"}
````

---

### 2. Fetch Paginated People Data

**GET /people?page=1&limit=10**

Fetches paginated results of people stored in the database.

**Example Response:**

```json
{
  "page": 1,
  "limit": 10,
  "total": 50,
  "data": [
    {"id": 1, "name": "John Doe", "role": "Engineer", "city": "Chennai"},
    ...
  ]
}
```

---

### 3. Search People

**GET /people/search?name=John&role=Engineer&city=Chennai**

Searches people based on name, role, or city (supports partial matches).

**Example Response:**

```json
{
  "results": [
    {"id": 2, "name": "John Smith", "role": "Engineer", "city": "Chennai"}
  ]
}
```

---

## 🗄️ Database Structure

**Table Name:** `people`

| Column | Type            | Description       |
| ------ | --------------- | ----------------- |
| id     | INT PRIMARY KEY | Unique identifier |
| name   | VARCHAR(100)    | Person’s name     |
| role   | VARCHAR(100)    | Job role          |
| city   | VARCHAR(100)    | City name         |

---

## 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sudharsan-T/Flask-DataAPI
cd Flask-DataAPI
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Create a `.env` file in the root directory with your MySQL credentials:

```
DB_HOST=localhost
DB_USER=root
DB_PASS=root
DB_NAME=assignment_db
DB_PORT=3306
```

### 5. Initialize the Database

```bash
python load_json.py
```

This will:

* Create the `people` table (if not exists)
* Load and upsert data from `data.json`

### 6. Run the Flask Application

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 📦 Dependencies

Listed in `requirements.txt`:

```
flask
mysql-connector-python
python-dotenv
```

---

## 🧩 Best Practices Followed

✅ **Environment Variables:** Secure credential management using `.env`
✅ **Pagination:** Efficient data handling for large datasets
✅ **Upsert Logic:** Avoids duplicate entries on data load
✅ **Modular Code:** Easy to maintain and extend
✅ **Parameterized Queries:** Prevents SQL injection

---

## 🚧 Areas for Improvement

* **Error Handling:** Add better try/except blocks for DB and API failures
* **Validation:** Validate query parameters to ensure safe inputs
* **Documentation:** Add API usage examples and curl commands
* **Testing:** Include unit tests for endpoints and DB operations
* **Connection Pooling:** Improve scalability for high traffic

---

## 🧠 Do’s and Don’ts

### ✅ Do’s

* Use `.env` for sensitive data
* Validate and sanitize user inputs
* Use pagination for large datasets
* Write clean, modular, and documented code

### ❌ Don’ts

* Don’t hardcode database credentials
* Don’t expose sensitive debug info in API responses
* Don’t use global DB connections

---

## 💡 Future Enhancements

* 🔍 Add sorting and advanced filters
* 🧪 Implement unit tests with `pytest`
* 📈 Add performance monitoring and caching
* 🔐 Integrate with AWS Secrets Manager for credential security

---

## 👨‍💻 Author

**Sudharsan T**
Flask Developer | AI Enthusiast | Open Source Contributor
🔗 [GitHub Profile](https://github.com/Sudharsan-T)

---

## 🏁 License

This project is licensed under the **MIT License** — feel free to use and modify it as per your needs.

```
```
