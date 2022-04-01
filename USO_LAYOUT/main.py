import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
'''
This project was created by David Diaz E, and is freely accesible to the open soruce developer comumunity :) .
If you like my work , please visit my youtube channel in this link: https://www.youtube.com/channel/UC9G8JpXyUztKxAO7H6ZVbgA
Have a nice day and remember never stop your improving! 
Att: David Diaz E 
'''
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.container =  QFrame()
        self.container.setObjectName("contenedor")
        self.container.setStyleSheet("#contenedor{background-color: #222}")
        self.layout = QVBoxLayout()
        ''' we create a layout and a container'''
        self.texto1 =  QLabel(text = "hola mundo 1")
        self.texto1.setStyleSheet("QLabel{color: red;}")
        self.texto2 = QLabel(text="hola mundo 2")
        self.texto2.setStyleSheet("QLabel{color: yellow;}")
        self.texto3 = QLabel(text="hola mundo 3")
        self.texto3.setStyleSheet("QLabel{color: blue;}")
        self.texto4 = QLabel(text="hola mundo 4")
        self.texto4.setStyleSheet("QLabel{color: cyan;}")
        self.layout.setSpacing(40)

        '''we added the text widgets to the layout'''
        self.layout.addWidget(self.texto1,0,Qt.AlignLeft)
        self.layout.addWidget(self.texto2, 1, Qt.AlignRight)
        self.layout.addWidget(self.texto3, 2, Qt.AlignTop)
        self.layout.addWidget(self.texto4, 3, Qt.AlignBottom)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        '''displayed the main window'''
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window =  MainWindow()
    sys.exit(app.exec_())