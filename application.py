from PyQt5 import QtCore, QtGui, QtWidgets
from InstagramAPI import InstagramAPI
import os
import sys
import json
from time import sleep
from threading import Thread


class InputUI(object):
    def __init__(self):
        self.username = ''
        self.password = ''

    def setup_user_interface(self, mainwindow):
        self.MainWindow = mainwindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(500, 400)
        self.MainWindow.setWindowTitle('Credentials')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindow.sizePolicy().hasHeightForWidth())
        self.MainWindow.setSizePolicy(sizePolicy)
        self.MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        self.MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        self.MainWindow.setStyleSheet("background-color: rgb(25, 25, 25);")

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.usrname_entry_field = QtWidgets.QLineEdit(self.centralwidget)
        self.usrname_entry_field.setGeometry(QtCore.QRect(100, 110, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.usrname_entry_field.setFont(font)
        self.usrname_entry_field.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.usrname_entry_field.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.usrname_entry_field.setStyleSheet(
        	"border-radius: 30px;\n"
			"border: 2px solid black;\n"
			"border-color: rgb(52, 152, 219);\n"
			"background-color: rgb(25, 25, 25);\n"
			"color: rgb(255, 255, 255);"
			)
        self.usrname_entry_field.setAlignment(QtCore.Qt.AlignCenter)
        self.usrname_entry_field.setObjectName("usrname_entry_field")
        self.usrname_entry_field.setPlaceholderText("Username")

        self.pwd_entry_field = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd_entry_field.setGeometry(QtCore.QRect(100, 200, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.pwd_entry_field.setFont(font)
        self.pwd_entry_field.setStyleSheet(
        	"border-radius: 30px;\n"
			"border: 2px solid black;\n"
			"border-color: rgb(52, 152, 219);\n"
			"background-color: rgb(25, 25, 25);\n"
			"color: rgb(255, 255, 255);"
			)
        self.pwd_entry_field.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pwd_entry_field.setAlignment(QtCore.Qt.AlignCenter)
        self.pwd_entry_field.setReadOnly(False)
        self.pwd_entry_field.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pwd_entry_field.setClearButtonEnabled(False)
        self.pwd_entry_field.setObjectName("pwd_entry_field")
        self.pwd_entry_field.setPlaceholderText("Password")
        self.pwd_entry_field.setEchoMode(self.pwd_entry_field.Password)

        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(175, 290, 150, 60))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setMouseTracking(True)
        self.login_button.setStyleSheet("QPushButton{border-radius: 30px;border: 2px solid black;border-color: rgb(46, 204, 113);background-color: rgb(25, 25, 25);color: rgb(255, 255, 255);}QPushButton:hover{background-color: rgb(46, 204, 113);}")
        self.login_button.setObjectName("login_button")
        self.login_button.setText('Login')
        pal = self.login_button.palette()
        pal.setColor(QtGui.QPalette.Background, QtCore.Qt.red)
        self.login_button.setPalette(pal)
        self.login_button.setAutoFillBackground(True)
        self.login_button.setFlat(True)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(126, 40, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText('CREDENTIALS')

        self.MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


class OutputUI(object):
    def setup_user_interface(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        MainWindow.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(126, 30, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Insta Manager")
        self.output_field = QtWidgets.QLabel(self.centralwidget)
        self.output_field.setGeometry(QtCore.QRect(30, 100, 441, 271))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(12)
        self.output_field.setFont(font)
        self.output_field.setStyleSheet(
        	"border-color: rgb(255, 255, 255);\n"
			"color: white;\n"
			""
			)
        self.output_field.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output_field.setIndent(4)
        self.output_field.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.output_field.setObjectName("output_field")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


class InstagramManager:
    def __init__(self, usr, pwd, output, main):
        self.__USERNAME = usr
        self.__PASSWORD = pwd
        self.output_field = output
        self.message = ""
        self.main = main
        self.__api = InstagramAPI(self.__USERNAME, self.__PASSWORD)
        self.followers = []
        self.followees = []
        self.number_of_followers = 0
        self.number_of_followees = 0
        self.traitors = []
        self.pending_follow_backs = []

    def output(self, message):
        self.message += "\n" + message
        self.output_field.setText(self.message)
        self.main.show()

    def login(self):
        try:
            self.__api.login()
        except:
            self.output("ERROR : login error.")
            sleep(3)
            quit(-1)
        self.output(">>> Successful login attempt")

    def fetch_profile_data(self):
        self.output(">>> Fetching your profile data")
        self.followers = self.__api.getTotalSelfFollowers()
        self.followees = self.__api.getTotalSelfFollowings()

        for follower in self.followers:
            del follower['profile_pic_url']
            del follower['latest_reel_media']
            follower['profile_page_url'] = f"https://www.instagram.com/{follower['username']}/"
        for followee in self.followees:
            del followee['profile_pic_url']
            del followee['latest_reel_media']
            del followee['is_favorite']
            followee['profile_page_url'] = f"https://www.instagram.com/{followee['username']}/"

        self.number_of_followers = len(self.followers)
        self.number_of_followees = len(self.followees)
        self.output("\tStatus : Complete")
        sleep(3)
        self.output("")

    def get_followers(self, action="save"):
        data = json.dumps(self.followers, indent=4)
        if action == "save":
            file = open(".\\library\\followers.json", "w")
            file.write(data)
            file.close()
        elif action == "print":
            print(data)
        elif action == "save_and_print":
            file = open(".\\library\\followers.json", "w")
            file.write(data)
            file.close()
            print(data)
        else:
            self.output('ERROR : unexpected argument for parameter "action"')
            sleep(3)
            quit(-1)

    def get_followees(self, action="save"):
        data = json.dumps(self.followees, indent=4)
        if action == "save":
            file = open(".\\library\\followees.json", "w")
            file.write(data)
            file.close()
        elif action == "print":
            print(data)
        elif action == "save_and_print":
            file = open(".\\library\\followees.json", "w")
            file.write(data)
            file.close()
            print(data)
        else:
            self.output('ERROR : unexpected argument for parameter "action"')
            sleep(3)
            quit(-1)

    def get_traitors(self, action="save"):
        usernames_of_followers = [follower['username'] for follower in self.followers]
        for followee in self.followees:
            if followee['username'] not in usernames_of_followers:
                self.traitors.append(followee)
        data = json.dumps(self.traitors, indent=4)
        if action == "print":
            print(data)
        elif action == "save":
            file = open(".\\library\\traitors.json", "w")
            file.write(data)
            file.close()
        else:
            self.output('ERROR : unexpected argument for parameter "action"')
            sleep(3)
            quit(-1)

    def get_pending_follow_backs(self, action="save"):
        usernames_of_followees = [followee['username'] for followee in self.followees]
        for follower in self.followers:
            if follower['username'] not in usernames_of_followees:
                self.pending_follow_backs.append(follower)
        data = json.dumps(self.pending_follow_backs, indent=4)
        if action == "print":
            print(data)
        elif action == "save":
            file = open(".\\library\\pending_follow_backs.json", "w")
            file.write(data)
            file.close()
        else:
            self.output('ERROR : unexpected argument for parameter "action"')
            sleep(3)
            quit(-1)

    def logout(self):
        try:
            self.__api.logout()
        except:
            self.output("ERROR : logout error")
        self.output(">>> Logged out successfully")


def manager(usr, pwd, out, main):
    manager = InstagramManager(usr, pwd, out, main)

    manager.login()
    manager.fetch_profile_data()

    manager.get_followers()
    manager.get_followees()
    manager.get_traitors()
    manager.get_pending_follow_backs()

    message = "\nData has been saved to the directory : \n\tInstaSleuth\\library\n\nLogout will be initiated in 5 seconds.\n"
    out.setText(message)

    sleep(5)
    manager.logout()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.input_user_interface = InputUI()
        self.output_user_interface = OutputUI()
        self.start_input_window()

    def start_output_window(self):
        self.output_user_interface.setup_user_interface(self)
        self.show()
        arguments = (self.input_user_interface.usrname_entry_field.text(),
                     self.input_user_interface.pwd_entry_field.text(),
                     self.output_user_interface.output_field,
                     self,)
        thread = Thread(name="manager", target=manager, args=arguments)
        thread.daemon = True
        thread.start()

    def start_input_window(self):
        self.input_user_interface.setup_user_interface(self)
        self.input_user_interface.login_button.clicked.connect(self.start_output_window)
        self.show()


if __name__ == '__main__':
    if not os.path.exists(".\\library"):
        os.mkdir(".\\library")
        
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
