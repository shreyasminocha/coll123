import sqlite3
from flask import Flask, session, request, redirect, flash, render_template

app = Flask(__name__)


app.config["DATABASE"] = "database.db"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        query = request.form.get("query", "")

        db = sqlite3.connect(app.config["DATABASE"])
        res = db.cursor().execute(
            f"SELECT name, path FROM files WHERE name LIKE '%{query}%' AND access != 'premium'"
        )

        content = res.fetchall()
        if not content:
            return "nothing found"

        return render_template("index.html", results=content)


if __name__ == "__main__":
    app.run(port=8000)
