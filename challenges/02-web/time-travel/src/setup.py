import sqlite3
import random


if __name__ == "__main__":
    db = sqlite3.connect("database.db")
    db.cursor().execute(
        "CREATE TABLE IF NOT EXISTS submissions (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, college TEXT, fav_month TEXT, timestamp INTEGER)"
    )
    db.commit()
