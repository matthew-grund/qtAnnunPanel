import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg

class Annunciator(qtw.QPushButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.setFixedSize(70, 30)
        self.setColor("Grey")
        self.setText("<Untitled>")

    def setColor(self, color):
        
        self.setStyleSheet("background-color: %s;" % color)
        self.bg_color = color
        self.show()

    def setError(self,error_string):
        self.setColor("Red")
        self.setToolTip(error_string)
        self.show()

    def setWarning(self,warn_string):
        self.setColor("Yellow")
        self.setToolTip(warn_string)
        self.show()

    def setInfo(self,info_string):
        self.setColor("Green")
        self.setToolTip(info_string)
        self.show()
