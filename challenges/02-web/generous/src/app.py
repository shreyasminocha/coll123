import sqlite3
import random
from urllib.parse import urlencode

from flask import Flask, session, request, redirect, flash, render_template
from flask.sessions import SecureCookieSessionInterface
from playwright.sync_api import sync_playwright

from secret import flag

app = Flask(__name__)
app.config["SECRET_KEY"] = random.randbytes(16).hex()
app.config["DATABASE"] = "database.db"

IS_DEBUG = False
HOST = "127.0.0.1:8000" if IS_DEBUG else "123.sec.rice.edu:50360"

session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)


@app.route("/flag")
def view_flag():
    username = session.get("username", None)
    if not username:
        return "register/login first"

    db = sqlite3.connect(app.config["DATABASE"])
    res = db.cursor().execute(
        "SELECT subscribed FROM users WHERE username=?", (username,)
    )

    user = res.fetchone()
    if not user:
        return "invalid credentials"

    if user[0] == 1:
        return flag

    return "not subscribed :("


@app.route("/gift/<giftee>", methods=["GET"])
def gift(giftee: str):
    gifter = session.get("username", None)
    if gifter != "admin":
        return "only admins can gift subscriptions"

    db = sqlite3.connect(app.config["DATABASE"])
    try:
        res = db.cursor().execute(
            "select username from users where username=?", (giftee,)
        )
        if not res.fetchone():
            return "invalid username"

        res = db.cursor().execute(
            "update users set subscribed=1 where username=?", (giftee,)
        )
        db.commit()
    except:
        return "something went wrong"

    return "successfully gifted a subscription to " + giftee


@app.route("/search-as-admin", methods=["GET"])
def search_as_admin():
    query = request.args.get("q", "example")
    simulated_session = session_serializer.dumps({"username": "admin"})

    with sync_playwright() as p:
        browser = p.firefox.launch()
        browser_context = browser.new_context()
        browser_context.add_cookies(
            [
                {
                    "name": "session",
                    "value": simulated_session,
                    "url": f"http://{HOST}/",
                }
            ]
        )
        page = browser_context.new_page()
        page.goto(f"http://{HOST}/?q={query}")
        browser.close()

    return "searched on behalf of admin"


@app.route("/")
def index():
    username = session.get("username", None)
    if not username:
        return """
            <ul>
                <li><a href="/login">Login</a></li>
                <li><a href="/register">Register</a></li>
            </ul>
        """

    db = sqlite3.connect(app.config["DATABASE"])
    res = db.cursor().execute(
        f"SELECT username FROM users WHERE username=?", (username,)
    )
    user = res.fetchone()
    if not user:
        return "something went wrong. are you logged in?"

    query = request.args.get("q", None)
    if not query:
        return render_template("search.html")
    print(query)

    db = sqlite3.connect(app.config["DATABASE"])
    res = db.cursor().execute(
        "SELECT name FROM streamers WHERE name LIKE ?", ("%" + query + "%",)
    )

    streamers = res.fetchall()
    return render_template("search.html", query=query, streamers=streamers)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        if not username or not password:
            return "missing credentials"

        db = sqlite3.connect(app.config["DATABASE"])
        res = db.cursor().execute(
            "SELECT username FROM users WHERE username=? and password=?",
            (username, password),
        )

        user = res.fetchone()
        if not user:
            return "invalid credentials"

        session["username"] = user[0]
        return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        if not username or not password:
            return "missing credentials"

        db = sqlite3.connect(app.config["DATABASE"])
        res = db.cursor().execute(
            f"SELECT * FROM users WHERE username=? and password=?", (username, password)
        )
        user = res.fetchone()
        if user:
            return "user already exists"

        # no sql injections lol dw
        db.cursor().execute(
            f"INSERT INTO users (username, password, subscribed) VALUES (?, ?, 0)",
            (username, password),
        )
        db.commit()

        return redirect("/login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if IS_DEBUG:
    app.run(port=8000)
else:
    app.run(port=50360, host="0.0.0.0")
