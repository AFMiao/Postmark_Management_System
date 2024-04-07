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

def main_menu():
    print("Welcome to Postmark Management System!\n===================================")
    print("Option: 1. Send\t2. Receive\t3. Show All")
    return input("Enter:")

def check_post_number():
    post_number = input("Enter post number: ")
    while post_number < 100000 or post_number > 999999:
        post_number = input("Enter post number: ")
    return post_number

def send(con, cur):
    print("SENDING LETTER\n==============")
    id = input("Enter id: ")
    office_name = input("Enter office name: ")
    post_number = check_post_number()

def receive(con, cur):
    pass

def show_all(con, cur):
    pass

if __name__ == "__main__":
    con = sqlite3.connect("Postmark.db")
    cur = con.cursor()

    initiate(con, cur)
    
    key = main_menu()
    while True:
        match key:
            case 1:
                send()
            case 2:
                receive()
            case 3:
                show_all()
            case _:
                key = main_menu()
                continue