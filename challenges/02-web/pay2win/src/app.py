import sqlite3
import random
from flask import Flask, session, request, redirect, flash, render_template
from secret import flag

app = Flask(__name__)
app.config["SECRET_KEY"] = random.randbytes(16).hex()
app.config["DATABASE"] = "database.db"


@app.route("/flag")
def view_flag():
    username = session.get("username", None)
    if not username:
        return "register/login first"

    db = sqlite3.connect(app.config["DATABASE"])
    res = db.cursor().execute("SELECT type FROM users WHERE username=?", (username,))

    user = res.fetchone()
    if not user:
        return "invalid credentials"

    if user[0] == "pro":
        return flag

    return "you must be a 'pro' user to access this content"


@app.route("/rename", methods=["GET", "POST"])
def rename():
    username = session.get("username", None)
    if not username:
        return "register/login first"

    if request.method == "GET":
        return """
            <form method="POST">
                <input type="text" name="new_name" placeholder="new name">
                <input type="submit" value="Submit">
            </form>
        """

    if request.method == "POST":
        new_name = request.form.get("new_name", None)

        db = sqlite3.connect(app.config["DATABASE"])
        res = db.cursor().execute(
            f"UPDATE users SET name='{new_name}' WHERE username=?",
            (username,),
        )
        db.commit()

        return redirect("/")


@app.route("/upgrade")
def upgrade():
    username = session.get("username", None)
    if not username:
        return "register/login first"

    return "<marquee>coming soon (tm)</marquee>"


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
        "SELECT name, type FROM users WHERE username=?", (username,)
    )
    user = res.fetchone()

    if not user:
        return "something went wrong. are you logged in?"

    return render_template("index.html", name=user[0], type=user[1])


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
            "SELECT * FROM users WHERE username=? and password=?", (username, password)
        )

        user = res.fetchone()
        if user:
            return "user already exists"

        db.cursor().execute(
            "INSERT INTO users (username, name, password, type) VALUES (?, ?, ?, 'regular')",
            (username, username, password),
        )
        db.commit()

        return redirect("/login")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(port=8000)
