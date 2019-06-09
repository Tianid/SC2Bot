import sys
import threading
import queue
import time
from threading import Thread
from typing import Optional, Callable, Any, Iterable, Mapping

import psycopg2

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class W(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        self.content = QWidget()
        scroll.setWidget(self.content)
        self.lay = QVBoxLayout(self.content)
        self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
        self.setStyleSheet("QScrollArea{min-width:500 px; min-height: 200px}")
        self.show()


    def add(self, string):
        self.lay.addWidget(QLabel(string, self))

    @pyqtSlot(str)
    def handleSuperDupa(self, input_string):
        self.add(input_string)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = W()
    gui.add("kek")
    gui.add("kek")
    sys.exit(app.exec_())


