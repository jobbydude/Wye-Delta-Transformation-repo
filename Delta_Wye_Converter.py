#imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap


class DeltaWyeConvertApp(QWidget):

    def __init__(self):
        super().__init__()
        #Main app objects and settings
        self.setWindowTitle("Delta Wye Converter")  #Self refers to the inherited QWidget of the class
        self.setMaximumSize(800, 500)

        #Create all objects/widgets
        self.pic1 = QPixmap('delta.jpg')
        self.pic2 = QPixmap('wye.jpg')

        self.label1 = QLabel("DELTA CONNECTION")
        self.label1.setPixmap(self.pic1)
        self.le1 = QLineEdit()
        self.le1.setAlignment(Qt.AlignRight)
        self.le2 = QLineEdit()
        self.le2.setAlignment(Qt.AlignRight)
        self.le3 = QLineEdit()
        self.le3.setAlignment(Qt.AlignRight)
        self.flo1 = QFormLayout()
        self.flo1.addRow("Z1 =",self.le1)
        self.flo1.addRow("Z2 =", self.le2)
        self.flo1.addRow("Z3 =",self.le3)


        self.label2 = QLabel("WYE CONNECTION")
        self.label2.setPixmap(self.pic2)
        self.lea = QLineEdit()
        self.lea.setAlignment(Qt.AlignRight)
        self.leb = QLineEdit()
        self.leb.setAlignment(Qt.AlignRight)
        self.lec = QLineEdit()
        self.lec.setAlignment(Qt.AlignRight)
        self.flo2 =QFormLayout()
        self.flo2.addRow("Za =",self.lea)
        self.flo2.addRow("Zb =", self.leb)
        self.flo2.addRow("Zc =",self.lec)

        self.button1 = QPushButton()
        self.button1.setText("CONVERT")

        self.button2 = QPushButton()
        self.button2.setText("CONVERT")

        #Design/Layouts
        self.grid = QGridLayout()
        self.grid.addWidget(self.label1, 0, 0)
        self.grid.addWidget(self.label2, 0, 2)
        self.grid.addLayout(self.flo1, 2, 0)
        self.grid.addLayout(self.flo2, 2, 2)
        self.grid.addWidget(self.button1, 3, 0)
        self.grid.addWidget(self.button2, 3, 2)
        self.setLayout(self.grid)

        #Events
        self.button1.clicked.connect(self.Delta_to_Wye)
        self.button2.clicked.connect(self.Wye_to_Delta)
        # self.button1.clicked.connect(lambda : self.Delta_to_Wye(parameters))
        # self.button2.clicked.connect(lambda : self.Wye_to_Delta(parameters))


    #Methods
    def Delta_to_Wye(self):
        try:
            z1 = complex(self.le1.text())
            z2 = complex(self.le2.text())
            z3 = complex(self.le3.text())
            za = (z2*z3)/(z1+z2+z3)
            zb = (z1*z3)/(z1+z2+z3)
            zc = (z1*z2)/(z1+z2+z3)
            self.lea.setText(str(za))
            self.leb.setText(str(zb))
            self.lec.setText(str(zc))
        except Exception as e:
            print(e)

    def Wye_to_Delta(self):
        try:
            za = complex(self.lea.text())
            zb = complex(self.leb.text())
            zc = complex(self.lec.text())
            z1 = (za*zb+za*zc+zb*zc)/za
            z2 = (za*zb+za*zc+zb*zc)/zb
            z3 = (za*zb+za*zc+zb*zc)/zc
            self.le1.setText(str(z1))
            self.le2.setText(str(z2))
            self.le3.setText(str(z3))
        except Exception as e:
            print(e)

#Run/show app
# if __name__ in"__main__":
# if __name__ in"__Delta_Wye_Converter_":
app = QApplication([])
main_window = DeltaWyeConvertApp()
main_window.show()
app.exec_()
