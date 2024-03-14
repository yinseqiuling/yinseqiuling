'''
弧形
圆形
椭圆
矩形（正方形）
多边形
绘制图像

'''
import sys
import math
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class DrawAll(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.resize(300, 600)
        self.setWindowTitle("绘制各类图形")

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.blue)

        # 绘制弧形
        rect = QRect(0, 10, 100, 100)
        qp.drawArc(rect, 0, 45*16)  # 第三个参数alen：1个alen等于1/16度

        # 通过弧绘制圆
        qp.setPen(Qt.red)
        qp.drawArc(120, 10, 100, 100, 0, 360*16)

        # 绘制带弦的弧形

        qp.drawChord(10, 120, 100, 100, 12, 120*16)

        # 绘制扇形
        qp.drawPie(10, 240, 100, 100, 15, 120*16)

        #  绘制椭圆
        qp.drawEllipse(120, 120, 150, 90)

        # 绘制多边形(5边)
        point1 = QPoint(140, 380)
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)
        polygon = QPolygon([point1, point2, point3, point4, point5])
        qp.drawPolygon(polygon)

        # 绘制图像
        image = QImage('./image/baidu1.png')
        rect1 = QRect(100, 400, int(image.width()/2), int(image.height()/2))
        qp.drawImage(rect, image)

        qp.end()


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = DrawAll()
    mainWindows.show()

    sys.exit(app.exec_())
