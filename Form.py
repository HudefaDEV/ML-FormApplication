"""

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DISCLAIMER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!This project was created by researching, learning and using other developers codes, articles, and applications documentations. This project was NOT developed!
!from PURE ORIGINAL MIND POWER of the developer. However, some modification, features and troubleshooting(the troubleshooting made me go NUTZ) was done by    !
!the developer's PURE MIND POWER.                                                                                                                             !
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Programing Language
- Python

# IDE (Integrated development environment)
-PyCharm

# Authentication & Database
- Firebase
- Email and Password authentication

# Usage
After running the application, a GUI login window will pop up. There are 2 options:
- Signing in using the a pre-created account.
- Creating a new account.

If the user has an account, they can proceed with logging in, If not, users are required to create an account before to be able to login.
Clicking on the creating a new account, firstly, a GUI windows will pop up, within the windows there's 2 sections to fill "Email & Password".
"Email" must have an email format to be accepted and the password must be 6 or more characters or numbers. A message will appear in the command
line with failure or success in creating an account.

Furthermore, creating an account successfully leads to creating a profile, which ask for ("user", "fullname", "age", "email", and "ssn"
which is Social Security Number). An option will appear if the user would like to display their data?, that's the user's choice.
"Granted Login, Earned it user" - Yoda

A successful logging will ask for the user created, so the user can be able to display their profile.


Notes:
    The Credentials below are the firebase dummy account used in the project.
    Mail: formapp.ml@gmail.com
    Password: Testapplication

"""

import sys  # To be able to launch applications
from termcolor import colored  # Changing colors of output.
from PyQt5 import QtWidgets, uic  # To be able to create, modify UIs and load them.
# from pyrebase4 import pyrebase  # A troubleshooting method in case of failure of PYREBASE package.
from Pyrebase import pyrebase  # A package to be able to modify and use firebase in python.

""" 
+ from Cryptodome.Cipher import AES  # A troubleshooting method in case of failure "CRYPTO" package (it's common). 
The problem was solved by modifying the pyrebase.py and changing "crypto" to "cryptodome"

# In case of failure, the configuration data may not contain "databaseURL". 
Manually add it ('databaseURL': "https://your-project-ID.firebaseio.com") or add firebase database link if it's used.
"""

FB_config = {

    'apiKey': "AIzaSyDtaxD3RKQlIVLXs-KmGfyyu1RkuXyqg-4",
    'authDomain': "formapp-ml.firebaseapp.com",
    'databaseURL': "https://formapp-ml-default-rtdb.firebaseio.com",
    'projectId': "formapp-ml",
    'storageBucket': "formapp-ml.appspot.com",
    'messagingSenderId': "236377735057",
    'appId': "1:236377735057:web:bd0524937f95644f28e430",
    'measurementId': "G-FL7KNFJERR"
}

FB = pyrebase.initialize_app(FB_config)  # To start the application
app_auth = FB.auth()  # To able to use firebase AUTHENTICATION service
app_db = FB.database()  # To able to use firebase DATABASE service


class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("Login.ui", self)
        self.button = self.findChild(QtWidgets.QPushButton, 'GO')  # Finding the button.
        self.button.clicked.connect(self.sign_in)  # Passing the return value.
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)  # To make the password column hidden when typing.
        self.button = self.findChild(QtWidgets.QPushButton, 'Acreation')  # Finding the button.
        self.button.clicked.connect(account_creation)  # Passing the return value.

    def sign_in(self):  # A sign in function
        email = self.email.text()  # Outputting the data into a variable
        password = self.password.text()  # Outputting the data into a variable
        try:
            app_auth.sign_in_with_email_and_password(email, password)
            print(colored(f"Successfully logged in with > \nEmail: {email} \nPassword: {password}", 'green'))

            #  Some code to display the account's information.
            user = input("Please input your user that you've chosen when creating the account:\n")
            fetch = app_db.child(user).get()
            print(f"Noice \n{fetch.val()}")
        except:
            print(colored("Invalid Email or Password", 'red'))


def account_creation():  # Displaying the UI function after the login UI
    creation = CreateAcc()
    widget.addWidget(creation)
    widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QtWidgets.QMainWindow):
    def __init__(self):
        super(CreateAcc, self).__init__()
        uic.loadUi("newcreation.ui", self)
        self.button = self.findChild(QtWidgets.QPushButton, 'Naccount')
        self.button.clicked.connect(self.new_account)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def new_account(self):
        email = self.email.text()
        password = self.password.text()
        try:
            app_auth.create_user_with_email_and_password(email, password)
            print(colored(f"Successfully created acc with > \nEmail: {email} \nPassword: {password}", 'green'))
            new_info()
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except:
            print(colored("Email already Exists", 'red'))
            print(colored("Choose Another", 'yellow'))


def new_info():  # A function asking the user to input the data
    user = input(colored(f"User:", 'blue'))
    fullname = input(colored(f"FullName:", 'blue'))
    age = input(colored(f"Age:", 'blue'))
    email = input(colored(f"Email:", 'blue'))
    ssn = input(colored(f"SSN:", 'blue'))
    data = {"Fullname": fullname, "Age": age, "Email": email, "SSN": ssn}
    app_db.child(user).set(data)  # Setting a the data under the user's name.
    app_db.push(data)  # Upload the data to the database
    print(colored(f"Information add to your account successfully.", 'cyan'))

    fetch = app_db.child(user).get()  # To be able to fetch and display the data.
    while True:
        request = input("Would you like to display your data?\ny/n ")
        if request == "y":
            print(f"\nNOICE \n{fetch.val()}")
            break
        elif request == "n":
            print("COOL COOL COOL. See ya")
            break
        else:
            print(colored(f"-_- Invalid Input There BUD. TRY AGAIN", 'red'))


#  Pyqt5 application execution
app = QtWidgets.QApplication(sys.argv)
page = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(page)
widget.setFixedWidth(450)
widget.setFixedHeight(550)
widget.show()
app.exec_()
