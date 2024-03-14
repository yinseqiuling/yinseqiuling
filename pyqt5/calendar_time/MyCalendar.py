'''
日历控件
QCalendarWidget

'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUi()

    def initUi(self):
        self.cal = QCalendarWidget(self)
        self.cal.resize(600, 600)
        self.cal.setMinimumDate(QDate(1994, 8, 29))
        self.cal.setMaximumDate(QDate(2080, 8, 29))
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked.connect(self.showData)
        self.setWindowTitle("日历")

        self.label = QLabel(self)
        data = self.cal.selectedDate()
        self.label.setText(data.toString("yyyy-MM-dd dddd"))
        self.label.move(20, 300)

    def showData(self, data):
        self.label.setText(data.toString("yyyy-MM-dd dddd"))


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = MyCalendar()
    mainWindows.show()

    sys.exit(app.exec_())
