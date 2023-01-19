import html
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return f"""
        <p>Sign up for my mailing list!</p>
        <p>Please use a rice.edu email address!!! Actually, if you're able to sign up with a non-rice domain, I'll give you a flag. How about that?</p>

        <form method="POST" action="/flag">
            <input name="email" value="foo@rice.edu" type="email" pattern="^[^@\.]+@rice\.edu$">
            <input type="submit" value="Sign me up!">
        </form>
    """


@app.route("/flag", methods=["POST"])
def flag():
    email = request.form.get("email", "foo@rice.edu")
    user, host = email.split("@")

    if host == "rice.edu":
        return """
            You must register with a non-rice email to get the flag! Surely the validation I implemented on the frontend is good enough to prevent that, r-right?
        """

    return open("flag.txt").read()
