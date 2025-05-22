# Hospital Management System

A comprehensive hospital management system built with PyQt5 and SQLite for managing patient records, employee data, and department information.

# Previwe

![1](https://github.com/user-attachments/assets/cbe40dcc-50ee-4e7f-8554-6406683d5dfe)

![2](https://github.com/user-attachments/assets/260e5d04-cec0-4775-b14a-0c8e692ad751)

## Features

- Patient Management:
  - Add new patient records
  - Search and display patient information
  - Store patient details including code, name, contact, and medical information

- Employee Management:
  - Add new employee records
  - Search and display employee information
  - Track employee expertise and department assignments

- Department Management:
  - Add and manage hospital departments
  - Associate employees and patients with departments

- User Interface:
  - Persian language support (RTL)
  - Intuitive forms for data entry
  - Search functionality with multiple filters
  - Confirmation dialogs for operations

## Technologies Used

- Python 3
- PyQt5 for GUI
- SQLite for database
- Qt Designer for UI design

## Database Schema

The system uses SQLite with the following tables:

1. patients - Stores patient information
2. employees - Stores employee records
3. departments - Manages hospital departments

## Installation

1. Clone the repository:
   bash
   git clone [repository-url]
   cd hospital-management
   
2. Install dependencies:
   bash
   pip install PyQt5
   
3. Run the application:
   bash
   python Ehos_main.py
   
## Usage

1. Main Menu: Choose between Admission or Archive functions.
2. Admission: Register new patients or employees.
3. Archive: Search and view existing records.
4. Data Entry: Fill all required fields in forms.
5. Navigation: Use the home/back buttons to move between screens.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
