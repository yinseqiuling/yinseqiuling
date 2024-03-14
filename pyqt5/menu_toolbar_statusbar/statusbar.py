'''
状态栏的创建和使用



'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget


class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("状态栏使用")
        self.resize(600, 500)

        bar = self.menuBar()

        file = bar.addMenu("file")
        file.addAction("show")
        file.triggered.connect(self.processTriggered)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def processTriggered(self, a):
        if a.text() == "show":
            self.statusBar.showMessage(a.text()+"cilcked", 5000)


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = StatusBar()
    mainWindows.show()

    sys.exit(app.exec_())
