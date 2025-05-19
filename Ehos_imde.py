from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QListWidget
from PyQt5 import uic
import sys
import sqlite3
from Ehos_ok import Ui_Dialog  # Adjust the import based on your file structure
from Ehos_nok import Ui_NDialog  # Adjust the import based on your file structure
from Ehos_main import UI_Main  # Assuming this is a QMainWindow or similar

# Create a database or connect to one
conn = sqlite3.connect('/home/mahdi/allpro/hospitall/da/1/hospital.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE if not exists department(
          part integer,  
          name text)""")

conn.commit()
conn.close()

class UI_DeptmentWindow(QMainWindow):
    def __init__(self):  # Corrected method name to __init__
        super(UI_DeptmentWindow, self).__init__()  # Corrected superclass initialization
        self.center()  # Call to center method
        self.count = 0
        # Load the ui file
        uic.loadUi("Ehos_imde.ui", self)
        # --------------------------------------------
        self.line_name = self.findChild(QLineEdit, "line_name")
        self.line_part = self.findChild(QLineEdit, "line_part")

        # self.list = self.findChild(QListWidget, "list_display")
        self.button_save = self.findChild(QPushButton, "but_save")  
        self.button_home = self.findChild(QPushButton, "but_home")
        self.button_bake = self.findChild(QPushButton, "but_bake")

        # Connect button clicks to methods
        self.button_save.clicked.connect(self.clicker_save)
        self.button_home.clicked.connect(self.clicker_home)
        self.button_bake.clicked.connect(self.clicker_bake)
                
        self.show()
    # --------------------------------------------
    def clicker_save(self):
        # Get values from line edits
        name = self.line_name.text()
        part = self.line_part.text()
        
        
        if (name == "" or part == ""):
            # self.list.clear()  # Clear previous items
            # self.list.addItem("Fill the table")  # Notify user to fill the table
            self.count += 1
            if self.count == 1:
                self.openNDialog()  # Open the NDialog
            else:
                self.count = 0
        else:     
            conn = sqlite3.connect('/home/mahdi/allpro/hospitall/da/1/hospital.db')  # Use the full path
            cur = conn.cursor()
            insert_to_tab = """INSERT INTO department
                        (part, name)
                        VALUES (?, ?);"""  # Fixed column name


            # Execute the insert statement with the values
            cur.execute(insert_to_tab, (int(part), name))

            conn.commit()
            cur.close()
            conn.close()
            self.openDialog()

            # Clear the input fields
            self.line_part.setText("")
            self.line_name.setText("")
            print("Data saved successfully") 
            self.count += 1

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

    def openNDialog(self):
        print("openNDialog called")
        self.window = QtWidgets.QDialog()  # Create a dialog instance
        self.ui = Ui_NDialog()  # Create an instance of the dialog's UI class
        self.ui.setupUi(self.window)  # Set up the dialog's UI
        self.window.exec_()  # Use exec_() to open as a modal dialog

    def openWindow(self):
        self.window = UI_Main()  # Create an instance of the main window
        self.window.show()  # Show the window (no exec_ needed for QMainWindow)

    def openImportWindow(self):
        from Ehos_im import UI_ImportWindow  # Local import to avoid circular import
        self.window = UI_ImportWindow()  # Create an instance of the main window
        self.window.show()  # Show the window (no exec_ needed for QMainWindow)

    def clicker_bake(self):
        # Open dialog for admission
        self.openImportWindow()
        self.close()  # Close the current window when opening the main window

    def clicker_home(self):
        # Open main window
        self.openWindow()
        self.close()  # Close the current window when opening the main window

# Initialize The App
if __name__ == "__main__":  # Corrected check to ensure this runs only when executed directly
    app = QApplication(sys.argv)
    UIWindow = UI_DeptmentWindow()  # Create an instance of UI_AdmisionWindow
    sys.exit(app.exec_())  # Properly exit the application
