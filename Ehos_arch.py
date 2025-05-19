from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import uic
import sys
from Ehos_ok import Ui_Dialog  # Adjust the import based on your file structure
from Ehos_main import UI_Main  # Assuming this is a QMainWindow or similar

class UI_ArchiveWindow(QMainWindow):
    def __init__(self):  # Corrected method name to __init__
        super(UI_ArchiveWindow, self).__init__()  # Corrected superclass initialization
        self.center()  # Call to center method
        # Load the ui file
        uic.loadUi("Ehos_arch.ui", self)
        # -------------------------------------------- 
        self.button_home = self.findChild(QPushButton, "but_home")
        self.button_import = self.findChild(QPushButton, "but_import") 
        self.button_extraction = self.findChild(QPushButton, "but_extraction") 

        # Connect button clicks to methods
        self.button_home.clicked.connect(self.clicker_home)
        self.button_import.clicked.connect(self.clicker_import)
        self.button_extraction.clicked.connect(self.clicker_extraction)

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

    def openWindow(self):
        self.window = UI_Main()  # Create an instance of the main window
        self.window.show()  # Show the window (no exec_ needed for QMainWindow)

    def openImportWindow(self):
        from Ehos_im import UI_ImportWindow  # Local import to avoid circular import
        self.window = UI_ImportWindow()  # Create an instance of the main window
        self.window.show()  # Show the window (no exec_ needed for QMainWindow) Extraction

    def openExtractiontWindow(self):
        from Ehos_di import UI_ExtractionWindow  # Local import to avoid circular import
        self.window = UI_ExtractionWindow()  # Create an instance of the main window
        self.window.show()  # Show the window (no exec_ needed for QMainWindow) Extraction
   
    def clicker_import(self):
        # Open dialog for admission
        self.openImportWindow()
        self.close()  # Close the current window when opening the main window

    def clicker_extraction(self):
        self.openExtractiontWindow()
        self.close()  # Close the current window when opening the main window

    def clicker_home(self):
        # Open main window
        self.openWindow()
        self.close()  # Close the current window when opening the main window

# Initialize The App
if __name__ == "__main__":  # Corrected check to ensure this runs only when executed directly
    app = QApplication(sys.argv)
    UIWindow = UI_ArchiveWindow()  # Create an instance of UI_AdmisionWindow
    sys.exit(app.exec_())  # Properly exit the application
