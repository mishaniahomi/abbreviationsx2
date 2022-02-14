import docx
import os
import sys
from PyQt5 import QtWidgets
import design
Table = [[],[]]
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browse_folder)

    def browse_folder(self):
        Table = [[],[]]
        self.listWidget.clear()
        directory = str(QtWidgets.QFileDialog.getOpenFileUrl(self, "Выберите файл"))
        directory=directory.replace('(PyQt5.QtCore.QUrl(\'file:///','')
        directory = directory.replace('\'), \'All Files (*)\')', '')
        if directory:
            doc = docx.Document(directory)
            text = []
            for paragraph in doc.paragraphs:
                text.append(paragraph.text)
            abbreviation = ""
            arr_abbreviations = []
            Upper = 0
            for paragraph in text:
                for i in paragraph:
                    if ((i == ' ' or i =='') and abbreviation != ""):
                        if len(abbreviation) >= 2 and Upper >= 2:
                            arr_abbreviations.append(abbreviation)
                        abbreviation = ""
                        Upper = 0
                    elif i.isupper():
                        Upper += 1
                        abbreviation += i
                    elif (i != ' ' and abbreviation != ""):
                        abbreviation += i
            for p in sorted(set(arr_abbreviations)):
                self.listWidget.addItem(p)
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

