import html
from flask import Flask, request

app = Flask(__name__)

available_files = ["hello.txt", "hmm.txt"]


@app.route("/")
def index():
    return f"""
        <link rel="stylesheet" href="https://minimalcss.jwestman.net/minimal.min.css">

        <p>Available Files:</p>

        <ul>
            {chr(10).join([f"<li><code>{file}</code></li>" for file in available_files])}
        </ul>

        <form method="POST" action="/view">
            <input name='path' value='hello.txt'>
            <input type='submit'>
        </form>
    """


@app.route("/view", methods=["POST"])
def view():
    path = request.form.get("path", "hello.txt").strip()

    try:
        contents = open(f"files/{path}").read()
    except FileNotFoundError:
        return "<pre>no such file!</pre>"

    return f"<pre>{html.escape(contents)}</pre>"
