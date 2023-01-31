import sqlite3
from flask import Flask, session, request, redirect, flash
from secret import flag

app = Flask(__name__)


app.config["DATABASE"] = "database.db"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return """
            <form method="POST">
                <input type="text" name="username" placeholder="admin">
                <input type="password" name="password" placeholder="hunter2">
                <input type="submit" value="Search">
            </form>

            <small>btw logins aren't persisted coz i'm lazy</small>
        """

    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        if not username or not password:
            return "missing credentials"

        print(password)

        db = sqlite3.connect(app.config["DATABASE"])
        res = db.cursor().execute(
            f"SELECT username FROM users WHERE username='{username}' and password='{password}'"
        )

        user = res.fetchone()
        if not user:
            return "invalid credentials"

        if user[0] == "admin":
            return flag

        return "hi user"


if __name__ == "__main__":
    app.run(port=8000)
