import time
import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
import PySide6.QtWidgets as qtw


class PyAnnunPanel(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Status")
        self.nrows = 13
        self.ncols = 3
        self.layout = qtw.QGridLayout(self)
        self.button=[]
        for row in range(self.nrows):
            for col in range(self.ncols):
                ind = row * self.ncols + col
                b = qtw.QPushButton(str(ind))
                b.clicked.connect(lambda: self.button_callback(ind))
                self.button.append(b)
                self.layout.addWidget(b,row,col)
    def button_callback(self, ind):
        print(f"clicked {ind}")

#  Start the QT app    
def main(args=None):
    app = qtw.QApplication()
    pap = PyAnnunPanel()
    pap.show()
    ret=app.exec()
    sys.exit(ret)

if __name__ == '__main__':
    main()        
