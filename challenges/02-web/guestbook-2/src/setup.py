import sqlite3
import random

if __name__ == "__main__":
    db = sqlite3.connect("database.db")
    db.cursor().execute("CREATE TABLE IF NOT EXISTS users (user TEXT)")
    db.cursor().execute("CREATE TABLE IF NOT EXISTS posts (user TEXT, text TEXT)")
    db.commit()
