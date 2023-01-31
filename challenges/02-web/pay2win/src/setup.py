from secret import flag
import sqlite3
import random


if __name__ == "__main__":
    db = sqlite3.connect("database.db")
    db.cursor().execute(
        "CREATE TABLE IF NOT EXISTS users (username TEXT, name TEXT, password TEXT, type TEXT)"
    )
    db.commit()
