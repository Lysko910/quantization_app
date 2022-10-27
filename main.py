import sys
import cv2 as cv
from PyQt5.QtWidgets import *
from utils import *
from PyQt5 import QtCore
from PyQt5 import QtGui

class PopUP_Parameters(QWidget):
    def __del__(self):
        pass
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parameters")
        self.setGeometry(680, 590, 340, 180)
        self.setWindowIcon(QtGui.QIcon("images/frog.png"))
        layout = QVBoxLayout()
        self.Topic = QLabel("Parameters")
        layout.addWidget(self.Topic)
        self.setLayout(layout)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.options = None
        self.setWindowIcon(QtGui.QIcon("images/frog.png"))
        self.setWindowTitle("QuantizationApp")
        self.setGeometry(450, 450, 680, 360)
        self.path = "images/marriage._default.jpg"
        self.parameters = load_default_parameters()
        self.PopUp = PopUP_Parameters()

        # 1 layer of layout
        Lay1_1 = QHBoxLayout()
        self.l1_1 = QLabel()
        self.l1_1.setText("Wybrana ścieżka do pliku :")
        Lay1_1.addWidget(self.l1_1)
        self.b1_1 = QPushButton()
        self.b1_1.setText("Wybierz plik")
        self.b1_1.clicked.connect(self.b1_1_clicked)
        Lay1_1.addWidget(self.b1_1)
        # 2 layer of layout
        Lay2 = QVBoxLayout()
        self.el2_1 = QLineEdit()
        self.el2_1.setText(self.path)
        self.el2_1.setStyleSheet("background-color: white")
        Lay2.addWidget(self.el2_1)
        # 3 layer of layout
        Lay3 = QGridLayout()
        self.cb3_1 = QCheckBox("K-means ")
        self.cb3_2 = QCheckBox("SuperPixele")
        self.cb3_3 = QCheckBox("Algorithm z Natury")
        self.cb3_4 = QCheckBox("Stała Paleta")
        ###############
        self.l3_1 = QLabel()
        self.l3_1.setText("Parameters : K ,n")
        self.l3_2 = QLabel()
        self.l3_2.setText("Parameters_2")
        self.l3_3 = QLabel()
        self.l3_3.setText("Parameters_3")
        self.l3_4 = QLabel()
        self.l3_4.setText("pParameter_4")
        ################
        self.el3_1_1 = QLineEdit()
        self.el3_1_2 = QLineEdit()
        self.el3_2_1 = QLineEdit()
        self.el3_2_2 = QLineEdit()
        self.el3_3_1 = QLineEdit()
        self.el3_3_2 = QLineEdit()
        self.el3_4_1 = QLineEdit()
        self.el3_4_2 = QLineEdit()
        #put text to all of edit lines
        self.updateEditLineParameters()

        ###############
        Lay3.addWidget(self.cb3_1, 0, 0)
        Lay3.addWidget(self.l3_1, 0, 1)
        Lay3.addWidget(self.el3_1_1, 0, 2)
        Lay3.addWidget(self.el3_1_2, 0, 3)
        ###############
        Lay3.addWidget(self.cb3_2, 1, 0)
        Lay3.addWidget(self.l3_2, 1, 1)
        Lay3.addWidget(self.el3_2_1, 1, 2)
        Lay3.addWidget(self.el3_2_2, 1, 3)
        ###############
        Lay3.addWidget(self.cb3_3, 2, 0)
        Lay3.addWidget(self.l3_3, 2, 1)
        Lay3.addWidget(self.el3_3_1, 2, 2)
        Lay3.addWidget(self.el3_3_2, 2, 3)
        ###############
        Lay3.addWidget(self.cb3_4, 3, 0)
        Lay3.addWidget(self.l3_4, 3, 1)
        Lay3.addWidget(self.el3_4_1, 3, 2)
        Lay3.addWidget(self.el3_4_2, 3, 3)
        # 4 layer of layout
        Lay4 = QHBoxLayout()
        self.b4_1 = QPushButton()
        self.b4_1.setText("Start Quantization")
        self.b4_1.clicked.connect(self.b4_1_clicked)
        ###############
        self.b4_2 = QPushButton()
        self.b4_2.setText("Restore to defaults")
        self.b4_2.clicked.connect(self.b4_2_clicked)
        ###############
        Lay4.addWidget(self.b4_2)
        Lay4.addWidget(self.b4_1)
        # END
        Lay0 = QVBoxLayout()
        Lay0.addLayout(Lay1_1)
        Lay0.addLayout(Lay2)
        Lay0.addLayout(Lay3)
        Lay0.addLayout(Lay4)
        self.setLayout(Lay0)

    ## MAIN TASK ##
    def b4_1_clicked(self):
        print("START!!")
        self.options = self.get_options()
        self.parameters = self.get_parameters()
        print( self.options)
        print(self.parameters)
        self.PopUp.show()

        if self.path:
            # read image from chosen path
            img = cv.imread(self.path)
            # start quantization process:
            # refactor images with chosen parameters in picked algorithms
            # and show images in 'n' windows
            makeQuantization(img,  self.options, self.parameters)
        print("END!!")

    ## FILE DIALOG ##
    def b1_1_clicked(self):
        # open file dialog window and get path to image
        self.path = self.saveFileDialog()
        # print path in edit line
        self.el2_1.setText(self.path)
        print(self.path)

    ## RESET ##
    def b4_2_clicked(self):
        # Load default path
        self.path = "images/marriage._default.jpg"
        # Load default parameters
        self.parameters = load_default_parameters()
        #set parameters on gui
        self.el2_1.setText(self.path)
        self.updateEditLineParameters()
        self.cb3_1.setChecked(False)
        self.cb3_2.setChecked(False)
        self.cb3_3.setChecked(False)
        self.cb3_4.setChecked(False)
        self.PopUp.close()
        cv.destroyAllWindows()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            fileName, _ = QFileDialog.getOpenFileNames(self, "Wybierz ścieżkę do pliku", "",
                                                       "All Files (*);;Text Files (*.txt)", options=options)
        except:
            print("Exception in file explorer")
        if not fileName:
            fileName = ['...']
        return fileName[0]

    def get_options(self):
        options = {"Algorithm_1": self.cb3_1.isChecked(), "Algorithm_2": self.cb3_2.isChecked(),
                   "Algorithm_3": self.cb3_3.isChecked(), "Algorithm_4": self.cb3_4.isChecked()}
        return options

    def get_parameters(self):
        parameters = {"parameter1": 0.0,
                      "parameter2": 0.0,
                      "parameter3": 0.0,
                      "parameter4": 0.0}
        try:
            parameters["parameter1"] = float(self.el3_1_1.text())
            parameters["parameter2"] = float(self.el3_2_1.text())
            parameters["parameter3"] = float(self.el3_3_1.text())
            parameters["parameter4"] = float(self.el3_4_1.text())
        except:
            print("Error in get_parameter from GUI")
        return parameters

    def updateEditLineParameters(self):
        self.el3_1_1.setText(str(self.parameters["parameter1"]))
        self.el3_1_2.setText(str(self.parameters["parameter2"]))
        self.el3_2_1.setText(str(self.parameters["parameter3"]))
        self.el3_2_2.setText(str(self.parameters["parameter4"]))
        self.el3_3_1.setText(str(self.parameters["parameter5"]))
        self.el3_3_2.setText(str(self.parameters["parameter6"]))
        self.el3_4_1.setText(str(self.parameters["parameter7"]))
        self.el3_4_2.setText(str(self.parameters["parameter8"]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
