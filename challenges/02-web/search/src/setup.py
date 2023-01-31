from secret import flag
import sqlite3


if __name__ == "__main__":
    db = sqlite3.connect("database.db")
    db.cursor().execute("CREATE TABLE data (content TEXT)")
    db.cursor().execute("INSERT INTO data VALUES (?)", (flag,))
    db.commit()
