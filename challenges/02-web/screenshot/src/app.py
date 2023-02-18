import random
import html
import uuid

from flask import Flask, request
from playwright.sync_api import sync_playwright

from secret import flag

app = Flask(__name__)


@app.route("/")
def index():
    return """
        <form action="/get" method="GET">
            <input type="text" name="url" placeholder="https://example.com" />
            <input type="submit" value="📸" />
        </form>
    """


@app.route("/get", methods=["GET"])
def make_request():
    url = request.args.get("url", "https://example.com")
    filename = str(uuid.uuid4())

    with sync_playwright() as p:
        browser = p.chromium.launch()
        browser_context = browser.new_context()
        browser_context.add_cookies(
            [
                {
                    "name": "flag",
                    "value": flag,
                    "url": url,
                }
            ]
        )

        page = browser_context.new_page()
        page.goto(url)
        try:
            page.screenshot(path=f"./static/files/{filename}.png")
            return f"<a href='/static/files/{filename}.png'>screenshot</a>"
        except:
            return "<p>something went wrong</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=False)
