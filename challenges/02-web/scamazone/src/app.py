import sqlite3
import random
from flask import Flask, session, request, redirect, flash, render_template
from secret import flag

app = Flask(__name__)
app.config["SECRET_KEY"] = random.randbytes(16).hex()
app.config["DATABASE"] = "database.db"

flag_price = 500
bullshit = [
    "tsa no fly list",
    "epstein jail cell footage",
    "shreyas' transcripts",
    "morbius dvd",
    "windows 11 zero day vulnerabilities",
]


@app.route("/")
def index():
    username = session.get("username", None)

    if not username:
        return """
            <a href="/login">Login</a>
            <a href="/register">Register</a>
        """

    db = sqlite3.connect(app.config["DATABASE"])
    res = db.cursor().execute(f"SELECT rowbux FROM users WHERE username=?", (username,))
    user = res.fetchone()

    if not user:
        return "something went wrong. are you logged in?"

    return render_template(
        "store.html",
        rowbux=user[0],
        flag_price=flag_price,
        bullshit=bullshit,
    )


@app.route("/buy/flag", methods=["POST"])
def buy_flag():
    if request.method == "POST":
        username = session.get("username", None)
        if not username:
            return "register/login first"

        db = sqlite3.connect(app.config["DATABASE"])
        res = db.cursor().execute(
            f"SELECT rowbux, username FROM users WHERE username=?", (username,)
        )

        user = res.fetchone()
        if not user:
            return "invalid credentials"

        if user[0] >= flag_price:
            return flag

        return "need more rowbux"


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
            f"SELECT username FROM users WHERE username='{username}' and password='{password}'"
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

        db.cursor().execute(
            f"INSERT INTO users (username, password, rowbux) VALUES (?, ?, 10)",
            (username, password),
        )
        db.commit()

        return redirect("/login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(port=8000)
