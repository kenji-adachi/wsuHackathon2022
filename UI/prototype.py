import psycopg2
import base64
import datetime
import time
from datetime import datetime as dt
decMessage = base64.b64decode("ZG9nczJjYXRzMA==").decode("utf-8")

connection = psycopg2.connect(
    host = "localhost",
    database = "cubhubs",
    user = "postgres",
    password = decMessage
)
cursor = connection.cursor()

roomStateTags = ["Public", "Private"]
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
        print("Room Number: " + row[0] + " Building Name: " + row[1] + " Room State: " + str(row[2]) + " Start Time: " + str(row[3]) + " End Time: " + str(row[4]) )


def reserve(buildingName, roomNumber, startDate, endDate, roomState):
    endDate = dt.strptime(endDate, '%Y-%m-%d %H:%M:%S')
    startDate = dt.strptime(startDate, '%Y-%m-%d %H:%M:%S')
    #buildingName = 'Spark'
    #roomNumber = '110'
    #startDate = datetime.datetime(2022, 2, 17, 8, 0, 0) # 2/20/2022 08:00:00
    #endDate = datetime.datetime(2022, 2, 17, 9, 0, 0) # 2/20/2022 09:00:00
    #print(startDate)
    startWeekDay = datetime.date(startDate.year, startDate.month, startDate.day).weekday()
    endWeekDay = datetime.date(endDate.year, endDate.month, endDate.day).weekday()

    availableSQL = "SELECT * FROM reservations WHERE roomnumber = '" + roomNumber + "' AND buildingname = '" + buildingName + "'"  
    cursor.execute(availableSQL)  
    if cursor.rowcount != 0:
        # convert start and end time to datetime variables
        availableSQLData = cursor.fetchall()
        originEndTime = availableSQLData[0][4]
        #originEndTime = originEndTime[:-2]
        originEndTime = dt.strptime(originEndTime, '%Y-%m-%d %H:%M:%S')
        originStartTime = availableSQLData[0][3]
        #originStartTime = originStartTime[:-2]
        originStartTime = dt.strptime(originStartTime, '%Y-%m-%d %H:%M:%S')

        if merge_conflict(startDate, endDate, originStartTime, originEndTime):
            errorStr = "This room is reserved!"
            print(errorStr)
            return errorStr
    
    # grab the building hours based off building name
    buildingHoursSQL = "SELECT * FROM building_hours WHERE buildingname ='" + buildingName + "'"
    
    # grab individual building hours
    cursor.execute(buildingHoursSQL)
    buildingHours = cursor.fetchall()
    buildingWeekOpen = buildingHours[0][1] # hardcoded based off of the table design
    buildingWeekClose = buildingHours[0][2]
    buildingWeekendOpen = buildingHours[0][3]
    buildingWeekendClose = buildingHours[0][4]

    reserveSQL = "INSERT INTO reservations(roomnumber, buildingname, starttime, endtime, roomstate) VALUES('" + roomNumber +"'"",'" + buildingName +"','"+ str(startDate) +"' , '" + str(endDate) +"','" + roomState + "')"

    # check the building_hours table to see if the room is open
    if is_building_open(startDate, buildingName) and is_building_open(endDate, buildingName):
        try:
            cursor.execute(reserveSQL)
        except psycopg2.IntegrityError as e:
            print(e)
            errorStr = "** An error has occurred! (Are you sure you entered the right room number?) **"
            print(errorStr)
            return errorStr
    else:
        errorStr = "This building is closed during your reservation time!"
        print(errorStr)
        return errorStr
    connection.commit()
    errorStr = "Successfully Reserved!"
    print(errorStr)
    return errorStr

def  merge_conflict(startDate, endDate, originStartTime, originEndTime):
    if ((startDate >= originStartTime and startDate <= originEndTime) # yes we could negate and save many lines of code, however I've been up for more than 24 hours
     or (endDate >= originStartTime and endDate <= originEndTime) # LMAO
     or (originStartTime >= startDate and originStartTime <= endDate)
     or (originEndTime >= startDate and originEndTime <= endDate)):
        return True
    return False

def is_building_open(date, buildingName):
    weekDay = datetime.date(date.year, date.month, date.day).weekday()
    timeSlot = datetime.time(date.hour, date.minute, date.second)
    # grab the building hours based off building name
    buildingHoursSQL = "SELECT * FROM building_hours WHERE buildingname ='" + buildingName + "'"
    
    # grab individual building hours
    cursor.execute(buildingHoursSQL)
    buildingHours = cursor.fetchall()
    buildingWeekOpen = buildingHours[0][1] # hardcoded based off of the table design
    buildingWeekClose = buildingHours[0][2]
    buildingWeekendOpen = buildingHours[0][3]
    buildingWeekendClose = buildingHours[0][4]

    if weekDay <= 4:  # week day (0 = day 1)
        if timeSlot >= buildingWeekOpen and timeSlot <= buildingWeekClose:
            return True
        else:
            return False
    else: # ensure further error checking if project is to be continued past hackathon 
        if timeSlot >= buildingWeekendOpen and timeSlot <= buildingWeekendClose:
            return True
        else:
            return False

def edit_reserve():
    pass

def cancel_reserve(roomNumber, buildingName, startDate):
    startDate = dt.strptime(startDate, '%Y-%m-%d %H:%M:%S')
    deleteSQL = "DELETE FROM reservations WHERE roomnumber = '" + roomNumber + "' AND buildingname = '" + buildingName + "' AND starttime = '" + str(startDate) + "'"
    cursor.execute(deleteSQL)
    connection.commit()

