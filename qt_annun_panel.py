import time
import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
import annun_button


class PyAnnunPanel(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Status")
        self.nrows = 7
        self.ncols = 3
        self.spacer_width = 3
        self.spacer_height = 3
        self.button_width = 70
        self.button_height = 30
        self.initButtons()

    def initButtons(self):
        self.setFixedSize(qtc.QSize(3+73*self.ncols, 3+33*self.nrows))
        self.buttons=[]
        for row in range(self.nrows):
            for col in range(self.ncols):
                ind = row * self.ncols + col
                b = annun_button.Annunciator(self)
                b.setGeometry(3+col*73, 3+row*33,70,30)
                b.setText(f"Button {ind+1}")
                self.buttons.append(b)
                print(f"added button {ind} at [{row},{col}]")

    def setError(self, annun_name, error_string ):
        for but in self.buttons:
            if but.text() == annun_name:
                but.setError(error_string)

    def setWarning(self, annun_name, warning_string ):
        for but in self.buttons:
            if but.text() == annun_name:
                but.setWarning(warning_string)

    def setInfo(self, annun_name, info_string ):
        for but in self.buttons:
            if but.text() == annun_name:
                but.setError(info_string)

    def changeAnnunName(self, old_button_name, new_button_name):
        for but in self.buttons:
            if but.text() == old_button_name:
                but.setText(new_button_name)

#  Start the QT app    
def main(args=None):
    app = qtw.QApplication()
    pap = PyAnnunPanel()
    pap.show()
    pap.setWarning("Button 2","Fuck")
    pap.changeAnnunName("Button 3","Fuck You")
    pap.setError("Button 1","Shit")
    ret=app.exec()
    exit(ret)

if __name__ == '__main__':
    main()        
