import sqlite3
import random
import uuid
import json
import html

from flask import Flask, session, request, redirect, flash, render_template
from playwright.sync_api import sync_playwright

from secret import flag

app = Flask(__name__)
app.config["SECRET_KEY"] = random.randbytes(16).hex()
app.config["DATABASE"] = "database.db"

IS_DEBUG = False
HOST = "127.0.0.1:8000" if IS_DEBUG else "123.sec.rice.edu:50350"


@app.route("/posts/<category>", methods=["GET", "POST"])
def posts(category: str):
    db = sqlite3.connect(app.config["DATABASE"])
    res = db.cursor().execute(
        "select category from categories where category=?", (category,)
    )
    if not res.fetchone():
        return "not like this; use the <a href='/'>auto-generated categories</a>!"

    if request.method == "GET":
        res = db.cursor().execute(
            "select title, url from posts where category=?", (category,)
        )
        posts = res.fetchall()

        return render_template("posts.html", category=category, posts=posts)

    if request.method == "POST":
        data = {}
        try:
            data = json.loads(request.data.decode("utf-8"))
        except:
            return "invalid json"

        title = data.get("title", "an interesting title")
        url = data.get("url", "https://example.com")

        # no scripts!!!!!!11
        url = url.replace("<", "").replace(">", "")

        try:
            res = db.cursor().execute(
                "insert into posts values(?, ?, ?)", (category, title, url)
            )
            db.commit()
        except:
            return "something went wrong"

        return "post added"


@app.route("/simulate-admin", methods=["POST"])
def simulate_admin():
    if request.method == "POST":
        category = request.form.get("category", None)
        if not category:
            return "no category specified"

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
            page.goto(f"http://{HOST}/posts/{category}")
            browser.close()

        return "viewed wall on behalf of admin"


@app.route("/")
def index():
    db = sqlite3.connect(app.config["DATABASE"])
    category_name = str(uuid.uuid4())[:8]

    res = db.cursor().execute("insert into categories values(?)", (category_name,))
    db.commit()

    return redirect(f"/posts/{category_name}")


if IS_DEBUG:
    app.run(port=8000)
else:
    app.run(port=50350, host="0.0.0.0")
