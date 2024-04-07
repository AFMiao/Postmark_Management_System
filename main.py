import sqlite3
import datetime

def initiate(con, cur):
    isInitiated = cur.execute("SELECT name FROM sqlite_master WHERE name='PMS'")
    if isInitiated.fetchone() is None:
        cur.execute("""CREATE TABLE PMS(
            ID TEXT PRIMARY KEY NOT NULL,
            OFFICE_NAME TEXT NOT NULL,
            POST_NUMBER INT CHECK(POST_NUMBER >= 100000 AND POST_NUMBER < 1000000),
            SEND_DATE DATE NOT NULL,
            RECEIVE_DATE DATE NOT NULL,
            PROVINCE TEXT NOT NULL,
            CITY TEXT NOT NULL,
            DISTRICT TEXT NOT NULL,
            ADDRESS TEXT NOT NULL,
            REG_NUMBER1 TEXT DEFAULT NULL,
            REG_NUMBER2 TEXT DEFAULT NULL)
        """)
        con.commit()


if __name__ == "__main__":
    con = sqlite3.connect("Postmark.db")
    cur = con.cursor()

    initiate(con, cur)
    