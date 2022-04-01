import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from numpy import random

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.frame1 = QFrame()
        self.frame1.setStyleSheet('QFrame{background-color: #222}')
        self.grid = QGridLayout()
        self.hContainer = QHBoxLayout()
        self.titulo = QLabel(" Quieres ser mi novia?")
        self.titulo.setStyleSheet('QLabel{color:white}')
        self.boton1 = QPushButton(text="si")
        self.boton1.clicked.connect(lambda: self.aceptar())
        self.boton2 = QPushButton(text="no")
        self.boton2.clicked.connect(lambda: self.desplazar())
        #layout horizontal
        self.hContainer.addWidget(self.boton1)
        self.hContainer.addWidget(self.boton2)
        #layout Grid
        self.grid.addWidget(self.titulo,0,0,Qt.AlignCenter)
        self.grid.addLayout(self.hContainer,1,0,Qt.AlignCenter)
        self.frame1.setLayout(self.grid)
        self.setCentralWidget(self.frame1)
        self.show()
    def aceptar(self):
        dialogo = QDialog(self)
        container = QVBoxLayout()
        texto3 = QLabel(text="GRACIAS BB <3")
        texto3.setStyleSheet("QLabel{color:white}")
        dialogo.setStyleSheet("QDialog{background-color:#7B241C }")
        dialogo.setWindowTitle("Hola")
        container.addWidget(texto3)
        dialogo.setLayout(container)
        dialogo.exec()
        self.close()
    def desplazar(self):
        x = random.randint(1300)
        y = random.randint(500)
        self.move(x,y)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())