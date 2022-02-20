import psycopg2
import base64
import datetime

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
        
#connection.close()

def view_avail():
    print ("** Available **")
    sql = '''SELECT * FROM reservations'''
    cursor.execute(sql) 
    rows = cursor.fetchall()

    for row in rows:
        for col in row:
            print(col, end=' ')
        print()
    

def reserve():
    sql = '''
            INSERT INTO reservations(roomnumber, buildingname, starttime, endtime)
            VALUES(110, 'Spark', '03:00:00', '06:00:00')
        '''


    startTime = ''
    dateDay = 19 # This will all be in one variable
    dateMonth = 2
    dateYear = 2022
    weekDay = datetime.date(dateYear, dateDay, dateMonth).weekday()
    buildingName = ''
    buildingHoursSQL = '''
            SELECT buildingname as buildingName FROM building_hours
        '''
    cursor.execute(buildingHoursSQL)
    buildingHours = cursor.fetchall()
    buildingWeekOpen = buildingHours[0][1] # hardcoded based off of the table design
    buildingWeekClose = buildingHours[0][2]
    buildingWeekendOpen = buildingHours[0][3]
    buildingWeekendClose = buildingHours[0][4]

    # check the building_hours table to see if the room is open
    if weekDay <= 4: # week day (0 = day 1)
        if startTime >= buildingWeekOpen and startTime <= buildingWeekClose:
            try:
                cursor.execute(sql)
            except psycopg2.IntegrityError as e:
                print("** An error has occurred! (Are you sure you entered the right room number?) **") 
        else:
            print("** This building is be closed during your reservation time! **")
    
    
   


def edit_reserve():
    pass

def cancel_reserve():
    pass

prototype_ui()
    