# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AAV1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import uic, QtCore, QtGui, QtWidgets

import Adafruit_DHT
import RPi.GPIO as GPIO
import sys


from tempyhumedadv3 import programa_prueba




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 672)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextoTempEstatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoTempEstatico.setGeometry(QtCore.QRect(10, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TextoTempEstatico.setFont(font)
        self.TextoTempEstatico.setObjectName("TextoTempEstatico")
        self.TextoHumEstatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoHumEstatico.setGeometry(QtCore.QRect(10, 70, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TextoHumEstatico.setFont(font)
        self.TextoHumEstatico.setObjectName("TextoHumEstatico")
        self.TextoCelciusEstatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoCelciusEstatico.setGeometry(QtCore.QRect(370, 30, 55, 21))
        self.TextoCelciusEstatico.setObjectName("TextoCelciusEstatico")
        self.TextoPorcEstatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoPorcEstatico.setGeometry(QtCore.QRect(370, 90, 55, 21))
        self.TextoPorcEstatico.setObjectName("TextoPorcEstatico")
        self.TextoTempDinamico = QtWidgets.QLabel(self.centralwidget)
        self.TextoTempDinamico.setGeometry(QtCore.QRect(240, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TextoTempDinamico.setFont(font)
        self.TextoTempDinamico.setObjectName("TextoTempDinamico")
        self.TextoHumDinamico = QtWidgets.QLabel(self.centralwidget)
        self.TextoHumDinamico.setGeometry(QtCore.QRect(240, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TextoHumDinamico.setFont(font)
        self.TextoHumDinamico.setObjectName("TextoHumDinamico")
        self.TextoEstadosAAEstatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoEstadosAAEstatico.setGeometry(QtCore.QRect(350, 210, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.TextoEstadosAAEstatico.setFont(font)
        self.TextoEstadosAAEstatico.setObjectName("TextoEstadosAAEstatico")
        self.TextoAA1Estatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoAA1Estatico.setGeometry(QtCore.QRect(260, 540, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TextoAA1Estatico.setFont(font)
        self.TextoAA1Estatico.setObjectName("TextoAA1Estatico")
        self.TextoAA2Estatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoAA2Estatico.setGeometry(QtCore.QRect(660, 540, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TextoAA2Estatico.setFont(font)
        self.TextoAA2Estatico.setObjectName("TextoAA2Estatico")
        self.figura1 = QtWidgets.QLabel(self.centralwidget)
        self.figura1.setGeometry(QtCore.QRect(130, 290, 301, 211))
        self.figura1.setText("")
        self.figura1.setPixmap(QtGui.QPixmap("/home/pi/Proyecto/ProyectoSDA/aire_encendido.jpeg"))

        self.figura1.setScaledContents(True)
        self.figura1.setObjectName("figura1")
        self.figura2 = QtWidgets.QLabel(self.centralwidget)
        self.figura2.setGeometry(QtCore.QRect(530, 290, 301, 201))
        self.figura2.setText("")
        self.figura2.setPixmap(QtGui.QPixmap("aire_apagado.jpeg"))
        self.figura2.setScaledContents(True)
        self.figura2.setObjectName("figura2")
        self.TextoParamConfigEstatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoParamConfigEstatico.setGeometry(QtCore.QRect(580, 30, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TextoParamConfigEstatico.setFont(font)
        self.TextoParamConfigEstatico.setObjectName("TextoParamConfigEstatico")
        self.TextoTempConmuEstatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoTempConmuEstatico.setGeometry(QtCore.QRect(580, 60, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TextoTempConmuEstatico.setFont(font)
        self.TextoTempConmuEstatico.setObjectName("TextoTempConmuEstatico")
        self.TextoMaxTempEstatico = QtWidgets.QLabel(self.centralwidget)
        self.TextoMaxTempEstatico.setGeometry(QtCore.QRect(580, 120, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TextoMaxTempEstatico.setFont(font)
        self.TextoMaxTempEstatico.setObjectName("TextoMaxTempEstatico")
        self.ComboBoxTconmu = QtWidgets.QComboBox(self.centralwidget)
        self.ComboBoxTconmu.setGeometry(QtCore.QRect(860, 80, 73, 22))
        self.ComboBoxTconmu.setObjectName("ComboBoxTconmu")
        self.ComboBoxTconmu.addItem("")
        self.ComboBoxTconmu.addItem("")
        self.ComboBoxTconmu.addItem("")
        self.ComboBoxTempMax = QtWidgets.QComboBox(self.centralwidget)
        self.ComboBoxTempMax.setGeometry(QtCore.QRect(860, 140, 73, 22))
        self.ComboBoxTempMax.setObjectName("ComboBoxTempMax")
        self.ComboBoxTempMax.addItem("")
        self.ComboBoxTempMax.addItem("")
        self.ComboBoxTempMax.addItem("")
        self.ComboBoxTempMax.addItem("")
        self.ComboBoxTempMax.addItem("")
        self.ComboBoxTempMax.addItem("")
        self.BotonCambiarParam = QtWidgets.QPushButton(self.centralwidget)
        self.BotonCambiarParam.setGeometry(QtCore.QRect(840, 190, 101, 41))
        self.BotonCambiarParam.setObjectName("BotonCambiarParam")
        
        #self.BotonIniciar = QtWidgets.QPushButton(self.centralwidget)
        #self.BotonIniciar.setGeometry(QtCore.QRect(910, 580, 101, 41))
        #self.BotonIniciar.setObjectName("BotonIniciar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.BotonCambiarParam.clicked.connect(self.pressedCambio)
        #self.BotonIniciar.clicked.connect(self.pressedInicio)
        self.programa_prueba_obj = programa_prueba()
        
        self.timerRefrescarValores = QtCore.QTimer()
        self.timerRefrescarValores.timeout.connect(self.timeouttimerRefrescarValores)
        self.timerRefrescarValores.start(3000)
        index = self.ComboBoxTempMax.findText(str(self.programa_prueba_obj.temperaturaEstablecida))
        self.ComboBoxTempMax.setCurrentIndex(index)
        index2 = self.ComboBoxTconmu.findText(str((self.programa_prueba_obj.tiempoConmutacionAires)//1000))
        self.ComboBoxTconmu.setCurrentIndex(index2)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TextoTempEstatico.setText(_translate("MainWindow", "Temperatura :"))
        self.TextoHumEstatico.setText(_translate("MainWindow", "Humedad:"))
        self.TextoCelciusEstatico.setText(_translate("MainWindow", "C"))
        self.TextoPorcEstatico.setText(_translate("MainWindow", "%"))
        self.TextoTempDinamico.setText(_translate("MainWindow", "TextLabel"))
        self.TextoHumDinamico.setText(_translate("MainWindow", "TextLabel"))
        self.TextoEstadosAAEstatico.setText(_translate("MainWindow", "Estado de AA"))
        self.TextoAA1Estatico.setText(_translate("MainWindow", "AA1"))
        self.TextoAA2Estatico.setText(_translate("MainWindow", "AA2"))
        self.TextoParamConfigEstatico.setText(_translate("MainWindow", "Parametros de configuración "))
        self.TextoTempConmuEstatico.setText(_translate("MainWindow", "T.Conmutacion (Seg) :"))
        self.TextoMaxTempEstatico.setText(_translate("MainWindow", "Temp. Maxima (C):"))
        self.ComboBoxTconmu.setItemText(0, _translate("MainWindow", "20"))
        self.ComboBoxTconmu.setItemText(1, _translate("MainWindow", "60"))
        self.ComboBoxTconmu.setItemText(2, _translate("MainWindow", "120"))
        self.ComboBoxTempMax.setItemText(0, _translate("MainWindow", "10"))
        self.ComboBoxTempMax.setItemText(1, _translate("MainWindow", "15"))
        self.ComboBoxTempMax.setItemText(2, _translate("MainWindow", "20"))
        self.ComboBoxTempMax.setItemText(3, _translate("MainWindow", "21"))
        self.ComboBoxTempMax.setItemText(4, _translate("MainWindow", "25"))
        self.ComboBoxTempMax.setItemText(5, _translate("MainWindow", "30"))
        self.BotonCambiarParam.setText(_translate("MainWindow", "Cambiar"))
        #self.BotonIniciar.setText(_translate("MainWindow", "Iniciar"))
        
    def pressedCambio(self):
        #print (self.ComboBoxTconmu.currentText())
        #print (self.ComboBoxTempMax.currentText())
        self.programa_prueba_obj.tiempoConmutacionAires= int(self.ComboBoxTconmu.currentText())*1000
        self.programa_prueba_obj.temperaturaEstablecida= int(self.ComboBoxTempMax.currentText())

    def pressedInicio(self):
        print ("inicio")
        #self.programa_prueba_obj.modoSistemRelay()
        #self.TextoTempDinamico.setText(str (self.programa_prueba_obj.temperatura))
        
    def timeouttimerRefrescarValores(self):
       self.TextoTempDinamico.setText(str (self.programa_prueba_obj.temperatura))
       self.TextoHumDinamico.setText(str (self.programa_prueba_obj.humedad))

       
       if (self.programa_prueba_obj.modo_operacion==1):
            self.figura1.setPixmap(QtGui.QPixmap("aire_encendido.jpeg"))
            self.figura2.setPixmap(QtGui.QPixmap("aire_encendido.jpeg"))
       elif(self.programa_prueba_obj.bandera_Relay==1):
            #print ("entre1")
            self.figura1.setPixmap(QtGui.QPixmap("/home/pi/Proyecto/ProyectoSDA/aire_encendido.jpeg"))
            self.figura2.setPixmap(QtGui.QPixmap("/home/pi/Proyecto/ProyectoSDA/aire_apagado.jpeg"))
       else:
            #print ("entre2")
            self.figura2.setPixmap(QtGui.QPixmap("/home/pi/Proyecto/ProyectoSDA/aire_encendido.jpeg"))
            self.figura1.setPixmap(QtGui.QPixmap("/home/pi/Proyecto/ProyectoSDA/aire_apagado.jpeg"))
            

        
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
