from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "myapp"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword")
    )


@app.route("/")
def home():
    return "Hello DevOps!"


@app.route("/data")
def data():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT message FROM messages ORDER BY id;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([row[0] for row in rows])


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)