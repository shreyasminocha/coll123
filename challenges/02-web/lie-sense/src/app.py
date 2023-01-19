import json
from flask import Flask, request, render_template

app = Flask(__name__)
valid_keys = open("keys.txt").read().splitlines()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/keys")
def keys():
    return json.dumps(valid_keys)


@app.route("/product", methods=["POST"])
def product():
    key = request.form.get("key", "-")

    if key not in valid_keys:
        return "<pre>invalid key!</pre>"

    return f"<pre>{open('flag.txt').read()}</pre>"
