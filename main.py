import sqlite3

if __name__ == "__main__":
    con = sqlite3.connect("Postmark.db")
    cur = con.cursor()