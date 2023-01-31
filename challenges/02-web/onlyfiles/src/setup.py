import sqlite3
import random


if __name__ == "__main__":
    db = sqlite3.connect("database.db")
    db.cursor().execute(
        "CREATE TABLE IF NOT EXISTS files (name TEXT, path TEXT, access TEXT)"
    )

    data = [
        ("[redacted]", "[redacted]", "free"),
        ("[redacted]", "[redacted]", "free"),
        ("[redacted]", "[redacted]", "free"),
        ("flag", "[redacted]", "premium"),
        ("[redacted]", "[redacted]", "premium"),
    ]
    db.cursor().executemany("INSERT INTO files VALUES(?, ?, ?)", data)

    db.commit()
