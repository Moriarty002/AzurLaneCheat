import sys
import Ui_ALC
from PyQt5 import QtCore, QtGui, QtWidgets
import tools

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()
   ui = Ui_ALC.Ui_AzurLaneCheater()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec_())