import sys

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import base64
import psycopg2
import prototype

qtCreatorFile = "UI\cubhubs.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class cubhubs(QMainWindow):
    def __init__(self):
        super(cubhubs, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadTableType()
        self.loadOptionsList()
        #self.connectQuery()
        self.ui.tableTypeSelect.currentTextChanged.connect(self.tableTypeSelectionChange)
        self.ui.submitButton.clicked.connect(self.submitReservation)
        self.ui.deleteButton.clicked.connect(self.deleteReservation)
        self.ui.buildingOptions.currentTextChanged.connect(self.buildingSelected)
        self.ui.buildingOptions_2.currentTextChanged.connect(self.buildingSelected_2)

    def loadTableType(self):
        #tables: Buildings, Rooms, BuildingHours, Reservations, Tags
        tableTypes = ["Buildings", "Rooms", "Building Hours", "Reservations", "Tags"]
        for i in range(5):
            self.ui.tableTypeSelect.addItem(tableTypes[i])
        self.ui.tableTypeSelect.setCurrentIndex(-1)
        self.ui.tableTypeSelect.clearEditText()
    
    def loadOptionsList(self):
        #Buildings
        buildingSQL = "SELECT * FROM building"
        prototype.cursor.execute(buildingSQL)
        buildingList = prototype.cursor.fetchall()
        for i in buildingList:
            self.ui.buildingOptions.addItem(i[0])
            self.ui.buildingOptions_2.addItem(i[0])
        self.ui.buildingOptions.setCurrentIndex(-1)
        self.ui.buildingOptions.clearEditText()
        self.ui.buildingOptions_2.setCurrentIndex(-1)
        self.ui.buildingOptions_2.clearEditText()

        #roomState
        self.ui.roomStateOption.addItem('1')
        self.ui.roomStateOption.addItem('2')
        self.ui.roomStateOption.setCurrentIndex(-1)
        self.ui.roomStateOption.clearEditText()
    
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
        prototype.cursor.execute(runTheSQL)
        if prototype.cursor.rowcount != 0:
            theTable = prototype.cursor.fetchall()
            print(theTable)
            self.ui.tableInsertType.setColumnCount(len(theTable[0]))
            self.ui.tableInsertType.setRowCount(len(theTable))
            #self.ui.tableInsertType.resizeColumnToContents()
            curRowCount = 0
            for row in theTable:
                for col in range(0,len(theTable[0])):
                    self.ui.tableInsertType.setItem(curRowCount,col,QTableWidgetItem(str(row[col])))
                curRowCount += 1
    
    def submitReservation(self):
        buildingChoice = self.ui.buildingOptions.currentText()
        roomChoice = self.ui.roomOptions.currentText()
        reserveStart = self.ui.reserveStartTime.text()
        reserveEnd = self.ui.reserveEndTime.text()
        theRoomState = self.ui.roomStateOption.currentText()

        #clear all inputs
        self.ui.buildingOptions.setCurrentIndex(-1)
        self.ui.roomOptions.setCurrentIndex(-1)
        self.ui.reserveStartTime.clear()
        self.ui.reserveEndTime.clear()
        self.ui.roomStateOption.setCurrentIndex(-1)
        #self.ui.tableTypeSelect.setCurrentIndex(-1)
        #show text
        errorStr = prototype.reserve(buildingChoice, roomChoice, reserveStart, reserveEnd, theRoomState)
        #self.ui.label_7.setText(errorStr)

    def deleteReservation(self):
        buildingChoice_2 = self.ui.buildingOptions_2.currentText()
        roomChoice_2 = self.ui.roomOptions_2.currentText()
        reserveStart_2 = self.ui.reserveStartDate.text()

        #clear all inputs
        self.ui.buildingOptions_2.setCurrentIndex(-1)
        self.ui.roomOptions_2.setCurrentIndex(-1)
        self.ui.reserveStartDate.clear()
        prototype.cancel_reserve(roomChoice_2, buildingChoice_2, reserveStart_2)

    def buildingSelected(self):
        #Rooms
        self.ui.roomOptions.clear()
        selectedBuilding = self.ui.buildingOptions.currentText()
        roomSQL = "SELECT distinct roomnumber FROM room WHERE buildingname ='" + selectedBuilding + "'"
        prototype.cursor.execute(roomSQL)
        roomList = prototype.cursor.fetchall()
        for i in roomList:
            self.ui.roomOptions.addItem(i[0])
        self.ui.roomOptions.setCurrentIndex(-1)
        self.ui.roomOptions.clearEditText()

    def buildingSelected_2(self):
        #Rooms
        self.ui.roomOptions_2.clear()
        selectedBuilding_2 = self.ui.buildingOptions_2.currentText()
        roomSQL_2 = "SELECT distinct roomnumber FROM room WHERE buildingname ='" + selectedBuilding_2 + "'"
        prototype.cursor.execute(roomSQL_2)
        roomList_2 = prototype.cursor.fetchall()
        for i in roomList_2:
            self.ui.roomOptions_2.addItem(i[0])
        self.ui.roomOptions_2.setCurrentIndex(-1)
        self.ui.roomOptions_2.clearEditText()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = cubhubs()
    window.show()
    sys.exit(app.exec_())
    




