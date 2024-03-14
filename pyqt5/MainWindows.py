import sys

import first

from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    # 创建主窗体应用
    app = QApplication(sys.argv)

    mainWindows = QMainWindow()

    ui = first.Ui_MainWindow()

    ui.setupUi(mainWindows)

    mainWindows.show()

    sys.exit(app.exec_())
