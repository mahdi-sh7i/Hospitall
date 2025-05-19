from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QListWidget
from PyQt5 import uic
import sys
import sqlite3
from Ehos_ok import Ui_Dialog  # Adjust the import based on your file structure
from Ehos_nok import Ui_NDialog  # Adjust the import based on your file structure
from Ehos_main import UI_Main  # Assuming this is a QMainWindow or similar


class UI_PatientsWindow(QMainWindow):
    def __init__(self):  # Corrected method name to __init__
        super(UI_PatientsWindow, self).__init__()  # Corrected superclass initialization
        self.center()  # Call to center method
        self.count = 0
        # Load the ui file
        uic.loadUi("Ehos_dipa.ui", self)
        # --------------------------------------------
        self.line_patient_code = self.findChild(QLineEdit, "line_patient_code")
        self.line_name = self.findChild(QLineEdit, "line_name")
        self.line_lastname = self.findChild(QLineEdit, "line_lastname")
        self.line_date = self.findChild(QLineEdit, "line_date")
        self.line_gender = self.findChild(QLineEdit, "line_gender")
        self.line_phone = self.findChild(QLineEdit, "line_phone")
        self.line_doctor_code = self.findChild(QLineEdit, "line_docter_code") 
        self.line_part = self.findChild(QLineEdit, "line_part")

        self.list = self.findChild(QListWidget, "list_display")

        self.button_display = self.findChild(QPushButton, "but_display")  
        self.button_home = self.findChild(QPushButton, "but_home")
        self.button_bake = self.findChild(QPushButton, "but_bake")

        # Connect button clicks to methods
        self.button_display.clicked.connect(self.clicker_display)
        self.button_home.clicked.connect(self.clicker_home)
        self.button_bake.clicked.connect(self.clicker_bake)
                    
        
        self.show()
    # --------------------------------------------
    def clicker_display(self):
        self.list.clear()
        # Get values from line edits
        patient = self.line_patient_code.text().strip() # Assuming patient code is a string
        name = self.line_name.text().strip()
        lastname = self.line_lastname.text().strip()
        date = self.line_date.text().strip()
        gender = self.line_gender.text().strip()
        phone = self.line_phone.text().strip() 
        doctor = self.line_doctor_code.text().strip() 
        part = self.line_part.text().strip()

        #############################################
        if (patient == "" and name == "" and lastname == "" and date == "" and gender == "" and phone == "" and doctor == "" and part == ""):
            self.list.addItem("!! عناوین بالا را پر کنید ")
            return             

        conn = sqlite3.connect('/home/mahdi/allpro/hospitall/da/1/hospital.db')  # Use the full path
        cur = conn.cursor()
        cond = []
        val = []

        if patient:
            cond.append("patient_code = ?")  # Corrected to match database column name
            val.append(patient)
        if name:
            cond.append("name LIKE ?")
            val.append(f"{name}%")
        if lastname:
            cond.append("lastname LIKE ?")
            val.append(f"{lastname}%")
        if date:
            cond.append("date = ?")
            val.append(date)
        if gender:
            cond.append("gender LIKE ?")
            val.append(f"{gender}%")
        if phone:
            cond.append("phone = ?")
            val.append(phone)
        if doctor:
            cond.append("doctor = ?")
            val.append(doctor)
        if part:
            cond.append("part = ?")
            val.append(part)


        q = "SELECT * FROM patients WHERE " + " AND ".join(cond) if cond else "SELECT * FROM patients"
        
        nodata = True  # فرض بر این است که داده‌ای وجود ندارد
        try:
            cur.execute(q, val)
            fetchedData = cur.fetchall()

            count = 1
            for row in fetchedData:
                self.list.addItem(
                    #f" شماره :{count} \n کدبیمار : {row[0]} \n "
                    f" کدبیمار : {row[0]} \n "
                    f" نام : {row[1]} \n نام خانوادگی : {row[2]} \n "
                    f" تاریخ : {row[3]} \n  جنسیت : {row[4]} \n"
                    f" تلفن : {row[5]} \n کد دکتر : {row[6]} \n"
                    f" بخش : {row[7]} \n "
                )
                count += 1
                nodata = False

            if nodata:
                self.list.addItem(" عدم تطابق !!")
                
        except Exception as e:
            self.list.addItem(" خطا مجدد اطلاعات را وارد کنید !!")
            print(f"Error: {e}")  # چاپ خطا در کنسول برای عیب‌یابی
        finally:
            cur.close()  # Corrected to close the cursor
            conn.close()
            # Clear the input fields
            self.line_patient_code.setText("")  # Clear patient code field as well
            self.line_name.setText("")
            self.line_lastname.setText("")
            self.line_date.setText("")
            self.line_gender.setText("")
            self.line_phone.setText("") 
            self.line_doctor_code.setText("")
            self.line_part.setText("")

        #############################################

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

    def openExtractionWindow(self): 
        from Ehos_di import UI_ExtractionWindow  # Local import to avoid circular import
        self.window =  UI_ExtractionWindow()  # Create an instance of the main window
        self.window.show()  # Show the window (no exec_ needed for QMainWindow)

    def clicker_bake(self):
        # Open dialog for admission
        self.openExtractionWindow()
        self.close()  # Close the current window when opening the main window

    def clicker_home(self):
        # Open main window
        self.openWindow()
        self.close()  # Close the current window when opening the main window

# Initialize The App
if __name__ == "__main__":  # Corrected check to ensure this runs only when executed directly
    app = QApplication(sys.argv)
    UIWindow = UI_PatientsWindow()  # Create an instance of UI_AdmisionWindow
    sys.exit(app.exec_())  # Properly exit the application
