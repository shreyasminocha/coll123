---
marp: true
theme: leet
---

# web

- web overview
- web security overview
- arbitrary code execution
<!-- - server-side request forgery -->
- sqli
- xss

---

## web overview

---

### http

---

### devtools

useful tabs:

- network
- storage ('application → storage' on chromium)
- …

---

> every* request can be replicated

right-click on a request in the network tab and choose 'copy value' ('copy' on chromium)

---

### methods

- `GET`
- `POST`
- …

---

### headers

---

### storage

- cookies
- `localStorage`
- indexed db

---

### making requests

#### with [`requests`](https://requests.readthedocs.io/en/latest/)

```py
import requests

response = requests.get('https://example.com')
print(response.text)
```

#### with [`curl`](https://curl.haxx.se/)

```sh
curl https://example.com
```

#### with [`httpie`](https://httpie.org/)

```sh
httpie https://example.com
```

---

```py
# headers
requests.get('https://example.com', headers={'foo': 'bar'})

# cookies
requests.get('https://example.com', cookies={'foo': 'bar'})

# form data
requests.post('https://example.com/form', data={'username': 'jj'})

# json
requests.post('https://example.com/api/data', json={'foo': 'bar'})
```

---

```sh
# headers
httpie get https://example.com/foo 'Key: Value'

# form data
httpie -f post https://example.com/foo key=value foo=bar

# json
httpie post https://example.com/foo key=value foo=bar
```

---

### building web applications

components*:

- backend
  - routes
  - api + database
- frontend
  - templates
  - assets
  - …
---

### flask

```py
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "<pre>Hello World!</pre>"

@app.route("/echo", methods=["GET", "POST"])
def echo():
    if request.method == "POST":
        return request.form["text"]

    return "<pre>/echo</pre>"

app.run(8000)
```


---

### web challenges in ctfs

---

> Frontend validation and data *can* and *will* be messed with

---

### sessions

```py
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return "<p>foo</p>"

    if request.method == "POST":
        session.clear()

        # ...
        user = res.fetchone()
        if not user or not bcrypt.verify(password, user[1]):
            flash("Invalid username/password", "danger")
            return redirect("/login")

        session["username"] = user[0]
        # ...
```

Example: `eyJ1c2VybmFtZSI6ImV4YW1wbGUifQ.Y8iUww.i9WJ-kOy1jYKkeb6pRypf6VUWec`

---

### `eval` and cousins

EVAL BAD!!!!11

- watch out when evaluating expressions or running commands that users may be able to control
- python payload for reading a file: `open('./file.txt').read()`
- reading files from a shell: `cat ./file.txt`

---

### files

- beware when letting users control paths
- beware when letting users upload files
- symbolic links

kid named `../secret/do/not/enter`: 👀

---

```py
path = 'foo' # user-controlled
open(f'/tmp/{path}').read()

path = '../etc/passwd'
open(f'/tmp/{path}').read()
```

---

## sql

note: this course will almost exclusively use sqlite through python's [`sqlite3`](https://docs.python.org/3/library/sqlite3.html) module

---

```sql
create table users (username text primary key, password text);
insert into users values ('admin', 'password');
```

note: never store passwords as plaintext lol

---

```sql
select * from users;
select * from users where username='admin';
select * from users where username='admin' and password='password';
select username from users where username='admin' and password='password';
```

---

```sql
delete from users where username='admin';
```

```sql
drop table users;
```

---

### sql injection 💉

---

BAD!

```py
# user-controlled, of course
username = ...
password = ...

result = db.cursor().execute(
    f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
)
```

<!-- this is a common pattern: 'string interpolation' is risky. -->

---

Good :)

```py
username = ...
password = ...

result = db.cursor().execute(
    "SELECT * FROM users WHERE username=? AND password=?", (username, password)
)
```

---

### sql injection patterns

```py
username = "admin"
password = "invalid' or 1=1 --"

result = db.cursor().execute(
    f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
)
```

note: `AND` has higher precedence than `OR` (thanks Ian!)

---

```py
username = "joe"
password = "invalid' or role='superuser' --"

result = db.cursor().execute(
    f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
)
```

---

```py
new_name = "Foo Bar', grade='A-"

db.cursor.execute(f"UPDATE students SET name='{new_name}' WHERE netid='ab123'")
db.commit()
```

---

list tables:

```sql
select * from sqlite_master where type='table';
```

---

## js

---

## xss
