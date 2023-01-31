import sqlite3
from flask import Flask, session, request, redirect, flash

app = Flask(__name__)


app.config["DATABASE"] = "database.db"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return """
            <form method="POST">
                <input type="text" name="query" placeholder="something">
                <input type="submit" value="Search">
            </form>
        """

    if request.method == "POST":
        query = request.form.get("query", None)

        if not query:
            return "enter a query"

        db = sqlite3.connect(app.config["DATABASE"])
        res = db.cursor().execute(
            f"SELECT content FROM data WHERE content like '{query}'"
        )

        content = res.fetchall()
        if not content:
            return "nothing found"

        return content


if __name__ == "__main__":
    app.run(port=8000)
