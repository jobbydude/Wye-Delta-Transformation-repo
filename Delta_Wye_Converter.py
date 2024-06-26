#imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap

#Main app objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Delta Wye Converter")
main_window.setMaximumSize(800, 500)

#Functions
dtw = []
wtd = []

def Delta_to_Wye():
    try:
        z1 = complex(le1.text())
        z2 = complex(le2.text())
        z3 = complex(le3.text())
        za = (z2*z3)/(z1+z2+z3)
        zb = (z1*z3)/(z1+z2+z3)
        zc = (z1*z2)/(z1+z2+z3)
        lea.setText(str(za))
        leb.setText(str(zb))
        lec.setText(str(zc))
    except Exception as e:
        print(e)

def Wye_to_Delta():
    try:
        za = complex(lea.text())
        zb = complex(leb.text())
        zc = complex(lec.text())
        z1 = (za*zb+za*zc+zb*zc)/za
        z2 = (za*zb+za*zc+zb*zc)/zb
        z3 = (za*zb+za*zc+zb*zc)/zc
        le1.setText(str(z1))
        le2.setText(str(z2))
        le3.setText(str(z3))
    except Exception as e:
        print(e)
    


#Create all objects/widgets
pic1 = QPixmap('delta.jpg')
pic2 = QPixmap('wye.jpg')

label1 = QLabel("DELTA CONNECTION")
label1.setPixmap(pic1)
le1 = QLineEdit()
le1.setAlignment(Qt.AlignRight)
le2 = QLineEdit()
le2.setAlignment(Qt.AlignRight)
le3 = QLineEdit()
le3.setAlignment(Qt.AlignRight)
flo1 = QFormLayout()
flo1.addRow("Z1 =",le1)
flo1.addRow("Z2 =", le2)
flo1.addRow("Z3 =",le3)


label2 = QLabel("WYE CONNECTION")
label2.setPixmap(pic2)
lea = QLineEdit()
lea.setAlignment(Qt.AlignRight)
leb = QLineEdit()
leb.setAlignment(Qt.AlignRight)
lec = QLineEdit()
lec.setAlignment(Qt.AlignRight)
flo2 =QFormLayout()
flo2.addRow("Za =",lea)
flo2.addRow("Zb =", leb)
flo2.addRow("Zc =",lec)

button1 = QPushButton()
button1.setText("CONVERT")

button2 = QPushButton()
button2.setText("CONVERT")

grid = QGridLayout()
#Design/Layouts
grid.addWidget(label1, 0, 0)
grid.addWidget(label2, 0, 2)
grid.addLayout(flo1, 2, 0)
grid.addLayout(flo2, 2, 2)
grid.addWidget(button1, 3, 0)
grid.addWidget(button2, 3, 2)

main_window.setLayout(grid)

#Events
button1.clicked.connect(lambda : Delta_to_Wye())
button2.clicked.connect(lambda : Wye_to_Delta())

#Run/show app
main_window.show()
app.exec_()