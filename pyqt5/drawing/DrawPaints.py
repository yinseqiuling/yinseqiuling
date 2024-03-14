'''
    绘制曲线用函数值x,y作为参数传递给drawPoint(),注意参数类型不能为浮点，需要为整型

'''

import sys
import math
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class DrawPaints(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.resize(300, 200)
        self.setWindowTitle("在窗口上用像素点绘制2个周期正弦曲线")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()
        for i in range(1000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) *
                               math.pi / 50) + size.height() / 2.0
            painter.drawPoint(int(x), int(y))

        painter.end()


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = DrawPaints()
    mainWindows.show()

    sys.exit(app.exec_())
