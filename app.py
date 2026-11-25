import os
import sqlite3
from contextlib import closing

from flask import Flask, jsonify, render_template, request


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        DB_DRIVER=os.getenv("DB_DRIVER", "mysql"),
        SQLITE_PATH=os.getenv("SQLITE_PATH", "messages.db"),
        MYSQL_HOST=os.getenv("MYSQL_HOST", "localhost"),
        MYSQL_USER=os.getenv("MYSQL_USER", "devops"),
        MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD", ""),
        MYSQL_DB=os.getenv("MYSQL_DB", "devops"),
    )
    if config:
        app.config.update(config)

    def connect():
        if app.config["DB_DRIVER"] == "sqlite":
            return sqlite3.connect(app.config["SQLITE_PATH"])
        if app.config["DB_DRIVER"] != "mysql":
            raise ValueError("DB_DRIVER must be mysql or sqlite")
        import pymysql
        return pymysql.connect(
            host=app.config["MYSQL_HOST"], user=app.config["MYSQL_USER"],
            password=app.config["MYSQL_PASSWORD"], database=app.config["MYSQL_DB"],
            connect_timeout=5,
        )

    def init_db():
        column = "INTEGER PRIMARY KEY AUTOINCREMENT" if app.config["DB_DRIVER"] == "sqlite" else "INT AUTO_INCREMENT PRIMARY KEY"
        with closing(connect()) as conn, closing(conn.cursor()) as cur:
            cur.execute(f"CREATE TABLE IF NOT EXISTS messages (id {column}, message TEXT NOT NULL)")
            conn.commit()

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    @app.route("/")
    def index():
        with closing(connect()) as conn, closing(conn.cursor()) as cur:
            cur.execute("SELECT message FROM messages ORDER BY id")
            messages = cur.fetchall()
        return render_template("index.html", messages=messages)

    @app.route("/submit", methods=["POST"])
    def submit():
        message = (request.form.get("new_message") or "").strip()
        if not message or len(message) > 2000:
            return jsonify(error="Message must contain 1–2000 characters"), 400
        placeholder = "?" if app.config["DB_DRIVER"] == "sqlite" else "%s"
        with closing(connect()) as conn, closing(conn.cursor()) as cur:
            cur.execute(f"INSERT INTO messages (message) VALUES ({placeholder})", (message,))
            conn.commit()
        return jsonify(message=message)

    app.init_db = init_db
    return app


app = create_app()

if __name__ == "__main__":
    app.init_db()
    app.run(host=os.getenv("HOST", "127.0.0.1"), port=5000, debug=False)
