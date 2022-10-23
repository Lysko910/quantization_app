import sys
import cv2 as cv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from quantization import quantization
import threading

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TEST")
        self.setGeometry(250, 250, 680, 360)
        self.path = None
        #1
        Lay1_1 = QHBoxLayout()
        self.l1_1 = QLabel()
        self.l1_1.setText("Wybrana ścieżka do pliku :")
        Lay1_1.addWidget(self.l1_1)
        self.b1_1 = QPushButton()
        self.b1_1.setText("Wybierz plik")
        self.b1_1.clicked.connect(self.b1_1_clicked)
        Lay1_1.addWidget(self.b1_1)
        #2
        Lay2 = QVBoxLayout()
        self.el2_1 = QLineEdit()
        self.el2_1.setStyleSheet("background-color: white")
        Lay2.addWidget(self.el2_1)
        #3
        Lay3 = QGridLayout()
        self.cb3_1 = QCheckBox("K-means ")
        self.cb3_2 = QCheckBox("SuperPixele")
        self.cb3_3 = QCheckBox("Algorytm z Natury")
        self.cb3_4 = QCheckBox("Stała Paleta")
        self.l3_1 = QLabel()
        self.l3_1.setText("Parametry : K ,n")
        ###############
        self.l3_2 = QLabel()
        self.l3_2.setText("parametry2")
        self.l3_3 = QLabel()
        self.l3_3.setText("parametry3")
        self.l3_4 = QLabel()
        self.l3_4.setText("parametry4")
        ################
        self.el3_1_1 = QLineEdit()
        self.el3_1_1.setText("8")
        self.el3_1_2 = QLineEdit()
        self.el3_1_2.setText("10")
        self.el3_2_1 = QLineEdit()
        self.el3_2_1.setText("0.0")
        self.el3_2_2 = QLineEdit()
        self.el3_2_2.setText("0.0")
        self.el3_3_1 = QLineEdit()
        self.el3_3_1.setText("0.0")
        self.el3_3_2 = QLineEdit()
        self.el3_3_2.setText("0.0")
        self.el3_4_1 = QLineEdit()
        self.el3_4_1.setText("0.0")
        self.el3_4_2 = QLineEdit()
        self.el3_4_2.setText("0.0")

        Lay3.addWidget(self.cb3_1,0,0)
        Lay3.addWidget(self.l3_1, 0,1)
        Lay3.addWidget(self.el3_1_1, 0, 2)
        Lay3.addWidget(self.el3_1_2, 0, 3)

        Lay3.addWidget(self.cb3_2,1,0)
        Lay3.addWidget(self.l3_2, 1, 1)
        Lay3.addWidget(self.el3_2_1, 1, 2)
        Lay3.addWidget(self.el3_2_2, 1, 3)

        Lay3.addWidget(self.cb3_3,2,0)
        Lay3.addWidget(self.l3_3, 2, 1)
        Lay3.addWidget(self.el3_3_1, 2, 2)
        Lay3.addWidget(self.el3_3_2, 2, 3)

        Lay3.addWidget(self.cb3_4,3,0)
        Lay3.addWidget(self.l3_4, 3, 1)
        Lay3.addWidget(self.el3_4_1, 3, 2)
        Lay3.addWidget(self.el3_4_2, 3, 3)
        #4
        Lay4 =QHBoxLayout()
        self.b4_1 = QPushButton()
        self.b4_1.setText("Start")
        self.b4_1.clicked.connect(self.b4_1_clicked)
        #
        self.b4_2 = QPushButton()
        self.b4_2.setText("Reset (TO DO)")
        #
        Lay4.addWidget(self.b4_2)
        Lay4.addWidget(self.b4_1)

        #END
        Lay0 = QVBoxLayout()
        Lay0.addLayout(Lay1_1)
        Lay0.addLayout(Lay2)
        Lay0.addLayout(Lay3)
        Lay0.addLayout(Lay4)
        self.setLayout(Lay0)

    def b4_1_clicked(self):
        print("START!!")
        opcje = self.get_options()
        print(opcje)
        parameters = self.get_parameters()
        print(parameters)
        if self.path:
            img = cv.imread(self.path)
            obj = quantization()
            obj.show(img, "Orginal")

            if opcje[0]:
                k_mean_img = obj.K_means(img, parameters["parametr1"], n=10)
                obj.show(k_mean_img, "k_mean_img")
            if opcje[1]:
                k_mean_img2 = obj.K_means(img, parameters["parametr1"], n=10)
                obj.show(k_mean_img2, "Algorytm2")

        print("END!!")

    def b1_1_clicked(self):
        self.path = self.saveFileDialog()
        self.el2_1.setText(self.path)
        print(self.path)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            fileName, _ = QFileDialog.getOpenFileNames(self, "Wybierz ścieżkę do pliku", "",
                                                      "All Files (*);;Text Files (*.txt)", options=options)
        except:
            print("Exception in file explorer")
        if not fileName:
            fileName=['...']
        return fileName[0]


    def get_options(self):
        options = [False,False,False,False]
        options[0] = self.cb3_1.isChecked()
        options[1] = self.cb3_2.isChecked()
        options[2] = self.cb3_3.isChecked()
        options[3] = self.cb3_4.isChecked()
        return options

    def get_parameters(self):
        parameters = {"parametr1":0.0,
                      "parametr2":0.0,
                      "parametr3":0.0,
                      "parametr4":0.0}
        try:
            parameters["parametr1"] = float(self.el3_1_1.text())
            parameters["parametr2"] = float(self.el3_2_1.text())
            parameters["parametr3"] = float(self.el3_3_1.text())
            parameters["parametr4"] = float(self.el3_4_1.text())
        except:
            print("Error in get_parameter from GUI")
        return parameters

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())