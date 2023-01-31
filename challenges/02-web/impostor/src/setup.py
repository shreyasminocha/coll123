from secret import flag
import sqlite3
import random


if __name__ == "__main__":
    db = sqlite3.connect("database.db")
    db.cursor().execute(
        "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
    )
    db.cursor().execute(
        "INSERT INTO users VALUES (?, ?)", ("admin", random.randbytes(16).hex())
    )
    db.commit()
