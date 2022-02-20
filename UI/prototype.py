import psycopg2
import base64

decMessage = base64.b64decode("ZG9nczJjYXRzMA==").decode("utf-8")

connection = psycopg2.connect(
    host = "localhost",
    database = "cubhubs",
    user = "postgres",
    password = decMessage
)
cursor = connection.cursor()

def prototype_ui():
    userInput = 0
    while int(userInput) < 5:
        print("**** CubHubs ****")
        print("1. View Availability")
        print("2. Reserve a Room")
        print("3. Edit Reservation")
        print("4. Cancel Reservation")
        print("5. Quit")
        userInput = int(input())
        print(userInput)
        # because who likes switch statements right
        if userInput == 1:
            view_avail()
        if userInput == 2:
            reserve()
        if userInput == 3:
            edit_reserve()
        if userInput == 4:
            cancel_reserve()
        
connection.close()

def view_avail():
    sql = '''SELECT * FROM room'''
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        for col in row:
            print(col, end=' ')
        print()
    

def reserve():
    pass

def edit_reserve():
    pass

def cancel_reserve():
    pass

prototype_ui()
    