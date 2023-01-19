from flask import Flask, session, request, redirect, flash

app = Flask(__name__)


@app.route("/")
def index():
    return "hi!! the flag is at <a href='/flag'><code>/flag</code></a>", {
        "set-cookie": "role=user"
    }


@app.route("/flag", methods=["GET"])
def flag():
    if request.method == "GET":
        if request.cookies["role"] == "admin":
            return open("flag.txt").read()

    return "You must have the 'admin' role to view the flag"
