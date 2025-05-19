from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic  # Ensure you import uic
import sys

class Ui_NDialog(object):
    def setupUi(self, NDialog):
        self.dialog = NDialog  # Store a reference to the dialog

        # Load the ui file
        uic.loadUi("Ehos_nok.ui", self.dialog)  # Pass NDialog to loadUi
        
        # --------------------------------------------
        self.button_close = self.dialog.findChild(QtWidgets.QPushButton, "Button_close")
        self.label = self.dialog.findChild(QtWidgets.QLabel, "label")

        # Connect button clicks to methods
        self.button_close.clicked.connect(self.clicker_close)
        # --------------------------------------------

    def clicker_close(self):
        self.label.setText("close !!!")  # Update label text
        # Close the dialog
        self.dialog.close()  # This will close the dialog

# Initialize The App
if __name__ == "__main__":  # Corrected name check
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_NDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
