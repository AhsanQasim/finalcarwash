import math
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QStyle, \
    QDialog
from PyQt5.QtGui import QIcon
import sqlite3
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
import random
import os
import sys



class Person:
    def __init__(self, fullname, username,password,address,email,telephone):
        self.name = fullname
        self.username = username
        self.password = password
        self.address = address
        self.email = email
        self.telephone = telephone
        self.washcard = random.randint(000000,999999)
        self.accountamount=0
        self.memberType = "regular"
        self.points = 0

    def getusername(self):
        return self.username
    def getpass(self):
        return self.password
    def getwashcard(self):
        return self.washcard
    def getacount(self):
        return self.accountamount


# def product_bought(product_name, product_price, amount_sold, money_earned):
#     my_file = open("records.txt", "r")
#     content = my_file.read()
#     content_list = content.split("\n")
#
#     found = False
#     user_id = ""
#     m = 0
#     for k in content_list:
#         temp_array = k.split("\\")
#
#         if temp_array != "":
#             if ((temp_array[3] == index01)):
#                 user_id = temp_array[3]
#                 found = True
#                 if (int(temp_array[7]) < int(product_price)):
#                     print("Washcard balance less than the selected product price")
#                     break
#                 else:
#                     amount = int(temp_array[7]) - int(product_price)
#                     stringbecome = temp_array[0] + "\\" + temp_array[1] + "\\" + temp_array[2] + "\\" + temp_array[
#                         3] + "\\" + temp_array[4] + "\\" + temp_array[5] + "\\" + temp_array[6] + "\\" + str(amount)
#                     content_list[m] = stringbecome
#                     break
#             else:
#                 m = m + 1
#         else:
#             break
#     if (found):
#         print("Updating Balance")
#         with open("records.txt", "w") as f:
#             for i in range(0, len(content_list) - 1):
#                 f.writelines((content_list[i]))
#                 f.writelines("\n")
#             f.close()
#
#         # Products and prices
#
#         final_content_list = []
#         with open("products &  prices.txt", "r") as my_file:
#             content = my_file.read()
#             content_list = content.split("\n")
#             final_content_list = content_list
#             index_number = -1
#             for i in range(0, len(content_list)):
#
#                 if (content_list[i].split("\\")[0] == product_name):
#                     index_number = i
#                     break
#                 else:
#                     continue
#             if (index_number == -1):
#                 print("Product not found")
#             else:
#                 print("Product present at index : " + str(index_number))
#
#     my_file = open("products &  prices.txt", "r")
#     content = my_file.read()
#     content_list = content.split("\n")
#
#     found = False
#     m = 0
#
#     temp_array = content_list[index_number].split("\\")
#
#     amount_increase = int(amount_sold) + 1
#     profit_increase = int(money_earned) + int(product_price)
#
#     stringbecome = str(temp_array[0]) + "\\" + str(temp_array[1]) + "\\" + str(temp_array[2]) + "\\" + str(
#         amount_increase) + "\\" + str(profit_increase)
#
#     content_list[index_number] = stringbecome
#
#     print("Products and prices updated")
#     with open("products &  prices.txt", "w") as f:
#         for i in range(0, len(content_list) - 1):
#             f.writelines((content_list[i]))
#             f.writelines("\n")
#         f.close()

def product_bought(product_name, product_price, amount_sold, money_earned):
    my_file = open("records.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")

    found = False
    user_id = ""
    m = 0
    for k in content_list:
        temp_array = k.split("\\")

        if temp_array != "":
            if len(temp_array) == 11:
                if ((temp_array[3] == index01)):
                    user_id = temp_array[3]
                    found = True
                    if (int(temp_array[9]) < int(product_price)):
                        print("Washcard balance less than the selected product price")
                        break
                    else:
                        amount = int(temp_array[9]) - int(product_price)
                        new_points = int(temp_array[8]) + int(product_price)
                        if (new_points >= 300 and new_points < 500):
                            stringbecome = temp_array[0] + "\\" + temp_array[1] + "\\" + temp_array[2] + "\\" + \
                                           temp_array[
                                               3] + "\\" + temp_array[4] + "\\" + temp_array[5] + "\\" + temp_array[
                                               6] + "\\" + "silver" + "\\" + str(new_points) + "\\" + str(
                                amount) + "\\" + " "
                            content_list[m] = stringbecome

                        elif (new_points >= 500):
                            stringbecome = temp_array[0] + "\\" + temp_array[1] + "\\" + temp_array[2] + "\\" + \
                                           temp_array[
                                               3] + "\\" + temp_array[4] + "\\" + temp_array[5] + "\\" + temp_array[
                                               6] + "\\" + "gold" + "\\" + str(new_points) + "\\" + str(
                                amount) + "\\" + " "
                            content_list[m] = stringbecome

                        else:

                            stringbecome = temp_array[0] + "\\" + temp_array[1] + "\\" + temp_array[2] + "\\" + \
                                           temp_array[
                                               3] + "\\" + temp_array[4] + "\\" + temp_array[5] + "\\" + temp_array[
                                               6] + "\\" + temp_array[7] + "\\" + temp_array[8] + "\\" + str(
                                amount) + "\\" + " "
                            content_list[m] = stringbecome
                        break
                else:
                    m = m + 1
            else:
                if ((temp_array[3] == index01)):
                    user_id = temp_array[3]
                    found = True
                    if (int(temp_array[7]) < int(product_price)):
                        print("Washcard balance less than the selected product price")
                        break
                    else:
                        amount = int(temp_array[7]) - int(product_price)
                        stringbecome = temp_array[0] + "\\" + temp_array[1] + "\\" + temp_array[2] + "\\" + temp_array[
                            3] + "\\" + temp_array[4] + "\\" + temp_array[5] + "\\" + temp_array[6] + "\\" + str(
                            amount) + "\\" + temp_array[8] + "\\" + temp_array[9]
                        content_list[m] = stringbecome
                        break
                else:
                    m = m + 1

        else:
            break

    if (found):
        print("Updating Balance")
        with open("records.txt", "w") as f:
            for i in range(0, len(content_list) - 1):
                f.writelines((content_list[i]))
                f.writelines("\n")
            f.close()

        # Products and prices

        final_content_list = []
        with open("products &  prices.txt", "r") as my_file:
            content = my_file.read()
            content_list = content.split("\n")
            final_content_list = content_list
            index_number = -1
            for i in range(0, len(content_list)):

                if (content_list[i].split("\\")[0] == product_name):
                    index_number = i
                    break
                else:
                    continue
            if (index_number == -1):
                print("Product not found")
            else:
                print("Product present at index : " + str(index_number))

    my_file = open("products &  prices.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")

    found = False
    m = 0

    temp_array = content_list[index_number].split("\\")

    amount_increase = int(amount_sold) + 1
    profit_increase = int(money_earned) + int(product_price)

    stringbecome = str(temp_array[0]) + "\\" + str(temp_array[1]) + "\\" + str(temp_array[2]) + "\\" + str(
        amount_increase) + "\\" + str(profit_increase)

    content_list[index_number] = stringbecome

    print("Products and prices updated")
    with open("products &  prices.txt", "w") as f:
        for i in range(0, len(content_list) - 1):
            f.writelines((content_list[i]))
            f.writelines("\n")
        f.close()


class PrintProfits(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Daily Profits:')
        self.left = 200
        self.top = 200
        self.width = 300
        self.height = 400
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.printProfits()

    def printProfits(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.backbutton = QPushButton('Back', self)
        self.backbutton.move(170, 0)
        self.backbutton.clicked.connect(self.on_clickback)

        self.signout = QPushButton('Signout', self)
        self.signout.move(0, 0)
        self.signout.clicked.connect(self.on_clicksignout)

        my_file = open("products &  prices.txt", "r")
        content = my_file.read()
        content_list = content.split("\n")
        temp_array1 = content_list[0].split("\\")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Product Name and Product profit")
        self.label.move(30, 30)

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array1[0])
        self.label.move(30, 60)

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array1[4])
        self.label.move(30, 90)

        temp_array2 = content_list[1].split("\\")

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array2[0])
        self.label.move(30, 120)

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array2[4])
        self.label.move(30, 150)

        temp_array3 = content_list[2].split("\\")

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array3[0])
        self.label.move(30, 180)

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array3[4])
        self.label.move(30, 210)

        temp_array4 = content_list[3].split("\\")

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array4[0])
        self.label.move(30, 240)

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array4[4])
        self.label.move(30, 270)

        temp_array5 = content_list[4].split("\\")

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array5[0])
        self.label.move(30, 300)

        self.label = QtWidgets.QLabel(self)
        self.label.setText(temp_array5[4])
        self.label.move(30, 330)

    def on_clickback(self):
        global identity
        if identity == "employee":
            self.cams = EmployeeMain()
            self.cams.show()
            self.close()
        else:
            self.cams = ManagerMain()
            self.cams.show()
            self.close()

    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()


class Employee(Person):
    def __init__(self, fullname, username,password,address,email,telephone,status,empid):
        super().__init__(fullname, username,password,address,email,telephone)
        self.status = status
        self.empid = empid

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'CAR WASH'
        self.left = 200
        self.top = 200
        self.width = 370
        self.height = 400
        self.window()

    def window(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        # ---------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Full Name:")
        self.label.move(40, 20)

        self.ftextbox = QLineEdit(self)
        self.ftextbox.move(40, 50)
        self.ftextbox.resize(90, 25)
        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Name:")
        self.label.move(220, 20)

        self.ltextbox = QLineEdit(self)
        self.ltextbox.move(220, 50)
        self.ltextbox.resize(90, 25)

        # ----------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Password:")
        self.label.move(40, 80)

        self.stextbox = QLineEdit(self)
        self.stextbox.move(40, 110)
        self.stextbox.resize(90, 25)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Address:")
        self.label.move(220, 80)

        self.ctextbox = QLineEdit(self)
        self.ctextbox.move(220, 110)
        self.ctextbox.resize(90, 25)

        # --------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Telephone:")
        self.label.move(40, 140)

        self.sstextbox = QLineEdit(self)
        self.sstextbox.move(40, 170)
        self.sstextbox.resize(90, 25)

        # ----------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Email:")
        self.label.move(220, 140)

        self.etextbox = QLineEdit(self)
        self.etextbox.move(220, 170)
        self.etextbox.resize(90, 25)

        # ------------------

        # ------------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Employee No:")
        self.label.move(220, 200)

        self.ettextbox = QLineEdit(self)
        self.ettextbox.move(220, 230)
        self.ettextbox.resize(90, 25)
        self.ettextbox.setText("N/A")

        # ------------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Status:")
        self.label.move(40, 200)

        self.sttextbox = QLineEdit(self)
        self.sttextbox.move(40, 230)
        self.sttextbox.resize(90, 25)
        self.sttextbox.setText("N/A")

        # Create a button in the window
        self.regbutton = QPushButton('Register', self)
        self.regbutton.move(40, 330)
        # Create a button in the window
        self.signbutton = QPushButton('Sign In', self)
        self.signbutton.move(220, 330)
        self.warlabel = QtWidgets.QLabel(self)
        self.warlabel.setText("")
        self.warlabel.move(120, 360)
        self.warlabel.setGeometry(QtCore.QRect(120, 360, 200, 20))  # (x, y, width, height)
        # connect button to function on_click
        self.regbutton.clicked.connect(self.on_clickreg)
        self.signbutton.clicked.connect(self.on_clicksign)
        self.show()


    @pyqtSlot()
    def on_clickreg(self):
        Fullname = self.ftextbox.text(),
        Username = self.ltextbox.text(),
        Password = self.stextbox.text(),
        Address = self.ctextbox.text(),
        telephone = self.sstextbox.text(),
        email = self.etextbox.text()
        emplno = self.ettextbox.text()
        status = self.sttextbox.text()
        inputvalidity = True

        try:
            s = self.ftextbox.text()
            if not s:
                print("Input must not be empty")
                inputvalidity = False
                self.warlabel.setText("Input Valid name")

            s = self.ltextbox.text()
            if not s:
                print("Input must not be empty")
                inputvalidity = False
                self.warlabel.setText("Input Valid username")

            s = self.stextbox.text()
            if not s:
                print("Input must not be empty")
                inputvalidity = False
                self.warlabel.setText("Input Valid pass")

            elif len(s)<8:
                print("Password must have length 8")
                inputvalidity = False
                self.warlabel.setText("Password must have length 8")

            s = self.ctextbox.text()
            if not s:
                print("Input must not be empty")
                inputvalidity = False
                self.warlabel.setText("Input Valid address")

            s = self.sstextbox.text()
            if not s:
                print("Input must not be empty")
                inputvalidity = False
                self.warlabel.setText("Input Valid telephone")

            elif len(s)<11:
                print("telephone must have length 8")
                inputvalidity = False
                self.warlabel.setText("telephone must have length 8")

            s = self.etextbox.text()
            if not s:
                print("Input must not be empty")
                inputvalidity = False
                self.warlabel.setText("Input Valid email")

            s = self.ettextbox.text()
            if s != "N/A":
                if not s.isdigit():
                    print("Empid must be a digit")
                    inputvalidity = False
                    self.warlabel.setText("Empid must be a digit")
            s = self.sttextbox.text()
            if not s:
                print("Input must not be empty")
                inputvalidity = False
                self.warlabel.setText("Input Valid email")
            elif s != "N/A":
                if s != "employee":
                    if s != "manager":
                        print("status can only be N/A,employee and manager")
                        inputvalidity = False
                        self.warlabel.setText("status can only be N/A,employee and manager")


        except ValueError:
            print("Must be an integer")

        print(inputvalidity)
        f = open("webuser.txt", "a")
        rec = open("records.txt", "a")

        if inputvalidity == True:
            if (emplno == "N/A"):

                user = Person(Fullname[0], Username[0], Password[0], Address[0], email[0], telephone[0])
                usetlist_str = str(user.username) + "\\" + str(user.password) + "\\" + str(user.washcard) + "\\" + str(
                    "user")
                usetlist_strreg = str(user.name) + "\\" + str(user.username) + "\\" + str(user.password) + "\\" + str(
                    user.washcard) + "\\" + str(user.address) + "\\" + str(user.email) + "\\" + str(
                    user.telephone) + "\\" + str(user.memberType) + "\\" + str(user.points) + "\\" + str(
                    user.accountamount) + "\\" + " "

                f.writelines(usetlist_str)  # error here
                f.writelines('\n')  # error here
                f.close()
                rec.writelines(usetlist_strreg)  # error here
                rec.writelines('\n')  # error here
                rec.close()
                f = open("webuser.txt", "r")
                rec = open("records.txt", "r")
                print(f.read())
                print("record.txt")
                print(rec.read())
            else:
                emp = Employee(Fullname[0], Username[0], Password[0], Address[0], email[0], telephone[0], status,
                               emplno)
                usetlist_str = str(emp.username) + "\\" + str(emp.password) + "\\" + str(emp.washcard) + "\\" + str(
                    emp.status)
                usetlist_strreg = str(emp.name) + "\\" + str(emp.username) + "\\" + str(emp.password) + "\\" + str(
                    emp.washcard) + "\\" + str(emp.address) + "\\" + str(emp.email) + "\\" + str(
                    emp.telephone)+ "\\" + str(emp.accountamount) + "\\" + str(emp.status) + "\\" + str(emp.empid)
                f.writelines(usetlist_str)  # error here
                f.writelines('\n')  # error here
                f.close()
                rec.writelines(usetlist_strreg)  # error here
                rec.writelines('\n')  # error here
                rec.close()
                f = open("webuser.txt", "r")
                rec = open("records.txt", "r")
                print(f.read())
                print(rec.read())

    def on_clicksign(self):
        self.cams = Signinwindow("self.lineEdit2.text()")
        self.cams.show()

        self.close()


class Signinwindow(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Sign In')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.sign()

    def sign(self):
        # ---------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Name:")
        self.label.move(40, 20)

        self.ustextbox = QLineEdit(self)
        self.ustextbox.move(40, 50)
        self.ustextbox.resize(90, 25)
        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Password:")
        self.label.move(220, 20)

        self.patextbox = QLineEdit(self)
        self.patextbox.move(220, 50)
        self.patextbox.resize(90, 25)

        # Create a button in the window
        self.signbutton = QPushButton('Sign In', self)
        self.signbutton.move(140, 100)
        self.signbutton.clicked.connect(self.signinfunc)
        

    def signinfunc(self):
        # f = open("webuser.txt", "a")
        global index01
        global number
        global identity
        my_file = open("webuser.txt", "r")
        content = my_file.read()
        content_listsign = content.split("\n")
        print(content_listsign)

        my_file.close()
        username = self.ustextbox.text()
        password = self.patextbox.text()

        found = False
        Employee_found = False
        Manager_found = False
        for k in content_listsign:
            temp_array = k.split("\\")
            # Simple User
            if (temp_array[3] == "user"):

                if ((temp_array[0] == username) and (temp_array[1] == password)):
                    found = True
                    index01 = temp_array[2]
                    number=index01
                    identity="user"
                    break
            else:
                if ((temp_array[0] == username) and (temp_array[1] == password)):
                    found = True
                    if (temp_array[3] == "employee"):
                        Employee_found = True

                        index01 = temp_array[2]
                        number = index01
                        identity="employee"
                        print(str(index01))
                    else:
                        Manager_found = True
                        index01 = temp_array[2]
                        number = index01
                        identity="manager"

                    break

        if (found and Employee_found == False and Manager_found == False):
            print("FOUND CREDENTIALS")
            self.cams = UserMain()
            self.cams.show()
            self.show()
            self.close()

        elif (found and Employee_found == True):
            print("FOUND Employee CREDENTIALS")
            self.cams = EmployeeMain()
            self.cams.show()
            self.show()
            self.close()

        elif (found and Manager_found == True):
            print("FOUND manager CREDENTIALS")
            self.cams = ManagerMain()
            self.cams.show()
            self.show()
            self.close()

        else:
            print("DID NOT FIND  CREDENTIALS")
            self.close()

    def goMainWindow(self):
        self.cams = App()
        self.cams.show()
        self.close()


class UserMain(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'User Main'
        self.left = 200
        self.top = 200
        self.width = 370
        self.height = 400
        self.window2()

    def window2(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        # ---------
        # Create a button in the window

        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(20, 20)
        self.outbutton.clicked.connect(self.on_clicksignout)

        self.signbutton = QPushButton('View Information', self)
        self.signbutton.move(140, 110)
        self.signbutton.clicked.connect(self.on_clickviewinfo)


        #  ------------

        self.signbutton = QPushButton('Purchase Product', self)
        self.signbutton.move(140, 150)
        self.signbutton.clicked.connect(self.purchaseproducts)

        # --------------

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Amount To Add:")
        self.label.move(60, 60)

        self.amounttextbox = QLineEdit(self)
        self.amounttextbox.move(100, 60)
        self.amounttextbox.resize(90, 25)

        self.topup = QPushButton('Top up', self)
        self.topup.move(230, 60)
        self.topup.clicked.connect(self.on_clicktopup)

        self.show()

    def purchaseproducts(self):
        self.cams = ProductView()
        self.cams.show()
        self.close()

    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def on_clicktopup(self):
        my_file = open("records.txt", "r")
        content = my_file.read()
        content_listtop = content.split("\n")
        print(self.amounttextbox.text())
        found = False
        m = 0
        for k in content_listtop:
            temp_array = k.split("\\")
            if (len(temp_array) > 2):
                if ((temp_array[3] == index01)):
                    found = True
                    amount = int(temp_array[9]) + int(self.amounttextbox.text())
                    stringbecome = temp_array[0] + "\\" + temp_array[1] + "\\" + temp_array[2] + "\\" + temp_array[
                        3] + "\\" + temp_array[4] + "\\" + temp_array[5] + "\\" + temp_array[6] + "\\" + temp_array[
                                       7] + "\\" + temp_array[8] + "\\" + str(amount) + "\\" + " "
                    content_listtop[m] = stringbecome
                    break
                else:
                    m = m + 1
            else:
                break

        if (found):
            print("Balance Added")
            with open("records.txt", "w") as f:
                print(len(content_listtop))
                for i in range(0, len(content_listtop) - 1):
                    f.writelines((content_listtop[i]))
                    f.writelines("\n")
                f.close()
            rec = open("records.txt", "r")
            print(rec.read())
            rec.close()
        else:
            print("Unable to add")

    @pyqtSlot()
    def on_clickviewinfo(self):
        self.cams = viewinfowindow("self.lineEdit2.text()")
        self.cams.show()

        self.close()





class ProductView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Products list'
        self.left = 200
        self.top = 200
        self.width = 450
        self.height = 600
        self.window3()

    def window3(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(20, 20)
        self.outbutton.clicked.connect(self.on_clicksignout)

        self.backbutton = QPushButton('Back', self)
        self.backbutton.move(270, 20)
        self.backbutton.clicked.connect(self.on_clickback)

        my_file = open("records.txt", "r")
        content = my_file.read()
        content_list = content.split("\n")
        found = False
        simple_user = False
        Employee_user = False
        Manager_user = False
        item_name_1 = ""
        item_price_1 = 0
        item_name_2 = ""
        item_price_2 = 0
        item_name_3 = ""
        item_price_3 = 0
        item_name_4 = ""
        item_price_4 = 0
        item_name_5 = ""
        item_price_5 = 0

        m = 0
        global templen
        for k in content_list:
            temp_array = k.split("\\")
            print("temparray: " + str(temp_array))
            print(str(temp_array[3]) + "==" + str(index01))
            if temp_array != "":
                if ((temp_array[3] == index01)):
                    templen = len(temp_array)
                    if len(temp_array) > 10:
                        found = True
                        simple_user = True

                        break
                    elif len(temp_array) == 10:
                        found = True
                        if (temp_array[8] == "Employee"):

                            Employee_user = True
                        else:
                            Manager_user = True

                        break
                else:
                    m = m + 1
            else:
                break

        my_file = open("products &  prices.txt", "r")
        content = my_file.read()
        content_list = content.split("\n")

        # ---------
        # Create a button in the window

        # Employee_user
        # Simple user is viewing products, give 15 % discount
        print("this is before")
        if (found and simple_user):
            print("this is after")
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[0].split("\\")[0])
            self.label.move(140, 30)
            self.label = QtWidgets.QLabel(self)

            price1 = math.floor(float(content_list[0].split("\\")[1]) * 0.85)
            amount_sold = int(content_list[0].split("\\")[3])
            money_earned = int(content_list[0].split("\\")[4])
            self.label.setText(str(price1))
            self.label.move(170, 60)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 90)
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[0].split("\\")[0], price1, amount_sold, money_earned))
            except:
                pass

            # ---------
            # Create a button in the window

            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[1].split("\\")[0])
            self.label.move(140, 150)
            self.label = QtWidgets.QLabel(self)
            price_2 = math.floor(float(content_list[1].split("\\")[1]) * 0.85)
            amount_sold = int(content_list[1].split("\\")[3])
            money_earned = int(content_list[1].split("\\")[4])
            self.label.setText(str(price_2))
            self.label.move(170, 180)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 210)
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[1].split("\\")[0], price_2, amount_sold, money_earned))
            except:
                pass
            # ---------
            # Create a button in the window
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[2].split("\\")[0])
            self.label.move(140, 240)
            self.label = QtWidgets.QLabel(self)
            price_3 = math.floor(float(content_list[2].split("\\")[1]) * 0.85)
            amount_sold = int(content_list[2].split("\\")[3])
            money_earned = int(content_list[2].split("\\")[4])
            self.label.setText(str(price_3))
            self.label.move(170, 270)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 300)
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[2].split("\\")[0], price_3, amount_sold, money_earned))
            except:
                pass
            # ---------
            # Create a button in the window
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[3].split("\\")[0])
            self.label.move(140, 330)
            self.label = QtWidgets.QLabel(self)
            price_4 = math.floor(float(content_list[3].split("\\")[1]) * 0.85)
            amount_sold = int(content_list[3].split("\\")[3])
            money_earned = int(content_list[3].split("\\")[4])
            self.label.setText(str(price_4))
            self.label.move(170, 360)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 390)

            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[3].split("\\")[0], price_4, amount_sold, money_earned))
            except:
                pass
            # ---------

            # Create a button in the window
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[4].split("\\")[0])
            self.label.move(140, 420)
            self.label = QtWidgets.QLabel(self)
            price_5 = math.floor(float(content_list[4].split("\\")[1]) * 0.85)
            amount_sold = int(content_list[4].split("\\")[3])
            money_earned = int(content_list[4].split("\\")[4])
            self.label.setText(str(price_5))
            self.label.move(170, 450)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 480)
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[4].split("\\")[0], price_5, amount_sold, money_earned))
            except:
                pass
            # self.signbutton.clicked.connect(self.signupfunc)

            self.show()
        elif (found and Employee_user):

            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[0].split("\\")[0])
            self.label.move(140, 30)
            self.label = QtWidgets.QLabel(self)
            print("Price type :")
            print(type(content_list[0].split("\\")[1]))

            price1 = math.floor(float(content_list[0].split("\\")[1]) * 0.7)
            amount_sold = int(content_list[0].split("\\")[3])
            money_earned = int(content_list[0].split("\\")[4])
            self.label.setText(str(price1))
            self.label.move(170, 60)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 90)
            item_name_1 = content_list[0].split("\\")[0]
            item_price_1 = price1
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(item_name_1, item_price_1, amount_sold, money_earned))
            except:
                pass
            # ---------
            # Create a button in the window

            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[1].split("\\")[0])
            self.label.move(140, 150)
            self.label = QtWidgets.QLabel(self)
            price_2 = math.floor(float(content_list[1].split("\\")[1]) * 0.7)
            amount_sold = int(content_list[1].split("\\")[3])
            money_earned = int(content_list[1].split("\\")[4])
            self.label.setText(str(price_2))
            self.label.move(170, 180)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 210)
            item_name_2 = content_list[1].split("\\")[0]
            item_price_2 = price_2
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(item_name_2, item_price_2, amount_sold, money_earned))
            except:
                pass
            # ---------
            # Create a button in the window
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[2].split("\\")[0])
            self.label.move(140, 240)
            self.label = QtWidgets.QLabel(self)
            price_3 = math.floor(float(content_list[2].split("\\")[1]) * 0.7)
            amount_sold = int(content_list[2].split("\\")[3])
            money_earned = int(content_list[2].split("\\")[4])
            self.label.setText(str(price_3))
            self.label.move(170, 270)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 300)
            item_name_3 = content_list[2].split("\\")[0]
            item_price_3 = price_3
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(item_name_3, item_price_3, amount_sold, money_earned))
            except:
                pass
            # ---------
            # Create a button in the window
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[3].split("\\")[0])
            self.label.move(140, 330)
            self.label = QtWidgets.QLabel(self)
            price_4 = math.floor(float(content_list[3].split("\\")[1]) * 0.7)
            amount_sold = int(content_list[3].split("\\")[3])
            money_earned = int(content_list[3].split("\\")[4])
            self.label.setText(str(price_4))
            self.label.move(170, 360)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 390)
            item_name_4 = content_list[3].split("\\")[0]
            item_price_4 = price_4
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(item_name_4, item_price_4, amount_sold, money_earned))
            except:
                pass
            # ---------

            # Create a button in the window
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[4].split("\\")[0])
            self.label.move(140, 420)
            self.label = QtWidgets.QLabel(self)
            price_5 = math.floor(float(content_list[4].split("\\")[1]) * 0.7)
            amount_sold = int(content_list[4].split("\\")[3])
            money_earned = int(content_list[4].split("\\")[4])
            self.label.setText(str(price_5))
            self.label.move(170, 450)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 480)
            item_name_5 = content_list[4].split("\\")[0]
            item_price_5 = price_5
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(item_name_5, item_price_5, amount_sold, money_earned))
            except:
                pass
            # self.signbutton.clicked.connect(self.signupfunc)

            self.show()


        elif (found and Manager_user):

            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[0].split("\\")[0])
            self.label.move(140, 30)
            self.label = QtWidgets.QLabel(self)
            print("Price type :")
            print(type(content_list[0].split("\\")[1]))

            price1 = math.floor(float(content_list[0].split("\\")[1]) * 0.5)
            amount_sold = int(content_list[0].split("\\")[3])
            money_earned = int(content_list[0].split("\\")[4])
            self.label.setText(str(price1))
            self.label.move(170, 60)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 90)
            try:

                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[0].split("\\")[0], price1, amount_sold, money_earned))
            except:
                pass
            # ---------
            # Create a button in the window

            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[1].split("\\")[0])
            self.label.move(140, 150)
            self.label = QtWidgets.QLabel(self)
            price_2 = math.floor(float(content_list[1].split("\\")[1]) * 0.5)
            amount_sold = int(content_list[1].split("\\")[3])
            money_earned = int(content_list[1].split("\\")[4])
            self.label.setText(str(price_2))
            self.label.move(170, 180)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 210)
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[1].split("\\")[0], price_2, amount_sold, money_earned))
            except:
                pass
            # ---------
            # Create a button in the window
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[2].split("\\")[0])
            self.label.move(140, 240)
            self.label = QtWidgets.QLabel(self)
            price_3 = math.floor(float(content_list[2].split("\\")[1]) * 0.5)
            amount_sold = int(content_list[2].split("\\")[3])
            money_earned = int(content_list[2].split("\\")[4])
            self.label.setText(str(price_3))
            self.label.move(170, 270)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 300)
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[2].split("\\")[0], price_3, amount_sold, money_earned))
            except:
                pass
            # ---------
            # Create a button in the window
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[3].split("\\")[0])
            self.label.move(140, 330)
            self.label = QtWidgets.QLabel(self)
            price_4 = math.floor(float(content_list[3].split("\\")[1]) * 0.5)
            amount_sold = int(content_list[3].split("\\")[3])
            money_earned = int(content_list[3].split("\\")[4])
            self.label.setText(str(price_4))
            self.label.move(170, 360)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 390)
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[3].split("\\")[0], price_4, amount_sold, money_earned))
            except:
                pass
            # ---------

            # Create a button in the window
            self.label = QtWidgets.QLabel(self)
            self.label.setText(content_list[4].split("\\")[0])
            self.label.move(140, 420)
            self.label = QtWidgets.QLabel(self)
            price_5 = math.floor(float(content_list[4].split("\\")[1]) * 0.5)
            amount_sold = int(content_list[4].split("\\")[3])
            money_earned = int(content_list[4].split("\\")[4])
            self.label.setText(str(price_5))
            self.label.move(170, 450)

            self.signbutton = QPushButton("Buy", self)
            self.signbutton.move(200, 480)
            try:
                self.signbutton.clicked.connect(
                    lambda: product_bought(content_list[4].split("\\")[0], price_5, amount_sold, money_earned))
            except:
                pass
            # self.signbutton.clicked.connect(self.signupfunc)

            self.show()

        def item1_buy(self):
            product_bought(item_name_1, item_price_1)

        def item2_buy(self):
            product_bought(item_name_2, item_price_2)

        def item3_buy(self):
            product_bought(item_name_3, item_price_3)

        def item4_buy(self):
            product_bought(item_name_4, item_price_4)

        def item5_buy(self):
            product_bought(item_name_5, item_price_5)
    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()
    def on_clickback(self):
        global identity
        if identity == "user":
            self.cams = UserMain()
            self.cams.show()
            self.close()
        elif identity == "employee":
            self.cams = EmployeeMain()
            self.cams.show()
            self.close()
        else:
            self.cams = ManagerMain()
            self.cams.show()
            self.close()


class EmployeeMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Employee Main'
        self.left = 200
        self.top = 200
        self.width = 370
        self.height = 400
        self.window4()

    def window4(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(20, 20)
        self.outbutton.clicked.connect(self.on_clicksignout)
        # ---------
        # Create a button in the window
        self.signbutton = QPushButton('User Details', self)
        self.signbutton.move(140, 80)
        self.signbutton.clicked.connect(self.on_clickuserdetails)

        #  ------------

        self.signbutton1 = QPushButton('User Card Details', self)
        self.signbutton1.move(140, 30)
        self.signbutton1.clicked.connect(self.on_clickusercard)

        # --------------
        # --------------

        self.signbutton2 = QPushButton('Print Record', self)
        self.signbutton2.move(140, 180)
        self.signbutton2.clicked.connect(self.on_clickprintrecords)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Enter Washcard to print:")
        self.label.move(80, 130)
        self.label.resize(120, 25)

        self.sttextbox = QLineEdit(self)
        self.sttextbox.move(200, 130)
        self.sttextbox.resize(110, 25)

        self.signbutton3 = QPushButton('Buy Products', self)
        self.signbutton3.move(140, 230)
        self.signbutton3.clicked.connect(self.employeeproducts)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Amount To Add:")
        self.label.move(110, 260)

        self.amounttextbox = QLineEdit(self)
        self.amounttextbox.move(250, 260)
        self.amounttextbox.resize(90, 25)


        self.topup = QPushButton('Top up', self)
        self.topup.move(140, 290)
        self.topup.clicked.connect(self.on_clicktopup)

        self.show()
    @pyqtSlot()
    def on_clicktopup(self):
        global addamount
        addamount=self.amounttextbox.text()
        FMtopupemployee_manager()


    @pyqtSlot()
    def on_clickuserdetails(self):
        self.cams = userdetails("self.lineEdit2.text()")
        self.cams.show()

        self.close()
    def on_clickprintrecords(self):
        global search
        search=self.sttextbox.text()
        if search == "":
            self.sttextbox.setText("enter Washcard No. here")
        else:
            self.cams = UserPrintinfowindow("self.lineEdit2.text()")
            self.cams.show()

            self.close()

    def on_clickusercard(self):
        self.cams = usercarddetails("self.lineEdit2.text()")
        self.cams.show()

        self.close()

    def employeeproducts(self):
        self.cams = ProductView()
        self.cams.show()
        self.close()

    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()





class UserPrintinfowindow(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PrintInfo Info:')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.printinfo()

    def printinfo(self):
        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(0, 0)
        self.outbutton.clicked.connect(self.on_clicksignout)
        self.backbutton = QPushButton('Back', self)
        self.backbutton.move(200, 0)
        self.backbutton.clicked.connect(self.on_clickback)

        myindex=search
        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Information:")
        self.label.move(90, 20)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Full Name:")
        self.label.move(40, 40)

        self.alabel = QtWidgets.QLabel(self)
        self.alabel.setText("")
        self.alabel.move(200, 40)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Name:")
        self.label.move(40, 70)

        self.blabel = QtWidgets.QLabel(self)
        self.blabel.setText("")
        self.blabel.move(200, 70)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Password:")
        self.label.move(40, 100)

        self.clabel = QtWidgets.QLabel(self)
        self.clabel.setText("")
        self.clabel.move(200, 100)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Wash Card:")
        self.label.move(40, 130)

        self.dlabel = QtWidgets.QLabel(self)
        self.dlabel.setText("")
        self.dlabel.move(200, 130)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Address:")
        self.label.move(40, 160)

        self.elabel = QtWidgets.QLabel(self)
        self.elabel.setText("")
        self.elabel.move(200, 160)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Email:")
        self.label.move(40, 190)

        self.flabel = QtWidgets.QLabel(self)
        self.flabel.setText("")
        self.flabel.move(200, 190)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Telephone:")
        self.label.move(40, 220)

        self.glabel = QtWidgets.QLabel(self)
        self.glabel.setText("")
        self.glabel.move(200, 220)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Balance:")
        self.label.move(40, 250)

        self.hlabel = QtWidgets.QLabel(self)
        self.hlabel.setText("")
        self.hlabel.move(200, 250)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Status:")
        self.label.move(40, 280)

        self.ilabel = QtWidgets.QLabel(self)
        self.ilabel.setText("")
        self.ilabel.move(200, 280)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Employee Id:")
        self.label.move(40, 310)

        self.jlabel = QtWidgets.QLabel(self)
        self.jlabel.setText("")
        self.jlabel.move(200, 310)

        my_file = open("records.txt", "r")
        content = my_file.read()
        content_listview = content.split("\n")

        found = False
        m = 0
        global templen
        for k in content_listview:
            temp_array = k.split("\\")
            print("temparray: " + str(temp_array))
            print(str(temp_array[3]) + "==" + str(myindex))
            if temp_array != "":
                if ((temp_array[3] == myindex)):
                    templen=len(temp_array)
                    if len(temp_array) > 8:
                        found = True
                        self.alabel.setText(str(temp_array[0]))
                        self.blabel.setText(str(temp_array[1]))
                        self.clabel.setText(str(temp_array[2]))
                        self.dlabel.setText(str(temp_array[3]))
                        self.elabel.setText(str(temp_array[4]))
                        self.flabel.setText(str(temp_array[5]))
                        self.glabel.setText(str(temp_array[6]))
                        self.hlabel.setText(str(temp_array[9]))
                        self.ilabel.setText("N/A")
                        self.jlabel.setText("N/A")
                        break
                    elif len(temp_array) == 10:
                        found = True
                        self.alabel.setText(str(temp_array[0]))
                        self.blabel.setText(str(temp_array[1]))
                        self.clabel.setText(str(temp_array[2]))
                        self.dlabel.setText(str(temp_array[3]))
                        self.elabel.setText(str(temp_array[4]))
                        self.flabel.setText(str(temp_array[5]))
                        self.glabel.setText(str(temp_array[6]))
                        self.hlabel.setText(str(temp_array[7]))
                        self.ilabel.setText(str(temp_array[8]))
                        self.jlabel.setText(str(temp_array[9]))
                        break
                else:
                    m = m + 1
            else:
                break

        if (found):
            print("info Shown")
        else:
            print("Unable to show")
        # ---------


        # Create a button in the window
        self.signbutton = QPushButton('Print', self)
        self.signbutton.move(130, 360)
        self.signbutton.clicked.connect(self.on_clickprint)

        self.prilabel = QtWidgets.QLabel(self)
        self.prilabel.setText("")
        self.prilabel.move(120, 380)
        self.prilabel.setGeometry(QtCore.QRect(120, 380, 100, 20))  # (x, y, width, height)

    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()

    def on_clickprint(self):
        self.prilabel.setText("Information Printed")

    def on_clickback(self):
        global identity
        if identity == "employee":
            self.cams = EmployeeMain()
            self.cams.show()
            self.close()
        else:
            self.cams = ManagerMain()
            self.cams.show()
            self.close()

class usercarddetails(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('User Card Details')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.left = 200
        self.top = 200
        self.width = 400
        self.height = 400
        self.usercard()

    def usercard(self):
        # ---------
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(20, 20)
        self.outbutton.clicked.connect(self.on_clicksignout)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Following Are The Records:")
        self.label.move(40, 50)
        self.label = QtWidgets.QLabel(self)
        self.label.move(40, 40)

        # ------------
        self.label = QtWidgets.QLabel(self)
        hello="hello"
        hello=FMreturnusercard()
        self.label.setText(hello)
        self.label.move(40, 70)

        # Create a button in the window
        self.signbutton = QPushButton('Go Back', self)
        self.signbutton.move(150, 300)
        self.signbutton.clicked.connect(self.on_clickgoback)

    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()

    def on_clickgoback(self):
        global identity
        if identity == "employee":
            self.cams = EmployeeMain()
            self.cams.show()
            self.close()
        else:
            self.cams = ManagerMain()
            self.cams.show()
            self.close()


def FMreturnusercard():
    my_file = open("records.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    found = False
    m = 0
    stringbecome=""
    for k in content_list:
        temp_array = k.split("\\")
        if temp_array != "":
            if len(temp_array) > 10:
                found = True
                stringbecome =stringbecome + "      User Name: " + temp_array[1] + "      Wash Card No: " + temp_array[2] + "      Card Amount: " + temp_array[9] + "\n"
                m = m + 1
        else:
            break

    if (found):
        return stringbecome


class userdetails(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('User Details')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.left = 200
        self.top = 200
        self.width = 450
        self.height = 400
        self.userd()

    def userd(self):
        # ---------

        self.setGeometry(self.left, self.top, self.width, self.height)

        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(20, 20)
        self.outbutton.clicked.connect(self.on_clicksignout)

        self.backbutton = QPushButton('Back', self)
        self.backbutton.move(250,20)
        self.backbutton.clicked.connect(self.on_clickback)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Following Are The Records:")
        self.label.move(40, 50)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Fullname \ username\ password \ washcardno \ address \ email \ telephone \ balance")
        self.label.move(40, 70)

        # ------------
        self.label = QtWidgets.QLabel(self)
        hello=FMreturnuser()
        self.label.setText(hello)
        self.label.move(40, 100)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Enter Washcard No.")
        self.label.move(40, 300)
        # Create a button in the window
        self.alabel = QLineEdit(self)
        self.alabel.resize(150, 25)
        self.alabel.move(150, 300)
        self.signbutton = QPushButton('Update Record', self)
        self.signbutton.move(300, 300)
        self.signbutton.clicked.connect(self.on_clickupdaterec)

    @pyqtSlot()
    def on_clickupdaterec(self):
        global search
        global condition
        search=self.alabel.text()
        condition=True
        self.cams = updateinfowindow("self.lineEdit2.text()")
        self.cams.show()
        self.close()
    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()

    def on_clickback(self):
        global identity
        if identity == "employee":
            self.cams = EmployeeMain()
            self.cams.show()
            self.close()
        else:
            self.cams = ManagerMain()
            self.cams.show()
            self.close()


def FMreturnuser():
    my_file = open("records.txt", "r")
    content = my_file.read()
    content_listfm = content.split("\n")
    my_file.close()
    found = False
    m = 0
    stringbecome=""
    for k in content_listfm:
        temp_array = k.split("\\")
        if temp_array != "":
            if len(temp_array) > 10:
                found = True
                stringbecome =stringbecome + temp_array[0] + "\\" + temp_array[1] + "\\" + temp_array[2] + "\\" + temp_array[3] + "\\" + temp_array[4] + "\\" + temp_array[5] + "\\" + temp_array[6] + "\\"+ temp_array[9] + "\n"
                m = m + 1
        else:
            break

    if (found):
        return stringbecome

class ManagerMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Manager Main'
        self.left = 200
        self.top = 200
        self.width = 370
        self.height = 400
        self.window5()

    def window5(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        # ---------
        # Create a button in the window
        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(20, 20)
        self.outbutton.clicked.connect(self.on_clicksignout)

        self.signbuttonu = QPushButton('User Details', self)
        self.signbuttonu.move(140, 30)
        self.signbuttonu.clicked.connect(self.on_clickuserdetails)

        #  ------------

        self.signbutton1 = QPushButton('User Card Details', self)
        self.signbutton1.move(140, 60)
        self.signbutton1.clicked.connect(self.on_clickusercard)

        # --------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Enter Washcard to Delete:")
        self.label.move(110, 90)
        self.label.resize(120, 25)

        self.sttextbox = QLineEdit(self)
        self.sttextbox.move(250, 90)
        self.sttextbox.resize(110, 25)

        self.signbutton2 = QPushButton('Delete record', self)
        self.signbutton2.move(140, 120)
        self.signbutton2.clicked.connect(self.on_clickdeleteuser)

        # --------------
        # --------------
        self.signbuttonmem = QPushButton('View Members', self)
        self.signbuttonmem.move(140, 150)
        self.signbuttonmem.clicked.connect(self.on_clickmemberdetails)
        # --------------
        self.signbutton4 = QPushButton('View Employees', self)
        self.signbutton4.move(140, 180)
        self.signbutton4.clicked.connect(self.on_clickemployeedetails)
        # --------------
        self.signbutton5 = QPushButton('Daily Profit', self)
        self.signbutton5.move(140, 210)
        self.signbutton5.clicked.connect(self.DailyProfitPrint)

        self.signbutton6 = QPushButton('Buy Products', self)
        self.signbutton6.move(140, 240)
        self.signbutton6.clicked.connect(self.managerproducts)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Amount To Add:")
        self.label.move(110, 270)

        self.amounttextbox = QLineEdit(self)
        self.amounttextbox.move(250, 270)
        self.amounttextbox.resize(90, 25)


        self.topup = QPushButton('Top up', self)
        self.topup.move(140, 300)
        self.topup.clicked.connect(self.on_clicktopup)


        self.show()
    def managerproducts(self):
        self.cams = ProductView()
        self.cams.show()
        self.close()
    def on_clickuserdetails(self):
        self.cams = userdetails("self.lineEdit2.text()")
        self.cams.show()

        self.close()
    def on_clickdeleteuser(self):
        global deletee
        deletee=self.sttextbox.text()
        if deletee == "":
            self.sttextbox.setText("Enter Washcard No Here")
        else:
            FMdeleteuser()
            self.sttextbox.setText("")

    def on_clickemployeedetails(self):
        self.cams = employeedetails("self.lineEdit2.text()")
        self.cams.show()

        self.close()

    def on_clickmemberdetails(self):
        self.cams = memberdetails("self.lineEdit2.text()")
        self.cams.show()

        self.close()

    def on_clickusercard(self):
        self.cams = usercarddetails("self.lineEdit2.text()")
        self.cams.show()

        self.close()
    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()

    def on_clicktopup(self):
        global addamount
        addamount=self.amounttextbox.text()
        FMtopupemployee_manager()

    def DailyProfitPrint(self):
        self.cams = PrintProfits("self.lineEdit2.text()")
        # self.cams = PrintProfits()
        self.cams.show()

        self.close()

class employeedetails(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Employee Details')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.left = 200
        self.top = 200
        self.width = 450
        self.height = 400
        self.employeedeta()

    def employeedeta(self):
        # ---------

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(20, 20)
        self.outbutton.clicked.connect(self.on_clicksignout)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Following Are The Records:")
        self.label.move(40, 50)
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Fullname \ username\ password \ washcardno \ address \ email \ telephone \ balance \ Status \ Emp-id ")
        self.label.move(40, 80)

        # ------------
        self.label = QtWidgets.QLabel(self)
        hello=FMreturnemployee()
        self.label.setText(hello)
        self.label.move(40, 100)

        self.signbutton = QPushButton('Back', self)
        self.signbutton.move(300, 300)

    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()

    def on_clickback(self):
        global identity
        if identity == "employee":
            self.cams = EmployeeMain()
            self.cams.show()
            self.close()
        else:
            self.cams = ManagerMain()
            self.cams.show()
            self.close()


class memberdetails(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Member Details')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.left = 200
        self.top = 200
        self.width = 450
        self.height = 400
        self.memberdeta()

    def memberdeta(self):
        # ---------

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(20, 20)
        self.outbutton.clicked.connect(self.on_clicksignout)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Following Are The Records:")
        self.label.move(40, 50)
        self.label = QtWidgets.QLabel(self)
        self.label.move(40, 40)

        # ------------
        self.label = QtWidgets.QLabel(self)
        hello = "hello"
        hello = FMreturnusermembership()
        self.label.setText(hello)
        self.label.move(40, 70)

        # Create a button in the window
        self.signbutton = QPushButton('Go Back', self)
        self.signbutton.move(150, 300)
        self.signbutton.clicked.connect(self.on_clickback)

    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()

    def on_clickback(self):
        global identity
        if identity == "employee":
            self.cams = EmployeeMain()
            self.cams.show()
            self.close()
        else:
            self.cams = ManagerMain()
            self.cams.show()
            self.close()


def FMreturnusermembership():
    my_file = open("records.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    found = False
    m = 0
    stringbecome=""
    for k in content_list:
        temp_array = k.split("\\")
        if temp_array != "":
            if len(temp_array) > 10:
                found = True
                stringbecome =stringbecome + "      User Name: " + temp_array[1] + "      Wash Card No: " + temp_array[2] + "      Card Amount: " + temp_array[9]+ "      Member: " + temp_array[7] + "\n"
                m = m + 1
        else:
            break

    if (found):
        return stringbecome


def FMtopupemployee_manager():
    global addamount
    my_file = open("records.txt", "r")
    content = my_file.read()
    content_listtop = content.split("\n")
    print(addamount)
    found = False
    m = 0
    for k in content_listtop:
        temp_array = k.split("\\")
        print("temparray: " + str(temp_array))
        print(str(temp_array[3]) + "==" + str(index01))
        if temp_array != "":
            if ((temp_array[3] == index01)):
                found = True
                amount = int(temp_array[7]) + int(addamount)
                stringbecome = temp_array[0] + "\\" + temp_array[1] + "\\" + temp_array[2] + "\\" + temp_array[
                    3] + "\\" + temp_array[4] + "\\" + temp_array[5] + "\\" + temp_array[6] + "\\" + str(amount)+ "\\" + temp_array[8]+ "\\" + temp_array[9]
                content_listtop[m] = stringbecome
                break
            else:
                m = m + 1
        else:
            break

    if (found):
        print("Balance Added")
        with open("records.txt", "w") as f:
            print(len(content_listtop))
            for i in range(0, len(content_listtop) - 1):
                f.writelines((content_listtop[i]))
                f.writelines("\n")
            f.close()
        rec = open("records.txt", "r")
        print(rec.read())
        rec.close()
    else:
        print("Unable to add")


def FMreturnemployee():
    my_file = open("records.txt", "r")
    content = my_file.read()
    content_listfm = content.split("\n")
    my_file.close()
    found = False
    m = 0
    stringbecome=""
    for k in content_listfm:
        temp_array = k.split("\\")
        if temp_array != "":
            if len(temp_array)==10:
                if temp_array[8]=="employee":
                    found = True
                    stringbecome =stringbecome + temp_array[0] + "\\" + temp_array[1] + "\\" + temp_array[2] + "\\" + temp_array[3] + "\\" + temp_array[4] + "\\" + temp_array[5] + "\\" + temp_array[6] + "\\"+ temp_array[7]+ "\\"+ temp_array[8]+ "\\"+ temp_array[9] + "\n"
                    m = m + 1
            else:
                m=m+1
        else:
            break

    if (found):
        if stringbecome=="":
            hel="no employee present"
            return hel
        else:
            return stringbecome

def FMdeleteuser():
    global deletee
    my_file = open("records.txt", "r")
    content = my_file.read()
    content_listinfo1 = content.split("\n")
    found = False
    m = 0
    for k in content_listinfo1:
        temp_array = k.split("\\")
        print("temparray: " + str(temp_array))
        print(str(temp_array[3]) + "==" + str(deletee))
        if temp_array != "":
            if ((temp_array[3] == deletee)):
                found = True
                content_listinfo1.pop(m)
                break
            else:
                m = m + 1
        else:
            break
    if (found):
        mycontent = content_listinfo1
        print(type(mycontent))
        a = len(mycontent)
        with open("records.txt", "w") as f:

            for i in range(0, a - 1):
                f.writelines((mycontent[i]))
                f.writelines("\n")
            f.close()
        rec = open("records.txt", "r")
        print(rec.read())
        rec.close()
        print("record updated account deleted from record.txt")
        print(content_listinfo1)

    my_file = open("webuser.txt", "r")
    content = my_file.read()
    content_listinfo2 = content.split("\n")
    found = False
    m = 0
    for k in content_listinfo2:
        temp_array = k.split("\\")
        print("temparray: " + str(temp_array))
        print(str(temp_array[2]) + "==" + str(deletee))
        if temp_array != "":
            if ((temp_array[2] == deletee)):
                found = True
                content_listinfo2.pop(m)
                break
            else:
                m = m + 1
        else:
            break
    if (found):
        mycontent = content_listinfo2
        print(type(content_listinfo2))
        a = len(content_listinfo2)
        with open("webuser.txt", "w") as f:

            for i in range(0, a - 1):
                f.writelines((content_listinfo2[i]))
                f.writelines("\n")
            f.close()
        rec = open("webuser.txt", "r")
        print(rec.read())
        rec.close()
        print("record updated account deleted from webuser.txt")
        print(content_listinfo2)


class viewinfowindow(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('View Info:')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.viewinfo()

    def viewinfo(self):
        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(0, 0)
        self.outbutton.clicked.connect(self.on_clicksignout)

        self.backbutton = QPushButton('Back', self)
        self.backbutton.move(170, 0)
        self.backbutton.clicked.connect(self.on_clickback)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Information:")
        self.label.move(70, 20)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Full Name:")
        self.label.move(40, 40)

        self.alabel = QtWidgets.QLabel(self)
        self.alabel.setText("")
        self.alabel.move(200, 40)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Name:")
        self.label.move(40, 70)

        self.blabel = QtWidgets.QLabel(self)
        self.blabel.setText("")
        self.blabel.move(200, 70)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Password:")
        self.label.move(40, 100)

        self.clabel = QtWidgets.QLabel(self)
        self.clabel.setText("")
        self.clabel.move(200, 100)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Wash Card:")
        self.label.move(40, 130)

        self.dlabel = QtWidgets.QLabel(self)
        self.dlabel.setText("")
        self.dlabel.move(200, 130)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Address:")
        self.label.move(40, 160)

        self.elabel = QtWidgets.QLabel(self)
        self.elabel.setText("")
        self.elabel.move(200, 160)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Email:")
        self.label.move(40, 190)

        self.flabel = QtWidgets.QLabel(self)
        self.flabel.setText("")
        self.flabel.move(200, 190)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Telephone:")
        self.label.move(40, 220)

        self.glabel = QtWidgets.QLabel(self)
        self.glabel.setText("")
        self.glabel.move(200, 220)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Balance:")
        self.label.move(40, 250)

        self.hlabel = QtWidgets.QLabel(self)
        self.hlabel.setText("")
        self.hlabel.move(200, 250)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Status:")
        self.label.move(40, 280)

        self.ilabel = QtWidgets.QLabel(self)
        self.ilabel.setText("")
        self.ilabel.move(200, 280)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Employee Id:")
        self.label.move(40, 310)

        self.jlabel = QtWidgets.QLabel(self)
        self.jlabel.setText("")
        self.jlabel.move(200, 310)

        my_file = open("records.txt", "r")
        content = my_file.read()
        content_listview = content.split("\n")

        found = False
        m = 0
        global templen
        for k in content_listview:
            temp_array = k.split("\\")
            print("temparray: " + str(temp_array))
            print(str(temp_array[3]) + "==" + str(index01))
            if temp_array != "":
                if ((temp_array[3] == index01)):
                    templen=len(temp_array)
                    if len(temp_array) > 10:
                        found = True
                        self.alabel.setText(str(temp_array[0]))
                        self.blabel.setText(str(temp_array[1]))
                        self.clabel.setText(str(temp_array[2]))
                        self.dlabel.setText(str(temp_array[3]))
                        self.elabel.setText(str(temp_array[4]))
                        self.flabel.setText(str(temp_array[5]))
                        self.glabel.setText(str(temp_array[6]))
                        self.hlabel.setText(str(temp_array[9]))
                        self.ilabel.setText("N/A")
                        self.jlabel.setText("N/A")
                        break
                    elif len(temp_array) == 10:
                        found = True
                        self.alabel.setText(str(temp_array[0]))
                        self.blabel.setText(str(temp_array[1]))
                        self.clabel.setText(str(temp_array[2]))
                        self.dlabel.setText(str(temp_array[3]))
                        self.elabel.setText(str(temp_array[4]))
                        self.flabel.setText(str(temp_array[5]))
                        self.glabel.setText(str(temp_array[6]))
                        self.hlabel.setText(str(temp_array[7]))
                        self.ilabel.setText(str(temp_array[8]))
                        self.jlabel.setText(str(temp_array[9]))
                        break
                else:
                    m = m + 1
            else:
                break

        if (found):
            print("info Shown")
        else:
            print("Unable to show")
        # ---------


        # Create a button in the window
        self.signbutton = QPushButton('Update', self)
        self.signbutton.move(130, 360)
        self.signbutton.clicked.connect(self.on_clickupdateinfo)
    @pyqtSlot()
    def on_clickupdateinfo(self):
        global condition
        condition=False
        self.cams = updateinfowindow("self.lineEdit2.text()")
        self.cams.show()

        self.close()

    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()

    def on_clickback(self):
        self.cams = UserMain()
        self.cams.show()
        self.close()

class updateinfowindow(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Update Info:')
        self.left = 200
        self.top = 200
        self.width = 370
        self.height = 400
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.viewinfotoup()

    def viewinfotoup(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        global index01
        global number
        global condition
        global templen
        if condition==True:
            index01=search
            my_file = open("records.txt", "r")
            content = my_file.read()
            content_list = content.split("\n")
            for k in content_list:
                temp_array = k.split("\\")
                print("temparray: " + str(temp_array))
                print(str(temp_array[3]) + "==" + str(index01))
                if temp_array != "":
                    if ((temp_array[3] == index01)):
                        templen = len(temp_array)
                        condition=False
                        break


        self.outbutton = QPushButton('Sign Out', self)
        self.outbutton.move(0, 0)
        self.outbutton.clicked.connect(self.on_clicksignout)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Information:")
        self.label.move(40, 20)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Full Name:")
        self.label.move(40, 40)

        self.alabel = QLineEdit(self)
        self.alabel.setText("")
        self.alabel.move(200, 40)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Name:")
        self.label.move(40, 70)

        self.blabel = QLineEdit(self)
        self.blabel.setText("")
        self.blabel.move(200, 70)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Password:")
        self.label.move(40, 100)

        self.clabel = QLineEdit(self)
        self.clabel.setText("")
        self.clabel.move(200, 100)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Wash Card:")
        self.label.move(40, 130)

        self.dlabel = QtWidgets.QLabel(self)
        self.dlabel.setText("")
        self.dlabel.move(200, 130)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Address:")
        self.label.move(40, 160)

        self.elabel = QLineEdit(self)
        self.elabel.setText("")
        self.elabel.move(200, 160)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Email:")
        self.label.move(40, 190)

        self.flabel = QLineEdit(self)
        self.flabel.setText("")
        self.flabel.move(200, 190)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Telephone:")
        self.label.move(40, 220)

        self.glabel = QLineEdit(self)
        self.glabel.setText("")
        self.glabel.move(200, 220)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Balance:")
        self.label.move(40, 250)

        self.hlabel = QtWidgets.QLabel(self)
        self.hlabel.setText("")
        self.hlabel.move(200, 250)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Status:")
        self.label.move(40, 280)

        self.ilabel = QtWidgets.QLabel(self)
        self.ilabel.setText("")
        self.ilabel.move(200, 280)

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Employee Id:")
        self.label.move(40, 310)

        self.jlabel = QtWidgets.QLabel(self)
        self.jlabel.setText("")
        self.jlabel.move(200, 310)

        my_file = open("records.txt", "r")
        content = my_file.read()
        content_listtoup = content.split("\n")
        my_file.close()
        found = False
        m = 0
        for k in content_listtoup:
            temp_array = k.split("\\")
            print("temparray: " + str(temp_array))
            print(str(temp_array[3]) + "==" + str(index01))
            if temp_array != "":
                if ((temp_array[3] == index01)):
                    templen=len(temp_array)
                    if len(temp_array) > 10:
                        found = True
                        self.alabel.setText(str(temp_array[0]))
                        self.blabel.setText(str(temp_array[1]))
                        self.clabel.setText(str(temp_array[2]))
                        self.dlabel.setText(str(temp_array[3]))
                        self.elabel.setText(str(temp_array[4]))
                        self.flabel.setText(str(temp_array[5]))
                        self.glabel.setText(str(temp_array[6]))
                        self.hlabel.setText(str(temp_array[9]))
                        self.ilabel.setText("N/A")
                        self.jlabel.setText("N/A")
                        break
                    elif len(temp_array) == 10:
                        found = True
                        self.alabel.setText(str(temp_array[0]))
                        self.blabel.setText(str(temp_array[1]))
                        self.clabel.setText(str(temp_array[2]))
                        self.dlabel.setText(str(temp_array[3]))
                        self.elabel.setText(str(temp_array[4]))
                        self.flabel.setText(str(temp_array[5]))
                        self.glabel.setText(str(temp_array[6]))
                        self.hlabel.setText(str(temp_array[7]))
                        self.ilabel.setText(str(temp_array[8]))
                        self.jlabel.setText(str(temp_array[9]))
                        break
                else:
                    m = m + 1
            else:
                break

        if (found):
            print("info Shown")
        else:
            print("Unable to show")
        # ---------


        # Create a button in the window
        self.signbutton = QPushButton('Update', self)
        self.signbutton.move(130, 360)
        self.signbutton.clicked.connect(self.on_clickupdateinfo1)
    @pyqtSlot()
    def on_clickupdateinfo1(self):
        global index01
        global templen
        global identity
        len1=templen
        if len1 > 10:
            my_file = open("records.txt", "r")
            content = my_file.read()
            content_listinfo1 = content.split("\n")

            found = False
            m = 0
            for k in content_listinfo1:
                temp_array = k.split("\\")
                print("temparray: " + str(temp_array))
                print(str(temp_array[3]) + "==" + str(index01))
                if temp_array != "":
                    if ((temp_array[3] == index01)):
                        found = True
                        stringbecome = str(self.alabel.text()) + "\\" + str(self.blabel.text()) + "\\" + str(
                            self.clabel.text()) + "\\" + str(self.dlabel.text()) + "\\" + str(
                            self.elabel.text()) + "\\" + str(self.flabel.text()) + "\\" + str(
                            self.glabel.text()) + "\\" + str(temp_array[7])+ "\\" + str(temp_array[8])+ "\\" + str(self.hlabel.text())+ "\\" + " "
                        content_listinfo1[m] = stringbecome
                        break
                    else:
                        m = m + 1
                else:
                    break

            my_filee = open("webuser.txt", "r")
            contentweb = my_filee.read()
            content_listinfoweb = contentweb.split("\n")
            m = 0
            for k in content_listinfoweb:
                temp_array = k.split("\\")
                print("temparray: " + str(temp_array))
                print(str(temp_array[2]) + "==" + str(index01))
                if temp_array != "":
                    if ((temp_array[2] == index01)):
                        found = True
                        stringbecome = str(self.blabel.text()) + "\\" + str(self.clabel.text()) + "\\" + str(self.dlabel.text()) + "\\" + "user"
                        content_listinfoweb[m] = stringbecome
                        index01 = number
                        break
                    else:
                        m = m + 1
                else:
                    break

        elif len1 == 10:
            my_file = open("records.txt", "r")
            content = my_file.read()
            content_listinfo1 = content.split("\n")
            print(self.amounttextbox.text())

            found = False
            m = 0
            for k in content_listinfo1:
                temp_array = k.split("\\")
                print("temparray: " + str(temp_array))
                print(str(temp_array[3]) + "==" + str(index01))
                if temp_array != "":
                    if ((temp_array[3] == index01)):
                        found = True
                        amount = int(temp_array[7]) + int(self.amounttextbox.text())
                        stringbecome = str(self.alabel.text()) + "\\" + str(self.blabel.text()) + "\\" + str(
                            self.clabel.text()) + "\\" + str(self.dlabel.text()) + "\\" + str(
                            self.elabel.text()) + "\\" + str(self.flabel.text()) + "\\" + str(
                            self.glabel.text()) + "\\" + str(self.hlabel.text())+ "\\" + str(self.ilabel.text())+ "\\" + str(self.jlabel.text())
                        content_listinfo1[m] = stringbecome
                        print(content_listinfo1)
                        break
                    else:
                        m = m + 1
                else:
                    break
            my_filee = open("webuser.txt", "r")
            contentweb = my_filee.read()
            content_listinfoweb = contentweb.split("\n")
            m = 0
            for k in content_listinfoweb:
                temp_array = k.split("\\")
                print("temparray: " + str(temp_array))
                print(str(temp_array[2]) + "==" + str(index01))
                if temp_array != "":
                    if ((temp_array[2] == index01)):
                        found = True
                        stringbecome = str(self.blabel.text()) + "\\" + str(self.clabel.text()) + "\\" + str(self.dlabel.text()) + "\\" + str(self.ilabel.text())
                        content_listinfoweb[m] = stringbecome
                        index01 = number
                        break
                    else:
                        m = m + 1
                else:
                    break
        if (found):
            print("record updated")
            print(content_listinfo1)
            mycontent = content_listinfo1
            print(type(mycontent))
            a = len(mycontent)
            with open("records.txt", "w") as f:

                for i in range(0, a- 1):
                    f.writelines((mycontent[i]))
                    f.writelines("\n")
                f.close()
            rec = open("records.txt", "r")
            print(rec.read())
            rec.close()

            print("record updated in web")
            print(content_listinfoweb)
            mycontentweb = content_listinfoweb
            print(type(mycontentweb))
            a = len(mycontentweb)
            with open("webuser.txt", "w") as f:

                for i in range(0, a - 1):
                    f.writelines((mycontentweb[i]))
                    f.writelines("\n")
                f.close()
            rec = open("webuser.txt", "r")
            print(rec.read())
            rec.close()

            if identity == "user":
                self.cams = viewinfowindow("self.lineEdit2.text()")
                self.cams.show()
                self.close()

            elif identity == "employee":
                self.cams = userdetails("self.lineEdit2.text()")
                self.cams.show()
                self.close()
            elif identity == "manager":
                self.cams = userdetails("self.lineEdit2.text()")
                self.cams.show()
                self.close()

        else:
            print("Unable to update")

    def on_clicksignout(self):
        self.cams = App()
        self.cams.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
