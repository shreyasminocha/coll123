import sqlite3
import random
import uuid

from flask import Flask, session, request, redirect, flash, render_template
from playwright.sync_api import sync_playwright
from random_username.generate import generate_username


from secret import flag

app = Flask(__name__)
app.config["SECRET_KEY"] = random.randbytes(16).hex()
app.config["DATABASE"] = "database.db"

IS_DEBUG = False
HOST = "127.0.0.1:8000" if IS_DEBUG else "123.sec.rice.edu:50330"


@app.route("/wall/<user>", methods=["GET", "POST"])
def wall(user: str):
    db = sqlite3.connect(app.config["DATABASE"])

    if request.method == "GET":
        res = db.cursor().execute("select user from users where user=?", (user,))
        if not res.fetchone():
            return "user does not exist"

        res = db.cursor().execute("select text from posts where user=?", (user,))
        posts = res.fetchall()

        return f"""
            <form action="/post/{user}" method="GET">
                <input type="text" name="text" />
                <input type="submit" value="Post" />
            </form>

            <h2>Posts</h2>
            <ul>
                {' '.join([f'<li>{post[0]}</li>' for post in posts])}
            </ul>

            <form action="/simulate-admin" method="POST">
                <input type="hidden" name="user" value="{user}" />
                <input type="submit" value="view wall on behalf of admin" />
            </form>
        """

    if request.method == "POST":
        text = request.form.get("text", "empty")
        res = db.cursor().execute("insert into posts values(?, ?)", (user, text))
        db.commit()

        return redirect(f"/wall/{user}")


@app.route("/simulate-admin", methods=["POST"])
def simulate_admin():
    if request.method == "POST":
        user = request.form.get("user", None)
        if not user:
            return "no user specified"

        with sync_playwright() as p:
            browser = p.chromium.launch()
            browser_context = browser.new_context()
            browser_context.add_cookies(
                [
                    {
                        "name": "flag",
                        "value": flag,
                        "url": f"http://{HOST}/",
                        "httpOnly": False,
                    }
                ]
            )
            page = browser_context.new_page()
            page.goto(f"http://{HOST}/wall/{user}")
            browser.close()

        return "viewed wall on behalf of admin"


@app.route("/")
def index():
    [name] = generate_username(1)

    db = sqlite3.connect(app.config["DATABASE"])
    # let's just assume that the user doesn't exist
    res = db.cursor().execute("insert into users values(?)", (name,))
    db.commit()

    return redirect(f"/wall/{name}")


if IS_DEBUG:
    app.run(port=8000)
else:
    app.run(port=50330, host="0.0.0.0")
