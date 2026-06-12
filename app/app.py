from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# DB path — works locally and in Docker
DB_PATH = os.environ.get("DB_PATH", "tasks.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # returns dict-like rows
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            title     TEXT    NOT NULL,
            done      INTEGER DEFAULT 0,
            created   TEXT    DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()

# ── Routes ──────────────────────────────────────────

@app.route("/health", methods=["GET"])
def health():
    """ECS uses this to check if container is alive"""
    return jsonify({"status": "healthy"}), 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return jsonify([dict(t) for t in tasks]), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "title is required"}), 400
    conn = get_db()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (data["title"],))
    conn.commit()
    conn.close()
    return jsonify({"message": "task created"}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    conn = get_db()
    conn.execute(
        "UPDATE tasks SET done = ? WHERE id = ?",
        (data.get("done", 0), task_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "task updated"}), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "task deleted"}), 200

# ── Start ────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)