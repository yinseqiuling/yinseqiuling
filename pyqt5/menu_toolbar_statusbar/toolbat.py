'''
创建和使用工具栏
工具栏默认按钮：只显示图标，将文本作为悬停提示展示
工具栏按钮有三种显示状态：
1、只显示图标
2、只显示文本
3、同时显示文本和图标

'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget


class toolBar(QMainWindow):
    def __init__(self):
        super(toolBar, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("工具栏使用")
        self.resize(300, 500)

        tb1 = self.addToolBar("file")
        new = QAction(QIcon('./image/baidu.png'), 'new', self)
        tb1.addAction(new)

        open = QAction(QIcon('./image/baidu1.png'), 'open', self)
        tb1.addAction(open)
        # tb1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        tb1.actionTriggered.connect(self.toolbtnpressed)

        tb2 = self.addToolBar('file2')
        new1 = QAction(QIcon('./image/baidu.png'), '新建', self)
        tb2.addAction(new1)
        tb2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        tb2.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self, a):
        print("按下的工具按钮时：", a.text())


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = toolBar()
    mainWindows.show()

    sys.exit(app.exec_())
