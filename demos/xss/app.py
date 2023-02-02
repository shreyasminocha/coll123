import sqlite3
import random
import uuid

from flask import Flask, session, request, redirect, flash, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = random.randbytes(16).hex()


@app.route("/", methods=["GET"])
def index():
    text = request.args.get("text", "n/a")
    return f"""
        <form>
            <input type="text" name="text" />
            <input type="submit" value="echo" />
        </form>

        <p>text was {text}</p>
    """


@app.route("/login")
def login():
    # just a simulated login, obviously
    session["username"] = "admin"
    return "logged in"


@app.route("/change-password", methods=["GET"])
def change_password():
    print(f"change password for {session['username']}")
    return f"<p>done</p>"


if __name__ == "__main__":
    app.run(port=8000)
