'''
使用剪切板

'''

import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()

        # 复制文本、HMTL、图像
        textCopyButton = QPushButton("复制文本")
        textPasteButton = QPushButton("粘贴文本")

        htmlCopyButton = QPushButton("复制HTML代码")
        htmlPasteButton = QPushButton("粘贴HTML代码")

        imageCopyButton = QPushButton("复制头像")
        imagePasteButton = QPushButton("粘贴头像")

        self.textLabel = QLabel("默认文本")
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap())

        layout = QGridLayout()
        # 三行三列布局
        # 第一行
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(htmlCopyButton, 0, 1)
        layout.addWidget(imageCopyButton, 0, 2)
        # 第二行
        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(htmlPasteButton, 1, 1)
        layout.addWidget(imagePasteButton, 1, 2)
        # 第三行
        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)

        self.setLayout(layout)

        textCopyButton.clicked.connect(self.copyText)

        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

        self.setWindowTitle("剪切板")

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('hello world')

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('./image/baidu.png'))

    def pasteImage(self):
        print('111')
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())  # 从剪贴板获得图片

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>Html Demo <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimaData = clipboard.mimeData()
        if mimaData.hasHtml():
            self.textLabel.setText(mimaData.html())


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = ClipBoard()
    mainWindows.show()

    sys.exit(app.exec_())
