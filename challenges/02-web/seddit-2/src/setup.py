import sqlite3
import random

if __name__ == "__main__":
    db = sqlite3.connect("database.db")
    db.cursor().execute("CREATE TABLE IF NOT EXISTS categories (category TEXT)")
    db.cursor().execute(
        "CREATE TABLE IF NOT EXISTS posts (category TEXT, title TEXT, url TEXT)"
    )
    db.commit()
