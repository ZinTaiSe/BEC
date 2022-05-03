from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QMessageBox,
                             QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit)
from PyQt5.QtCore import Qt
from PyQt5.Qt import QPixmap
from PyQt5.QtGui import QFont
import style as s
import webbrowser
import main as m
import sys


class App(QWidget):
    def __init__(self, title, left, top, width, height):
        super().__init__()
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.main_initUI()

    def main_initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        # self.setStyleSheet(s.background)
        self.hide()


class TitleWindow(App):
    def __init__(self, title, left, top, width, height, login, password, path, main_win):
        super().__init__(title, left, top, width, height)

        self.keyLogin = login
        self.keyPassword = password
        self.main_win = main_win

        self.v_line = QVBoxLayout()
        self.h1_line = QHBoxLayout()
        self.h2_line = QHBoxLayout()

        self.logo = QLabel()
        self.pixmap = QPixmap(path).scaled(self.logo.width()-300, self.logo.height(), Qt.KeepAspectRatio)
        self.heading = QLabel("Введите данные:", self)
        self.login_l = QLabel("Логин:", self)
        self.password_l = QLabel("Пароль:", self)
        self.login = QLineEdit(self)
        self.password = QLineEdit(self)
        self.button = QPushButton("Войти", self)
        self.button.clicked.connect(self.clicked)
        self.initUI()

    def initUI(self):
        # self.logo.setStyleSheet(s.logo)
        self.logo.setPixmap(self.pixmap)

        self.heading.setStyleSheet(s.q_text_style)
        self.login.setFixedSize(400, 50)
        self.login_l.setFont(QFont("Times font", 18))
        self.password.setFixedSize(400, 50)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_l.setFont(QFont("Arial font", 18))
        self.button.setStyleSheet(s.enter_button)

        self.setLayout(self.v_line)
        self.v_line.addWidget(self.logo, alignment=Qt.AlignCenter, stretch=3)
        self.v_line.addWidget(self.heading, alignment=Qt.AlignCenter, stretch=1)
        self.v_line.addLayout(self.h1_line)
        self.v_line.addLayout(self.h2_line)
        self.v_line.addWidget(self.button)
        self.h1_line.addWidget(self.login_l, alignment=Qt.AlignCenter)
        self.h1_line.addWidget(self.login)
        self.h2_line.addWidget(self.password_l, alignment=Qt.AlignCenter)
        self.h2_line.addWidget(self.password)

    def clicked(self):
        login = self.login.text()
        password = self.password.text()

        if (login == self.keyLogin) and (password == self.keyPassword):
            self.hide()
            self.main_win.show()
        else:
            self.heading.setText("Логин или пароль введены неверно!")
            self.login.setText("")
            self.password.setText("")


class MainWindow(App):
    def __init__(self, title, left, top, width, height, path):
        super().__init__(title, left, top, width, height)

        self.h_line = QHBoxLayout()
        self.h0_line = QHBoxLayout()
        self.h1_line = QHBoxLayout()
        self.h2_line = QHBoxLayout()
        self.v_line_left = QVBoxLayout()
        self.v_line_right = QVBoxLayout()

        self.logo = QLabel()
        self.pixmap = QPixmap(path).scaled(self.logo.width()-300, self.logo.height(), Qt.KeepAspectRatio)

        self.but_info = QPushButton("INFO")
        self.but_profile = QPushButton("Личный \nкабинет")
        self.but_data = QPushButton("Данные")
        self.but_calc = QPushButton("Калькулятор")
        self.but_mail = QPushButton("Обратная \n связь")
        self.buttons = [self.but_profile, self.but_data, self.but_calc, self.but_mail]

        self.alert = QMessageBox()
        self.msg = QMessageBox()

        self.initUI()

    def initUI(self):
        self.logo.setPixmap(self.pixmap)
        self.setStyleSheet(s.main_window)

        self.alert.setIcon(QMessageBox.Critical)
        self.alert.setText("Бета версия")
        self.alert.setInformativeText(s.alert_text)
        self.alert.setWindowTitle("Проект")

        self.msg.setText("Справочная информация")
        self.msg.setInformativeText(s.info_text)
        self.msg.setWindowTitle("Справка")

        self.but_info.setStyleSheet(s.info_button)
        for button in self.buttons:
            button.setFixedSize(120, 80)
            button.setStyleSheet(s.main_buttons)

        self.setLayout(self.h_line)
        self.h_line.addLayout(self.v_line_left, stretch=6)
        self.h_line.addLayout(self.v_line_right, stretch=5)
        self.v_line_left.addLayout(self.h0_line)
        self.v_line_left.addLayout(self.h1_line)
        self.v_line_left.addLayout(self.h2_line)
        self.v_line_right.addWidget(self.logo)
        self.h0_line.addWidget(self.but_info, alignment=Qt.AlignLeft)
        self.h1_line.addWidget(self.but_profile, alignment=Qt.AlignCenter)
        self.h1_line.addWidget(self.but_data, alignment=Qt.AlignCenter)
        self.h2_line.addWidget(self.but_calc, alignment=Qt.AlignCenter)
        self.h2_line.addWidget(self.but_mail, alignment=Qt.AlignCenter)

        self.but_info.clicked.connect(self.info)
        self.but_profile.clicked.connect(self.test)
        self.but_data.clicked.connect(self.test)
        self.but_calc.clicked.connect(self.test)
        self.but_mail.clicked.connect(self.butMail)

    @staticmethod
    def butMail():
        webbrowser.open("https://mail.google.com/")

    def test(self):
        self.alert.exec_()

    def info(self):
        self.msg.exec_()

