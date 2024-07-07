import sys
from PyQt5 import QtWidgets, QtGui
from widgets.main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowIcon(QtGui.QIcon('resources/icons/Altum.png'))
    main_window.setWindowTitle("Vegetation Index Calculator")
    main_window.setFixedSize(756, 557)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
