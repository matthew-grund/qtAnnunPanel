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
                b.setGeometry(3+col*73, 3+row*33,70,30) # FIXME - use class static values
                b.setText(f"Annun {ind+1}")
                self.buttons.append(b)
                # print(f"added button {ind} at [{row},{col}]")

    def setError(self, annun_name, error_string ):
        for but in self.buttons:
            if but.text() == annun_name:
                but.setError(error_string)

    def setCritical(self, annun_name, crit_string ):
        for but in self.buttons:
            if but.text() == annun_name:
                but.setCritical(crit_string)

    def setWarning(self, annun_name, warning_string ):
        for but in self.buttons:
            if but.text() == annun_name:
                but.setWarning(warning_string)

    def setInfo(self, annun_name, info_string ):
        for but in self.buttons:
            if but.text() == annun_name:
                but.setInfo(info_string)

    def setDebug(self, annun_name, info_string ):
        for but in self.buttons:
            if but.text() == annun_name:
                but.setDebug(info_string)

    def changeAnnunName(self, old_button_name, new_button_name):
        for but in self.buttons:
            if but.text() == old_button_name:
                but.setText(new_button_name)
                # print(f"{old_button_name} is now {new_button_name}")

    def changeAnnunColor(self, button_name, color):
        for but in self.buttons:
            if but.text() == button_name:
                but.setColor(color)
                # print(f"{button_name} is now colored {color}")

    def setAnnunBlink(self, button_name, do_blink):
        for but in self.buttons:
            if but.text() == button_name:
                but.setBlink(do_blink)
                # print(f"{button_name} is blinking: {do_blink}")

#  Start the QT app    
def main(args=None):
    app = qtw.QApplication()
    pap = PyAnnunPanel()
    pap.show()
    # all access is by annunciator name
    pap.changeAnnunName("Annun 1","Error")
    pap.changeAnnunName("Annun 2","Warning")
    pap.changeAnnunName("Annun 3","Info")   
    pap.changeAnnunName("Annun 4", "Debug")
    pap.changeAnnunName("Annun 5","Critical")
    pap.setWarning("Warning","Oh no! A warning.")
    pap.setInfo("Info","Hooray! Good good info.")
    pap.setError("Error","Drat, an Error.")
    pap.setDebug("Debug","some debug message.")
    pap.setCritical("Critical","Oh crap.")
    pap.changeAnnunName("Annun 6", "Magenta")
    pap.changeAnnunColor("MagEntA","magenta")
    pap.changeAnnunName("Annun 7","Blink")
    pap.changeAnnunColor("Blink","Cyan")
    pap.setAnnunBlink("Blink",True)
    ret=app.exec()
    exit(ret)

if __name__ == '__main__':
    main()        
