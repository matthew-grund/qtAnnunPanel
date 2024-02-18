import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
import math

class Annunciator(qtw.QPushButton):

    def __init__(self,parent):
        super().__init__(parent)
        self.setFixedSize(70, 30)
        self.setColor("Grey")
        self.setText("<Untitled>")
        self.setBlink(False)
        self.do_blink = False
        self.is_off = False
        self.blink_timer = qtc.QTimer(self)
        self.blink_timer.singleShot(500, self.blinkTimerCallback)
        
    def blinkTimerCallback(self):
        if self.do_blink:
            if self.is_off:
                self.setColor(self.bg_color)
                self.is_off = False
            else:
                old_color = self.bg_color
                self.setColor("black")
                self.bg_color = old_color
                self.is_off = True
        else:
            self.is_off = False
            self.setColor(self.bg_color)    
        self.blink_timer.singleShot(500, self.blinkTimerCallback)

    def colorIsBright(self,color):
        qtcolor = qtg.QColor(color)
        red = qtcolor.red()
        green = qtcolor.green()
        blue = qtcolor.blue()
        b = red * red * 0.241 + green * green * 0.691 + blue * blue * 0.068
        brightness = math.sqrt(b)
        # print(f"color: {color} brightness: {brightness}")
        if brightness > 130:
            return True
        return False

    def setColor(self, color):
        if self.colorIsBright(color):
            self.setStyleSheet("color: black; background-color: %s;" % color)
        else:
            self.setStyleSheet("color: white; background-color: %s;" % color)   
        self.bg_color = color
        self.show()

    def setBlink(self, do_blink):
        self.do_blink = do_blink

    def setCritical(self,crit_string):
        self.setColor("Orange")
        self.setToolTip(crit_string)
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
        # print(f"Info (Green) {self.text()}: {info_string}")
        self.setColor("Green")
        self.setToolTip(info_string)
        self.show()

    def setDebug(self,debug_string):
        # print(f"Debug (Blue) {self.text()}: {debug_string}")
        self.setColor("Blue")
        self.setToolTip(debug_string)
        self.show()