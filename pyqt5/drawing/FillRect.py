import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class FillRect(QWidget):
    def __init__(self):
        super(FillRect, self).__init__()
        self.setWindowTitle("用画刷填充区域")
        self.resize(300, 600)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 10, 60, 60)

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 70, 60, 60)

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 130, 60, 60)

        brush = QBrush(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 190, 60, 60)

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 250, 60, 60)
        qp.end()


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = FillRect()
    mainWindows.show()

    sys.exit(app.exec_())
