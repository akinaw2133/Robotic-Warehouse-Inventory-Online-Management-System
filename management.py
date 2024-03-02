from PyQt4 import QtCore, QtGui
import sys
from db import *
import hamster_threads
from calltable import *
import be_hamster2
import Queue
import threading
import finalMain
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.row = 0

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(729, 589)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 731, 591))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(470, 520, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 520, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(150, 130, 421, 281))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(8)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 90, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(50, 50, 101, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(210, 50, 69, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(70, 440, 61, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(280, 440, 45, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(470, 440, 51, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(130, 430, 104, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 430, 104, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(self.tab)
        self.textEdit_3.setGeometry(QtCore.QRect(530, 430, 104, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(590, 90, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 90, 81, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Product Name", None))
        self.label_2.setText(_translate("Form", "Product Quantity", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "7", None))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "8", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Product Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Product Quantity", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Price", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Item Total Price", None))
        self.pushButton_3.setText(_translate("Form", "Add", None))
        self.comboBox.setItemText(0, _translate("Form", "Soap", None))
        self.comboBox.setItemText(1, _translate("Form", "Shampoo", None))
        self.comboBox.setItemText(2, _translate("Form", "Lotion", None))
        self.comboBox.setItemText(3, _translate("Form", "Detergent", None))
        self.comboBox.setItemText(4, _translate("Form", "Fruits", None))
        self.comboBox.setItemText(5, _translate("Form", "Vegetables", None))
        self.comboBox.setItemText(6, _translate("Form", "Cereals", None))
        self.comboBox.setItemText(7, _translate("Form", "Sauces", None))
        self.comboBox.setItemText(8, _translate("Form", "Toiletries", None))
        self.comboBox.setItemText(9, _translate("Form", "Household", None))
        self.comboBox.setItemText(10, _translate("Form", "Breads", None))
        self.comboBox.setItemText(11, _translate("Form", "FrozenFood", None))
        self.comboBox.setItemText(12, _translate("Form", "Pasta", None))
        self.comboBox.setItemText(13, _translate("Form", "Rice", None))
        self.comboBox.setItemText(14, _translate("Form", "Snacks", None))
        self.comboBox.setItemText(15, _translate("Form", "BabyItems", None))
        self.comboBox.setItemText(16, _translate("Form", "CannedGoods", None))
        self.comboBox.setItemText(17, _translate("Form", "PetItems", None))
        self.comboBox.setItemText(18, _translate("Form", "Electronics", None))
        self.comboBox.setItemText(19, _translate("Form", "Computers", None))
        self.comboBox.setItemText(20, _translate("Form", "Tablets", None))
        self.comboBox.setItemText(21, _translate("Form", "DVD", None))
        self.comboBox.setItemText(22, _translate("Form", "Entertainment", None))
        self.comboBox.setItemText(23, _translate("Form", "GiftCards", None))
        self.comboBox.setItemText(24, _translate("Form", "Beauty", None))
        self.comboBox.setItemText(25, _translate("Form", "Jewelry", None))
        self.comboBox.setItemText(26, _translate("Form", "Watches", None))
        self.comboBox.setItemText(27, _translate("Form", "Books", None))
        self.comboBox.setItemText(28, _translate("Form", "Clothes", None))
        self.comboBox.setItemText(29, _translate("Form", "Jeans", None))
        self.comboBox.setItemText(30, _translate("Form", "Chocolates", None))
        self.comboBox.setItemText(31, _translate("Form", "Juices", None))
        self.comboBox.setItemText(32, _translate("Form", "Phones", None))
        self.comboBox.setItemText(33, _translate("Form", "Cameras", None))
        self.comboBox.setItemText(34, _translate("Form", "SunGlasses", None))
        self.comboBox.setItemText(35, _translate("Form", "Bracelets", None))
        self.comboBox.setItemText(36, _translate("Form", "HandBags", None))
        self.comboBox.setItemText(37, _translate("Form", "Shoes", None))
        self.comboBox_2.setItemText(0, _translate("Form", "1", None))
        self.comboBox_2.setItemText(1, _translate("Form", "2", None))
        self.comboBox_2.setItemText(2, _translate("Form", "3", None))
        self.comboBox_2.setItemText(3, _translate("Form", "4", None))
        self.comboBox_2.setItemText(4, _translate("Form", "5", None))
        self.comboBox_2.setItemText(5, _translate("Form", "6", None))
        self.comboBox_2.setItemText(6, _translate("Form", "7", None))
        self.comboBox_2.setItemText(7, _translate("Form", "8", None))
        self.comboBox_2.setItemText(8, _translate("Form", "9", None))
        self.comboBox_2.setItemText(9, _translate("Form", "10", None))
        self.label_3.setText(_translate("Form", "Gross Price", None))
        self.label_4.setText(_translate("Form", "VAT 15%", None))
        self.label_5.setText(_translate("Form", "Total Price", None))
        self.pushButton_4.setText(_translate("Form", "Remove", None))
        self.pushButton_5.setText(_translate("Form", "Clear All", None))
        self.pushButton_6.setText(_translate("Form", "Print Receipt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Order Items", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Admins Tab", None))

        self.pushButton.clicked.connect(self.collectData)
        self.pushButton_3.clicked.connect(self.addcontent)
        #for clear all button
        self.pushButton_5.clicked.connect(self.clearTable)
        #for print receipt button
        self.pushButton_6.clicked.connect(self.printPrices)
        #for remove button
        self.pushButton_4.clicked.connect(self.removeItem)
        #for cancel button
        self.pushButton_2.clicked.connect(self.closeApplication)

    def collectData(self):
        #global event_queue
        for i in range(0,8):
            for j in range(0,2):
                if((self.tableWidget.item(i,j) != None) and (self.tableWidget.item(i,j).text() != '')):
                    if(j == 0):
                        chosenIt = self.tableWidget.item(i,j).text()
                    else:
                        chosenQua = self.tableWidget.item(i,j).text()
                j+=1
            if((self.tableWidget.item(i,0) != None) and (self.tableWidget.item(i,0).text() != '')):
                print chosenIt, chosenQua
                mydb = Database()
                mydb.updateT(int(chosenQua), chosenIt)
                mydb3 = Database()
                shfNum = mydb3.selectShf(chosenIt)
                print('shfNum:', shfNum)
                finalMain.putItem(shfNum)
                #time.sleep(1)
                print('Queue empty: ', finalMain.getSize())
            i+=1
        print 'out'
        behavior_thread3 = threading.Thread(target=hamster_threads.main)
        behavior_thread3.daemon = True
        behavior_thread3.start()
        #behavior_thread3.join()
        #hamster_threads.main()
        #shfNum=self.comboBox.currentIndex()+1
        #self.orderRobot(shfNum)
    def removeItem(self):
        data=[]
        data.append(('', '', '', ''))
        #global row
        self.row-=1
        for tup in data:
            col=0
            for item in tup:
                anitem=QtGui.QTableWidgetItem(item)
                #print(anitem)
                self.tableWidget.setItem(self.row,col, anitem)
                col+=1
            #row+=1
            self.tableWidget.show() 
    def printPrices(self):
        grossPriceValue = 0
        VATvalue = 0
        totalPriceValue = 0
        for i in range(0,8):
            if((self.tableWidget.item(i,3) != None) and (self.tableWidget.item(i,3).text() != '')):
                itemPriceValue = int(self.tableWidget.item(i,3).text())
                grossPriceValue += itemPriceValue
            i+=1
        VATvalue = 0.15 * grossPriceValue
        totalPriceValue = grossPriceValue + VATvalue
        self.textEdit.setText(str(grossPriceValue)+' Birr')
        self.textEdit_2.setText(str(VATvalue)+' Birr')
        self.textEdit_3.setText(str(totalPriceValue)+' Birr')
    def clearTable(self):
        data=[]
        data.append(('', '', '', ''))
        #global row
        #row-=1
        for i in range(0, self.row+1):
            for tup in data:
                col=0
                for item in tup:
                    anitem=QtGui.QTableWidgetItem(item)
                    #print(anitem)
                    self.tableWidget.setItem(i,col, anitem)
                    col+=1
                #row+=1
                self.tableWidget.show()
        self.row = 0
        #pass
    def closeApplication(self):
        sys.exit(app.exec_())

    def addCcontent(self):
        chosenItem = self.comboBox.itemText(self.comboBox.currentIndex())
        chosenQuantity = self.comboBox_2.itemText(self.comboBox_2.currentIndex())
        anitem=QtGui.QTableWidgetItem(chosenItem)
        self.tableWidget.setItem(0,0, anitem)
        #QtGui.QTableWidgetItem(chosenQuantity)
        #mydb = Database()
        #mydb.updateT(int(chosenQua), chosenIt)
    def addcontent(self):
        #global row
        chosenItem = self.comboBox.itemText(self.comboBox.currentIndex())
        chosenQuantity = self.comboBox_2.itemText(self.comboBox_2.currentIndex())
        mydb2 = Database()
        priceValue = mydb2.selectT(chosenItem)
        #print(priceValue)
        totalPrice = priceValue*int(chosenQuantity)
        data=[]
        data.append((chosenItem, chosenQuantity,str(priceValue),str(totalPrice)))
        for tup in data:
            col=0
            #print(len(tup))
            for item in tup:
                anitem=QtGui.QTableWidgetItem(item)
                #print(anitem)
                self.tableWidget.setItem(self.row,col, anitem)
                col+=1
            self.row+=1
            self.tableWidget.show()
        #print('done adding and')
    #if __name__ == "__main__":
   
def main(argv=None):
    #import sys
    global shfNum#,row
    #global event_queue
    #event_queue = Queue.Queue()
    #row = 0
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    #myQueue = ui.event_queue
    sys.exit(app.exec_())
