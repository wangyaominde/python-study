# -*- coding: utf-8 -*-
import time
import xlrd
import xlwt
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class LineEditEx(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(None, parent)
        self.setGeometry(50, 50, 100, 20)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)  # 開啟可拖放事件


    def dragEnterEvent(self, QDragEnterEvent):
        e = QDragEnterEvent  # type:QDragEnterEvent
        print('type:', e.type())  # 事件的類型
        print('pos:', e.pos())  # 拖放位置
        print(e.mimeData().urls())  # 文檔所有的路徑
        print(e.mimeData().text())  # 文檔路徑
        print(e.mimeData().formats())  # 支持的所有格式
        print(e.mimeData().data('text/plain'))  # 根據mime類型取路徑 值為字節數組
        print(e.mimeData().hasText())  # 是否支持文本文檔格式
        
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.mimeData().text()) #如果之前設置ignore 為False 這裏將不會生效

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUi()

    def setUi(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('将excel文件拖入对话框')
        self.textEdit = LineEditEx(self)

        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
