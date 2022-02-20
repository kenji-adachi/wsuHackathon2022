import sys

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import base64
import psycopg2

qtCreatorFile = "cubhubs.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

decMessage = base64.b64decode("S2pwb3N0Z3JlMg==").decode("utf-8")

try:
    connection = psycopg2.connect(dbname='cubhubs', user='postgres', host='localhost', password=decMessage)
except:
    print("Error: Could not connect to database")
cursor = connection.cursor()

class cubhubs(QMainWindow):
    def __init__(self):
        super(cubhubs, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadTableType()
        #self.connectQuery()
        self.ui.tableTypeSelect.currentTextChanged.connect(self.tableTypeSelectionChange)

    def connectQuery(self):
        try:
            connection = psycopg2.connect(dbname='cubhubs', user='postgres', host='localhost', password=decMessage)
        except:
            print("Error: Could not connect to database")
        cursor = connection.cursor()

    def loadTableType(self):
        #tables: Buildings, Rooms, BuildingHours, Reservations, Tags
        tableTypes = ["Buildings", "Rooms", "Building Hours", "Reservations", "Tags"]
        for i in range(5):
            self.ui.tableTypeSelect.addItem(tableTypes[i])
        self.ui.tableTypeSelect.setCurrentIndex(-1)
        self.ui.tableTypeSelect.clearEditText()
    
    def tableTypeSelectionChange(self):
        typeSelection = self.ui.tableTypeSelect.currentText()
        if(typeSelection == "Buildings"):
            #load up the Building table
            runTheSQL = "SELECT * FROM building"

        elif(typeSelection == "Rooms"):
            #load up the Room table
            runTheSQL = "SELECT * FROM room"

        elif(typeSelection == "Building Hours"):
            #load up the Building Hours table
            runTheSQL = "SELECT * FROM building_hours"

        elif(typeSelection == "Reservations"):
            #load up the Resrvations table
            runTheSQL = "SELECT * FROM reservations"

        elif(typeSelection == "Tags"):
            #load up the Tags table
            runTheSQL = "SELECT * FROM tags"
        cursor.execute(runTheSQL)
        theTable = cursor.fetchall()
        print(theTable)
        self.ui.tableInsertType.setColumnCount(len(theTable[0]))
        self.ui.tableInsertType.setRowCount(len(theTable))
        #self.ui.tableInsertType.resizeColumnToContents()
        curRowCount = 0
        for row in theTable:
            for col in range(0,len(theTable[0])):
                self.ui.tableInsertType.setItem(curRowCount,col,QTableWidgetItem(str(row[col])))
            curRowCount += 1

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = cubhubs()
    window.show()
    sys.exit(app.exec_())




