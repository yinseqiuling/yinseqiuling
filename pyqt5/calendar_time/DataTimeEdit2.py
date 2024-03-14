''''
日历的高级用法
QDataTimeEdit

'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class DataTimeEdit1(QWidget):
    def __init__(self):
        super(DataTimeEdit1, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("设置不同风格的日期和时间")
        self.resize(300, 100)
        vlayout = QVBoxLayout()
        dataTimeEdit1 = QDateTimeEdit()
        dataTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        # dataTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dataTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))

        dataTimeEdit1.dateChanged.connect(self.onDataChanged)
        dataTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dataTimeEdit1.dateTimeChanged.connect(self.onTimeChanged)

        dataTimeEdit2.setCalendarPopup(True)

        dataEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dataTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dataTimeEdit2.setDisplayFormat("yyyy/MM/dd HH:mm:ss")
        dataEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:sss")
        self.btn = QPushButton('获取当前时间和日期')
        self.btn.clicked.connect(self.onButtonClick)

        self.dataTimeEdit = dataTimeEdit1

        vlayout.addWidget(dataTimeEdit1)
        vlayout.addWidget(dataTimeEdit2)
        vlayout.addWidget(dataEdit)
        vlayout.addWidget(timeEdit)
        vlayout.addWidget(self.btn)

        self.setLayout(vlayout)

    def onDataChanged(self, data):
        print(data)

    def onTimeChanged(self, time):
        print(time)

    def onDataTimeChanged(self, datatime):
        print(datatime)

    def onButtonClick(self):
        dataTime = self.dataTimeEdit.dateTime()
        print(dataTime)


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = DataTimeEdit1()
    mainWindows.show()

    sys.exit(app.exec_())
