import sqlite3
import datetime

def initiate(con):
    isInitiated = con.execute("SELECT name FROM sqlite_master WHERE name='PMS'")
    if isInitiated.fetchone() is None:
        con.execute("""CREATE TABLE PMS(
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

def enter_date(date):
    time = datetime.datetime.strptime(date, '%Y-%m-%d')
    return (datetime.date(time.year, time.month, time.day), )

def send(con):
    print("SENDING LETTER\n==============")

    id = input("Enter id: ")
    
    office_name = input("Enter office name: ")
    
    post_number = check_post_number()
    
    send_date = enter_date(input("Enter send date(YYYY-mm-dd): "))
    
    receive_date = enter_date(input("Enter receive date(YYYY-mm-dd): "))
    
    province = input("Enter province: ")
    city = input("Enter city: ")
    district = input("Enter district")
    address = input("Enter address: ")
    
    reg_flag1 = input("Is the letter a registered one? (y/n): ")
    reg_number1 = ""
    if reg_flag1 == 'y':
        reg_number1 = input("Enter registered number: ")
    
    reg_flag2 = input("Is the receive a registered one? (y/n): ")
    reg_number2 = ""
    if reg_flag2 == 'y':
        reg_number2 = input("Enter registered number: ")
    
    data = [
        (id, office_name, post_number, send_date, receive_date, province, city, district, address, reg_number1, reg_number2),
    ]

    con.execute("INSERT INTO PMS VALUES(?)", data)
        

def receive(con, cur):
    pass

def show_all(con, cur):
    pass

if __name__ == "__main__":
    con = sqlite3.connect("Postmark.db")

    initiate(con)
    
    key = main_menu()
    while True:
        match key:
            case 1:
                send(con)
            case 2:
                receive(con)
            case 3:
                show_all(con)
            case _:
                key = main_menu()
                continue