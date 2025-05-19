from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic  # Ensure you import uic
import sys
#from main4 import UI

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog  # Store a reference to the dialog

        # Load the ui file
        uic.loadUi("Ehos_ok.ui", self.dialog)  # Pass Dialog to loadUi
        
        # --------------------------------------------
        self.button_close = self.dialog.findChild(QtWidgets.QPushButton, "Button_close")
        #self.button_hide = self.dialog.findChild(QtWidgets.QPushButton, "Button_hide")
        self.label = self.dialog.findChild(QtWidgets.QLabel, "label")

        # Connect button clicks to methods
        self.button_close.clicked.connect(self.clicker_close)
        #self.button_hide.clicked.connect(self.clicker_hide)
        # --------------------------------------------
        #self.label.setText("> j")

    def clicker_close(self):
        self.label.setText("close !!!")  # Update label text
        # Close the dialog
        self.dialog.close()  # This will close the dialog

'''   def clicker_hide(self):
        self.label.setText("hide !!!")  # Update label text
        # Close the dialog
        self.dialog.close()  # This will close the dialog '''

# Initialize The App
if __name__ == "__main__":  # Corrected __name__ check
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
