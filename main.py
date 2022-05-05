import design as d
import sys


if __name__ == '__main__':
    app = d.QApplication(sys.argv)
    DataWindow = d.DataWindow("Данные", 700, 200, 400, 600)
    MainWindow = d.MainWindow("БЭСК. Техническое обслуживание и ремонт", 500, 300, 800, 400, "img/besk.jpg", DataWindow)
    TitleWindow = d.TitleWindow("БЭСК", 600, 400, 600, 300, "admin", "123", "img/besk.jpg", MainWindow)
    TitleWindow.show()
    sys.exit(app.exec_())
