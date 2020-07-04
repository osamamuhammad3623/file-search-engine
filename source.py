import sys
import os
from os import path
from PyQt5.QtWidgets import QApplication , QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUiType

FORM_CLASS,_ = loadUiType(path.join(path.dirname("__file__"),"main.ui"))



class my_form(QMainWindow,FORM_CLASS):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.search_btn.clicked.connect(self.searching_method)
        self.clear_btn.clicked.connect(self.clear_all)
        self.show()
        
    def searching_method(self):
        
        
        user_directory = self.directory.text()
        search_string = self.search_for.text()

        table_row = 0
        dir_files = os.listdir(user_directory)
        for file in dir_files:
            if file.endswith(".txt"):
                content = open (os.path.join(user_directory, file))
                #listdir returns names of files in the dir. , not the full path
                #so i had to join the path with the file name
                for line in content:
                    if search_string in line:
                        file_cell =QTableWidgetItem(file)
                        line_cell =QTableWidgetItem(line)
                        self.table.setItem(table_row, 0 , file_cell)
                        self.table.setItem(table_row, 1 , line_cell)
                        table_row += 1

        if table_row == 0:
            self.if_no_match()
                        
    def if_no_match(self):
        self.no_match.setText("No matches found !")
                        
    def clear_all(self):
        self.directory.clear()
        self.search_for.clear()
        self.table.clear()
        self.table.setHorizontalHeaderLabels(["File name", "Line"])
       

                 
if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = my_form()
    window.show()
    sys.exit(application.exec_())