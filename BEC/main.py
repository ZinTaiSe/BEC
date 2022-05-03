import design as d
import sys


if __name__ == '__main__':
    app = d.QApplication(sys.argv)
    MainWindow = d.MainWindow("БЭСК. Техническое обслуживание и ремонт", 500, 300, 800, 400, "img/besk.jpg")
    TitleWindow = d.TitleWindow("БЭСК", 600, 400, 600, 300, "admin", "123", "img/besk.jpg", MainWindow)
    TitleWindow.show()
    sys.exit(app.exec_())
