import sqlite3


try:
    #Task 1: Create a New SQLite Database
    with sqlite3.connect("../db/magazines.db") as conn:
        #Turn on the foreign key restraint
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        print("Database is connected.")
except sqlite3.Error as e:
    print(f"Database was not made successfully: {e}")
