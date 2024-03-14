'''
1、绘制直线，设置完样式以后要设置一次画笔setPen()

'''
import sys
import math
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.resize(300, 200)
        self.setWindowTitle("设置Pen颜色")

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # painter.setPen(Qt.color)
        pen = QPen(Qt.red, 3, Qt.SolidLine)

        # 默认实线，不需要设置
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        # 设置虚线
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        # 设置点划线
        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 100, 250, 100)

        # 设置粗的点划线
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        # 自定义线型
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([2, 8, 2, 8])
        painter.setPen(pen)
        painter.drawLine(20, 140, 250, 140)

        painter.end()


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = DrawMultiLine()
    mainWindows.show()

    sys.exit(app.exec_())
