import sqlite3
import datetime

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
            REG_NUMBER2 TEXT DEFAULT NULL)
        """)
        con.commit()

def main_menu():
    print("Welcome to Postmark Management System!\n===================================")
    print("Option: 1. Send  2. Receive  3. Show All  0. Exit")
    ret = input("Enter: ")
    print("\n")
    return int(ret)

def check_post_number():
    post_number = int(input("Enter post number: "))
    while post_number < 100000 or post_number > 999999:
        post_number = input("Enter post number: ")
    return post_number

def enter_date(date):
    time = datetime.datetime.strptime(date, '%Y-%m-%d')
    return (datetime.date(time.year, time.month, time.day), )

def send(con, cur):
    print("SENDING LETTER\n==============")

    id = input("Enter id: ")
    
    office_name = input("Enter office name: ")
    
    post_number = input("Enter post number: ")
    
    send_date = input("Enter send date(YYYY-mm-dd): ")
    
    receive_date = input("Enter receive date(YYYY-mm-dd): ")
    
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
    
    data = [id, office_name, post_number, send_date, receive_date, province, city, district, address, reg_number1, reg_number2]

    cur.execute("INSERT INTO PMS (ID, OFFICE_NAME, POST_NUMBER, SEND_DATE, RECEIVE_DATE, PROVINCE, CITY, DISTRICT, ADDRESS, REG_NUMBER1, REG_NUMBER2) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

    print("Table updated!\n")

    return int(input("Continue? (y/n): "))
        
municipalities = ("北京市", "天津市", "上海市", "重庆市")

def isMunicipality(province):
    return province in municipalities

def receive(con, cur):
    pass

def show_all(con, cur):
    pass


if __name__ == "__main__":
    con = sqlite3.connect("Postmark.db")
    cur = con.cursor()

    initiate(con, cur)
    
    while True:
        key = main_menu()
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