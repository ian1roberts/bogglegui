"""Application wrapper for boggle-gui."""
import sys
from os import path
from PyQt5 import QtWidgets, uic

HERE = path.dirname(__file__)
qtCreatorFile = path.join(HERE, "src", "bogglegui.ui")
print(qtCreatorFile)

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
