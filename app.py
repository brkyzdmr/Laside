import sys, sqlite3, re, string
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLineEdit, QInputDialog
from main_screen import  Ui_MainScreen
from save_word_screen import Ui_SaveWordScreen
from dictionary_screen import  Ui_DictionaryScreen
from settings_screen import Ui_SettingsScreen
from signin_screen import Ui_SignInScreen
import pyrebase

class MainScreen(QMainWindow):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent=parent)
        self.ui = Ui_MainScreen()
        self.ui.setupUi(self)
        self.show()
    def btn_saveword_clicked(self):
        window = SaveWordScreen(self)
        window.show()
        self.hide()
    def btn_dictionary_clicked(self):
        print(" Clicked!")
        window = DictionaryScreen(self)
        window.show()
        self.hide()
    def btn_settings_clicked(self):
        window = SettingsScreen(self)
        window.show()
        self.hide()

class SaveWordScreen(QMainWindow):
    def __init__(self, parent=None):
        super(SaveWordScreen, self).__init__(parent=parent)
        self.ui = Ui_SaveWordScreen()
        self.ui.setupUi(self)
    def btn_back_clicked(self):
        window = MainScreen(self)
        window.show()
        self.hide()
    def btn_save_clicked(self):
        print("Save clicked!")
        word = self.ui.tb_word.text()
        meaning = self.ui.tb_meaning.toPlainText()

        test_word = re.sub('[^A-Za-z]+', '', word)
        test_meaning = re.sub('[^A-Za-z]+', '', meaning)
        if test_word != "" and test_meaning != "":
            print(test_word + ", " + test_meaning)
            word.lower()
            meaning.lower()
            meaning_words = meaning.split(",")

            data = {
                "word": word,
                "meaning": meaning_words
            }
            
            fb_con = firebase.FirebaseApplication("https://laside-6b158.firebaseio.com/", None)
            result = fb_con.post("/users/user2", data)
            print(result)      

class DictionaryScreen(QMainWindow):
    def __init__(self, parent=None):
        super(DictionaryScreen, self).__init__(parent=parent)
        self.ui = Ui_DictionaryScreen()
        self.ui.setupUi(self)
    def btn_back_clicked(self):
        window = MainScreen(self)
        window.show()
        self.hide()

class SettingsScreen(QMainWindow):
    def __init__(self, parent=None):
        super(SettingsScreen, self).__init__(parent=parent)
        self.ui = Ui_SettingsScreen()
        self.ui.setupUi(self)
    def btn_signin_clicked(self):
        print("sign-in")
        window = SignInScreen(self)
        window.show()
        self.hide()
    def btn_signup_clicked(self):
        print("sign-up")
    def btn_back_clicked(self):
        window = MainScreen(self)
        window.show()
        self.hide()

class SignInScreen(QMainWindow):
    def __init__(self, parent=None):
        super(SignInScreen, self).__init__(parent=parent)
        self.ui = Ui_SignInScreen()
        self.ui.setupUi(self)
        self.ui.tb_password.setEchoMode(QLineEdit.Password)
    def btn_signin_clicked(self):
        email = self.ui.tb_email.text()
        password = self.ui.tb_password.text()

        email = re.sub(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', '', email)
        
        if email != "" and password != "":
            fb_con = firebase.initialize_app("https://laside-6b158.firebaseio.com/", None)
            auth = firebase.auth()

            try:
                user = auth.sign_in_with_email_and_password(email, password)
                print(user)  
            except:
                print("Fail!")
            
    def btn_signup_clicked(self): 
        print("signup!")
    def btn_back_clicked(self):
        window = SettingsScreen(self)
        window.show()
        self.hide()

def main():
    app = QApplication(sys.argv)
    window = MainScreen()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()