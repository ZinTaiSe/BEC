import webbrowser
import time

from PyQt5.Qt import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QWidget, QLabel, QMessageBox, QApplication, QProgressBar,
                             QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget)

import db, sys
import style as s


class App(QWidget):
    def __init__(self, title, left, top, width, height):
        super().__init__()
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.icon = QIcon("img/key.jpg")
        self.main_initUI()

    def main_initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(self.icon)
        self.hide()


class TitleWindow(App):
    def __init__(self, title, left, top, width, height, key, path, main_win):
        super().__init__(title, left, top, width, height)

        self.keyLogin = key[0][0]
        self.keyPassword = key[0][1]
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
        self.progressbar = QProgressBar()
        self.initUI()

    def initUI(self):
        self.logo.setPixmap(self.pixmap)
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        self.progressbar.setFixedSize(600, 20)

        self.heading.setStyleSheet(s.q_text_style)
        self.login.setFixedSize(400, 40)
        self.login_l.setFont(QFont("Times font", 18))
        self.password.setFixedSize(400, 40)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_l.setFont(QFont("Arial font", 18))
        self.button.setStyleSheet(s.enter_button)
        self.button.clicked.connect(self.clicked)

        self.setLayout(self.v_line)
        self.v_line.addWidget(self.logo, alignment=Qt.AlignCenter, stretch=3)
        self.v_line.addWidget(self.heading, alignment=Qt.AlignCenter, stretch=1)
        self.v_line.addLayout(self.h1_line)
        self.v_line.addLayout(self.h2_line)
        self.v_line.addWidget(self.progressbar, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.button)
        self.h1_line.addWidget(self.login_l, alignment=Qt.AlignCenter)
        self.h1_line.addWidget(self.login)
        self.h2_line.addWidget(self.password_l, alignment=Qt.AlignCenter)
        self.h2_line.addWidget(self.password)

    def clicked(self):
        login = self.login.text()
        password = self.password.text()

        if (login == self.keyLogin) and (password == self.keyPassword):
            for i in range(100):
                time.sleep(0.01)
                self.progressbar.setValue(i+1)

            self.hide()
            self.main_win.show()
        else:
            self.heading.setText("Логин или пароль введены неверно!")
            self.login.setText("")
            self.password.setText("")


class MainWindow(App):
    def __init__(self, title, left, top, width, height, path, data_win, person_win):
        super().__init__(title, left, top, width, height)

        self.h_line = QHBoxLayout()
        self.h0_line = QHBoxLayout()
        self.h1_line = QHBoxLayout()
        self.h2_line = QHBoxLayout()
        self.v_line_left = QVBoxLayout()
        self.v_line_right = QVBoxLayout()

        self.logo_sign = QLabel("Последняя неполадка: \n")
        self.logo = QLabel()
        self.pixmap = QPixmap(path).scaled(self.logo.width()-300, self.logo.height(), Qt.KeepAspectRatio)

        self.but_info = QPushButton("INFO")
        self.but_profile = QPushButton("Личный \nкабинет")
        self.but_data = QPushButton("Данные")
        self.but_calc = QPushButton("Калькулятор")
        self.but_mail = QPushButton("Обратная \n связь")
        self.buttons = [self.but_profile, self.but_data, self.but_calc, self.but_mail]

        self.data_win = data_win
        self.person_win = person_win
        self.alert = QMessageBox()
        self.msg = QMessageBox()
        self.link_button = None

        self.initUI()
        self.show_image()

    def initUI(self):
        self.but_info.setStyleSheet(s.info_button)
        self.logo_sign.setStyleSheet(s.logo_sign)
        self.logo.setMaximumSize(400, 500)
        self.logo.setPixmap(self.pixmap)
        self.setStyleSheet(s.main_window)

        self.alert.setIcon(QMessageBox.Critical)
        self.alert.setText("Бета версия")
        self.alert.setInformativeText(s.alert_text)
        self.alert.setWindowTitle("Проект")

        self.msg.setText("Справочная информация")
        self.msg.setInformativeText(s.info_text)
        self.msg.setWindowTitle("Справка")
        self.msg.addButton(QMessageBox.Ok)
        self.link_button = self.msg.addButton("changelogs", QMessageBox.YesRole)
        self.link_button.clicked.connect(self.go_to_changelog)

        for button in self.buttons:
            button.setFixedSize(120, 80)
            button.setStyleSheet(s.main_buttons)

        self.setLayout(self.h_line)
        self.h_line.addLayout(self.v_line_left, stretch=6)
        self.h_line.addLayout(self.v_line_right, stretch=3)
        self.v_line_left.addLayout(self.h0_line)
        self.v_line_left.addLayout(self.h1_line)
        self.v_line_left.addLayout(self.h2_line)
        self.v_line_right.addWidget(self.logo_sign, stretch=2)
        self.v_line_right.addWidget(self.logo, stretch=8)
        self.h0_line.addWidget(self.but_info, alignment=Qt.AlignLeft)
        self.h1_line.addWidget(self.but_profile, alignment=Qt.AlignCenter)
        self.h1_line.addWidget(self.but_data, alignment=Qt.AlignCenter)
        self.h2_line.addWidget(self.but_calc, alignment=Qt.AlignCenter)
        self.h2_line.addWidget(self.but_mail, alignment=Qt.AlignCenter)

        self.but_info.clicked.connect(self.info)
        self.but_profile.clicked.connect(self.profile)
        self.but_data.clicked.connect(self.data)
        self.but_calc.clicked.connect(self.test)
        self.but_mail.clicked.connect(self.butMail)

    def show_image(self):
        self.pixmap = QPixmap(db.sort_by_date()[0][3])
        self.pixmap = self.pixmap.scaled(self.logo.width(), self.logo.height())
        self.logo.setPixmap(self.pixmap)
        self.logo_sign.setText("Последние неполадки: \n" + db.sort_by_date()[0][1] + " (" + db.sort_by_date()[0][4] + ")")

    @staticmethod
    def butMail():
        webbrowser.open("https://mail.google.com/")

    @staticmethod
    def go_to_changelog():
        webbrowser.open("https://github.com/ZinTaiSe/BEC/blob/main/changelog.txt")

    def data(self):
        self.data_win.show()

    def profile(self):
        self.person_win.show()

    def test(self):
        self.alert.exec_()

    def info(self):
        self.msg.exec_()


class DataWindow(App):
    def __init__(self, title, left, top, height, width):
        super().__init__(title, left, top, height, width)

        self.main_v_line = QVBoxLayout()
        self.bottom_h_line = QHBoxLayout()

        self.info = QLabel("Отсортируйте список")
        self.image = QLabel()
        self.pixmap = QPixmap("no_image.jpg")
        self.button = QPushButton("Назад")
        self.button_sort_by_date = QPushButton("Сортировка \nпо дате")
        self.button_sort_by_person = QPushButton("Сортировка \nпо исполнителю")
        self.data_list = QListWidget()
        self.sort_type = db.sort_by_date()
        self.initUI()

    def initUI(self):
        self.data_list.itemClicked.connect(self.show_image)
        self.info.setStyleSheet(s.logo)
        self.image.setMinimumSize(350, 300)
        self.image.setMaximumSize(380, 300)
        self.pixmap = self.pixmap.scaled(self.image.width(), self.image.height())
        self.image.setPixmap(self.pixmap)

        self.button.setStyleSheet(s.enter_button)
        self.button.clicked.connect(self.back)
        self.button_sort_by_date.setStyleSheet(s.sort_button)
        self.button_sort_by_date.clicked.connect(self.sort_by_date)
        self.button_sort_by_person.setStyleSheet(s.sort_button)
        self.button_sort_by_person.clicked.connect(self.sort_by_person)

        self.main_v_line.addWidget(self.info, stretch=2, alignment=Qt.AlignCenter)
        self.main_v_line.addWidget(self.image, stretch=5)
        self.main_v_line.addWidget(self.data_list, stretch=5)
        self.main_v_line.addLayout(self.bottom_h_line, stretch=2)
        self.bottom_h_line.addWidget(self.button_sort_by_date, stretch=3)
        self.bottom_h_line.addWidget(self.button, stretch=7)
        self.bottom_h_line.addWidget(self.button_sort_by_person, stretch=3)
        self.setLayout(self.main_v_line)

    def back(self):
        self.hide()

    def fill_data(self):
        for item in self.sort_type:
            self.data_list.addItem(item[1] + ", " + item[4])

    def show_image(self):
        name = self.data_list.selectedItems()[0].text().split(", ")[0]

        for item in self.sort_type:
            if name in item[1]:
                self.pixmap = QPixmap(item[3])
                self.pixmap = self.pixmap.scaled(self.image.width(), self.image.height())
                self.image.setPixmap(self.pixmap)
                self.info.setText(item[2])

    def sort_by_date(self):
        self.change_buttons(self.button_sort_by_date, self.button_sort_by_person)
        self.sort_type = db.sort_by_date()
        self.data_list.clear()
        self.info.setText("Выберите объект в списке")
        self.fill_data()

    def sort_by_person(self):
        self.change_buttons(self.button_sort_by_person, self.button_sort_by_date)
        self.sort_type = db.sort_by_person()
        self.data_list.clear()
        self.info.setText("Выберите объект в списке")
        self.fill_data()

    @staticmethod
    def change_buttons(button1: QPushButton, button2: QPushButton):
        button1.setDisabled(True)
        button2.setEnabled(True)
        button1.setStyleSheet(s.not_sort_button)
        button2.setStyleSheet(s.sort_button)


class PersonalWindow(App):
    def __init__(self, title, left, top, height, width, name):
        super().__init__(title, left, top, height, width)

        self.main_v_line = QVBoxLayout()
        self.data = None
        self.label_name = QLabel(name)
        self.label_stage = QLabel("Стаж:   9 лет")
        self.label_job = QLabel("Должность:   Инженер-инспектор")
        self.label_status = QLabel("Статус:   На объекте...")
        self.button = QPushButton("Назад")
        self.data_list = QListWidget()
        self.image = QLabel()
        self.pixmap = QPixmap("no_image.jpg")

        self.fill_data()
        self.initUI()

    def initUI(self):
        self.data_list.itemClicked.connect(self.show_image)
        self.button.clicked.connect(self.back)

        self.image.setMaximumSize(380, 330)
        self.pixmap = self.pixmap.scaled(self.image.width(), self.image.height())
        self.image.setPixmap(self.pixmap)

        self.label_name.setStyleSheet(s.logo_sign)
        self.button.setStyleSheet(s.enter_button)
        self.label_stage.setStyleSheet(s.label_info)
        self.label_job.setStyleSheet(s.label_info)
        self.label_status.setStyleSheet(s.label_info)

        self.main_v_line.addWidget(self.label_name, alignment=Qt.AlignCenter, stretch=2)
        self.main_v_line.addWidget(self.label_stage, stretch=1, alignment=Qt.AlignLeft)
        self.main_v_line.addWidget(self.label_job, stretch=1, alignment=Qt.AlignLeft)
        self.main_v_line.addWidget(self.label_status, stretch=1, alignment=Qt.AlignLeft)
        self.main_v_line.addWidget(self.image, stretch=5)
        self.main_v_line.addWidget(self.data_list, stretch=5)
        self.main_v_line.addWidget(self.button, stretch=2)
        self.setLayout(self.main_v_line)

    def fill_data(self):
        self.data = db.data_for_person(self.label_name)
        for element in self.data:
            self.data_list.addItem(element[1] + ",  " + element[2])

    def show_image(self):
        date = self.data_list.selectedItems()[0].text().split(",  ")[0]
        for item in self.data:
            if date in item[1]:
                self.pixmap = QPixmap(item[3])
                self.pixmap = self.pixmap.scaled(self.image.width(), self.image.height())
                self.image.setPixmap(self.pixmap)

    def back(self):
        self.hide()
