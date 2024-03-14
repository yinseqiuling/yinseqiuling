'''
让控件支持拖拽动作
A.setDragEnable(True)
B.setAcceptDrops(True)

B需要2个事件
1、dragEnterEvent 将A拖到B触发
2、dropEvent   在B区域放下A时触发事件



'''
import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class MyConboBox(QComboBox):
    def __init__(self):
        super(MyConboBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())


class DragDropDemo(QWidget):
    def __init__(self):
        super(DragDropDemo, self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel("请将左边文本拖拽到右边的下拉列表中"))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)  # 让控件QLineEdit可拖动

        combox = MyConboBox()
        formLayout.addRow(lineEdit, combox)
        self.setLayout(formLayout)
        self.setWindowTitle("拖拽案例")


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = DragDropDemo()
    mainWindows.show()

    sys.exit(app.exec_())
