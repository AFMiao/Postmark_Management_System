import sqlite3
from datetime import datetime

def initiate(con, cur):
    isInitiated = cur.execute("SELECT name FROM sqlite_master WHERE name='PMS'")
    if isInitiated.fetchone() is None:
        con.execute("""CREATE TABLE PMS(
            ID TEXT PRIMARY KEY NOT NULL,
            OFFICE_NAME TEXT NOT NULL,
            POST_NUMBER TEXT NOT NULL,
            SEND_DATE DATE NOT NULL,
            RECEIVE_DATE DATE DEFAULT NULL,
            PROVINCE TEXT NOT NULL,
            CITY TEXT NOT NULL,
            DISTRICT TEXT NOT NULL,
            ADDRESS TEXT NOT NULL,
            REG_NUMBER1 TEXT DEFAULT NULL,
            REG_NUMBER2 TEXT DEFAULT NULL,
            POSTMARK TEXT DEFAULT NULL)
        """)
        con.commit()

def main_menu():
    print("Welcome to Postmark Management System!\n===================================")
    print("Option: 1. Send  2. Receive  3. Show All  0. Exit")
    ret = input("Enter: ")
    print("")
    return int(ret)

def check_post_number():
    post_number = int(input("Enter post number: "))
    while post_number < 100000 or post_number > 999999:
        post_number = input("Enter post number: ")
    return post_number

def add_postmark(str, num = 1):
    if str == "quit":
        return ""
    return str + ";" + add_postmark(input(f"Enter postmark {num + 1}: "), num + 1)

def send(con, cur):
    print("SENDING LETTER\n==============")

    id = input("Enter id: ")
    
    office_name = input("Enter office name: ")
    
    post_number = input("Enter post number: ")
    
    send_date = input("Enter send date(YYYY-mm-dd): ")
    
    receive_date = input("Enter receive date(YYYY-mm-dd): ")
    if receive_date == "now":
        receive_date = datetime.now().strftime("%Y-%m-%d")
    elif receive_date == "withdrawn":
        receive_date = "9999-12-31"
    
    province = input("Enter province: ")

    if isMunicipality(province):
        city = province
        print("Enter city: ", city)
    else:
        city = input("Enter city: ")
    
    district = input("Enter district: ")
    
    address = input("Enter address: ")
    
    reg_flag1 = input("Is the letter a registered one? (y/n): ")
    reg_number1 = ""
    if reg_flag1 == 'y':
        reg_number1 = input("Enter registered number: ")
    
    reg_flag2 = input("Is the receive a registered one? (y/n): ")
    reg_number2 = ""
    if reg_flag2 == 'y':
        reg_number2 = input("Enter registered number: ")
    
    postmarks = add_postmark(input("Enter postmark 1: "))
    
    data = [id, office_name, post_number, send_date, receive_date, province, city, district, address, reg_number1, reg_number2, postmarks]

    cur.execute("INSERT INTO PMS (ID, OFFICE_NAME, POST_NUMBER, SEND_DATE, RECEIVE_DATE, PROVINCE, CITY, DISTRICT, ADDRESS, REG_NUMBER1, REG_NUMBER2, POSTMARK) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

    print("\nTable updated!")
    ret = int(input("Continue? (1/0): "))
    print("")

    return ret
        
municipalities = ("北京市", "天津市", "上海市", "重庆市")

def isMunicipality(province):
    return province in municipalities

def receive(con, cur):
    id = input("Enter letter id: ")
    res = cur.execute("SELECT OFFICE_NAME FROM PMS WHERE ID=?", (id,))

    if res.fetchone() is None:
        print(f"Letter No.{id} not found.")
        ret = int(input("Continue? (1/0): "))
        print("")
        if ret == 1:
            ret = 2
        return ret
    else:
        receive_date = input("Enter receive date (YYYY-mm-dd)\n(enter \"now\" to insert today's date): ")
        if receive_date == "now":
            receive_date = datetime.now().strftime('%Y-%m-%d')
        elif receive_date == "withdrawn":
            receive_date = "9999-12-31"

        cur.execute("UPDATE PMS SET RECEIVE_DATE = ? WHERE ID=?", (receive_date, id))

        con.commit()
    
    print("Receive date updated.")
    ret = int(input("Continue? (1/0): "))
    if ret == 1:
        ret = 2
    print("")

    return ret

def show_all(con, cur):
    for row in cur.execute("SELECT * FROM PMS ORDER BY ID ASC"):
        print(row)
    
    print("That's all!")
    ret = int(input("What to do next? (1. Send / 2. Receive / 0. Quit): "))
    print("")

    return ret


if __name__ == "__main__":
    con = sqlite3.connect("Postmark.db")
    cur = con.cursor()

    initiate(con, cur)
    
    key = main_menu()
    while True:
        match key:
            case 0:
                break
            case 1:
                key = send(con, cur)
            case 2:
                key = receive(con, cur)
            case 3:
                key = show_all(con, cur)
            case _:
                continue

    cur.close()
    con.close()