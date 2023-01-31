import sqlite3
import time
from datetime import datetime
from flask import Flask, session, request, redirect, flash, render_template
from secret import flag

app = Flask(__name__)


app.config["DATABASE"] = "database.db"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return """
        <link rel="stylesheet" href="https://minimalcss.jwestman.net/minimal.min.css">

        <form method="POST">
            <p>
                <label for="name">Name</label>
                <input type="text" name="name" placeholder="John Doe" required>
            </p>

            <p>
                <label for="college">College</label>
                <input type="text" name="college" placeholder="Will Rice" required>
            </p>

            <p>
                <label for="fav-month">Favourite Month</label>
                <input type="text" name="fav-month" placeholder="January" required>
            </p>

            <input type="submit" value="submit">
        </form>
        """

    if request.method == "POST":
        name = request.form.get("name", None)
        college = request.form.get("college", None)
        fav_month = request.form.get("fav-month", None)

        if not (name and college and fav_month):
            return "please fill all three form fields!"

        now = int(time.time())

        db = sqlite3.connect(app.config["DATABASE"])
        row_id = None
        try:
            res = db.cursor().execute(
                f"INSERT INTO submissions (name, college, fav_month, timestamp) VALUES('{name}', '{college}', '{fav_month}', {now})"
            )
            row_id = res.lastrowid
            db.commit()
        except:
            return "uh something went wrong. sorry."

        assert row_id is not None

        res = db.cursor().execute(
            "SELECT timestamp FROM submissions where id = ?", (row_id,)
        )
        timestamp = res.fetchone()[0]

        twenty_twenty = datetime(2020, 1, 1).timestamp()
        if timestamp < twenty_twenty:
            return flag

        return "too late! you submitted after 2020…"


if __name__ == "__main__":
    app.run(port=8000)
