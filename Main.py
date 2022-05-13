import design as d
import sys
import db
import os


def start():
    app = d.QApplication(sys.argv)
    DataWindow = d.DataWindow("Данные", 700, 200, 400, 600)
    PersonalWindow = d.PersonalWindow("Личный кабинет", 700, 200, 400, 600, 'Kovalevski A.P.')
    MainWindow = d.MainWindow("БЭСК. Техническое обслуживание и ремонт", 500, 300, 800, 400, "besk.jpg", DataWindow, PersonalWindow)
    TitleWindow = d.TitleWindow("БЭСК", 600, 400, 600, 300, key, "besk.jpg", MainWindow)
    TitleWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    key = [["admin", "123"]]
    if not os.path.exists("energy.db"):
        db.create_some_data()
        db.check_new_data()
    start()
