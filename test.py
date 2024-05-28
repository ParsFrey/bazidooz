from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QtCore.QRect(310, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushbutton.setFont(font)
        self.pushbutton.setObjectName("pushbutton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(280, 50, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, 50, 20, 491))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(120, 190, 501, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(120, 380, 501, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 70, 61, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 70, 61, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 70, 61, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 240, 61, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 240, 61, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(520, 240, 61, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 420, 61, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(360, 420, 61, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(520, 420, 61, 101))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 550, 671, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushbutton.clicked.connect(self.khob)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushbutton.setText(_translate("MainWindow", "خب؟"))
        self.lineEdit.setText(_translate("MainWindow", "?"))
        self.lineEdit_2.setText(_translate("MainWindow", "?"))
        self.lineEdit_3.setText(_translate("MainWindow", "?"))
        self.lineEdit_4.setText(_translate("MainWindow", "?"))
        self.lineEdit_5.setText(_translate("MainWindow", "?"))
        self.lineEdit_6.setText(_translate("MainWindow", "?"))
        self.lineEdit_7.setText(_translate("MainWindow", "?"))
        self.lineEdit_8.setText(_translate("MainWindow", "?"))
        self.lineEdit_9.setText(_translate("MainWindow", "?"))
        self.label.setText(_translate("MainWindow", "نوبتی خانه هارا با x و یا o پر کنید و در آخر \"خب\" را فشار دهید."))

    def khob(self):
        winning_combinations = [
            (self.lineEdit, self.lineEdit_2, self.lineEdit_3),
            (self.lineEdit_4, self.lineEdit_5, self.lineEdit_6),
            (self.lineEdit_7, self.lineEdit_8, self.lineEdit_9),
            (self.lineEdit, self.lineEdit_4, self.lineEdit_7),
            (self.lineEdit_2, self.lineEdit_5, self.lineEdit_8),
            (self.lineEdit_3, self.lineEdit_6, self.lineEdit_9),
            (self.lineEdit, self.lineEdit_5, self.lineEdit_9),
            (self.lineEdit_3, self.lineEdit_5, self.lineEdit_7)
        ]

        def check_winner(player):
            for combination in winning_combinations:
                if all(cell.text() == player for cell in combination):
                    return True
            return False

        try:
            if check_winner('x'):
                self.label.setText("player x won")
            elif check_winner('o'):
                self.label.setText("player o won")
            else:
                self.label.setText("No winner yet")
        except Exception as error:
            self.label.setText(" لطفا با توجه به Readme دوباره امتحان کنید.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
