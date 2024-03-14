import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPaintEngine, QPaintEvent, QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class DrawText(QWidget):
    def __init__(self):
        super(drawText, self).__init__()
        self.setWindowTitle("窗口绘制文本")
        self.resize(300, 200)
        self.text = "这是一个文本"

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        print('aaaa')
        painter.setPen(QColor(153, 43, 5))
        painter.setFont(QFont('Simsum', 25))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        painter.end()


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = DrawText()
    mainWindows.show()

    sys.exit(app.exec_())
