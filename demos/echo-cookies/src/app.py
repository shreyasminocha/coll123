import sqlite3
import html

from flask import Flask, session, request, redirect, flash, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    print(request.cookies, flush=True)
    return f"""<pre>hello</pre>"""


if __name__ == "__main__":
    app.run(port=8000)
