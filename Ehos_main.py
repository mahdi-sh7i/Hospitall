from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys
from Ehos_ok import Ui_Dialog  # Adjust the import based on your file structure

class UI_Main(QMainWindow):
    def __init__(self):  # Corrected method name to __init__
        super(UI_Main, self).__init__()  # Corrected superclass initialization
        self.center()  # Call to center method
        # Load the UI file
        uic.loadUi("Ehos_main.ui", self)
        # --------------------------------------------
        self.button_admission = self.findChild(QPushButton, "but_admission")
        self.button_archive = self.findChild(QPushButton, "but_archive")

        # Connect button clicks to methods
        self.button_admission.clicked.connect(self.clicker_admission)
        self.button_archive.clicked.connect(self.clicker_archive)

        # Show The App
        self.show()
    # --------------------------------------------

    def center(self):
        """Center the window on the screen."""
        qr = self.frameGeometry()  # Get the frame geometry of the window
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()  # Get the center of the screen
        qr.moveCenter(cp)  # Move the rectangle to the center of the screen
        self.move(qr.topLeft())  # Move the top-left corner of the window to the top-left of the rectangle

    def openDialog(self):
        self.window = QtWidgets.QDialog()  # Create a dialog instance
        self.ui = Ui_Dialog()  # Create an instance of the dialog's UI class
        self.ui.setupUi(self.window)  # Set up the dialog's UI
        self.window.exec_()  # Use exec_() to open as a modal dialog

    def openAdmisionWindow(self):
        from Ehos_ajns import UI_AdmisionWindow  # Local import to avoid circular import
        self.window = UI_AdmisionWindow()  # Create an instance of the admission window
        self.window.show()  # Show the window (no exec_ needed for QMainWindow)

    def openArchiveWindow(self):
        from Ehos_arch import UI_ArchiveWindow  # Local import to avoid circular import
        self.window = UI_ArchiveWindow()  # Create an instance of the archive window
        self.window.show()  # Show the window (no exec_ needed for QMainWindow)

    def clicker_admission(self):
        # Open dialog for admission
        self.openAdmisionWindow()
        self.close()  # This will close the current window

    def clicker_archive(self):
        # Open archive window
        self.openArchiveWindow()
        self.close()  # This will close the current window

# Initialize The App
if __name__ == "__main__":  # Corrected check to ensure this runs only when executed directly
    app = QApplication(sys.argv)
    UIWindow = UI_Main()
    sys.exit(app.exec_())  # Properly exit the application
