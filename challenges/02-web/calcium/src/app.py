from math import *
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        query = request.form.get("query", "")
        try:
            result = eval(query)
        except Exception as e:
            result = "error"

        return render_template("index.html", result=result)
