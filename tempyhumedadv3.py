from PyQt5 import uic, QtCore, QtGui
import Adafruit_DHT
import RPi.GPIO as GPIO
import sys

sensor = Adafruit_DHT.DHT11

class programa_prueba(QtCore.QObject):  
    def __init__(self):
        super().__init__()
        self.sensor = Adafruit_DHT.DHT11
        self.pin_sensor = 4
        self.pin_relay1 = 17
        self.pin_relay2 = 27
        self.temperatura= 0
        self.humedad=0
        self.temperaturaEstablecida=21
        self.modo_operacion=0
        self.tiempoConmutacionAires = 5000
        self.bandera_Relay = 1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pin_relay1, GPIO.OUT)
        GPIO.setup(self.pin_relay2, GPIO.OUT)
        GPIO.output(self.pin_relay1, GPIO.HIGH)
        GPIO.output(self.pin_relay1, GPIO.HIGH)

        self.timerInicioDeSecuenciaRelay = QtCore.QTimer()
        self.timerInicioDeSecuenciaRelay.timeout.connect(self.timeoutTimerInicioDeSecuencia)
        self.timerInicioDeSecuenciaRelay2 = QtCore.QTimer()
        self.timerInicioDeSecuenciaRelay2.timeout.connect(self.timeoutTimerInicioDeSecuencia2)
        # con ste codigo se logra iniciar la lectura de temperatura
        self.timerCheckSensorTemp = QtCore.QTimer()
        self.timerCheckSensorTemp.timeout.connect(self.timeouttimerCheckSensorTemp)
        self.timerCheckSensorTemp.start(5000)
    # checkeo la temperatura y actualizo el estado de operacion    
    def timeouttimerCheckSensorTemp(self):
        self.humedad, self.temperatura = Adafruit_DHT.read_retry(self.sensor, self.pin_sensor)
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(self.temperatura, self.humedad)) 
        if (self.temperatura >= self.temperaturaEstablecida):
            self.modo_operacion = 1
        elif (self.temperatura < self.temperaturaEstablecida):
            self.modo_operacion = 0
        self.modoSistemRelay()
            
    def modoSistemRelay(self):
        if (self.modo_operacion == 1 ):    
            GPIO.output(self.pin_relay1, GPIO.LOW)
            GPIO.output(self.pin_relay1, GPIO.LOW)
            self.timerInicioDeSecuenciaRelay.stop()
            self.timerInicioDeSecuenciaRelay2.stop()
        else:
            if (self.bandera_Relay==1):
               self.inicioDeSecuenciaRelay()
            else:
               self.inicioDeSecuenciaRelay2() 
            
    
    def inicioDeSecuenciaRelay(self):
        GPIO.output(self.pin_relay1, GPIO.LOW)
        GPIO.output(self.pin_relay2, GPIO.HIGH)
        if not self.timerInicioDeSecuenciaRelay.isActive():
            self.bandera_relay=1
            self.timerInicioDeSecuenciaRelay.start(self.tiempoConmutacionAires)


            
    def inicioDeSecuenciaRelay2(self):
        GPIO.output(self.pin_relay1, GPIO.HIGH)
        GPIO.output(self.pin_relay2, GPIO.LOW)
        if not self.timerInicioDeSecuenciaRelay2.isActive():
            self.bandera_relay=2
            self.timerInicioDeSecuenciaRelay2.start(self.tiempoConmutacionAires)
 


    def timeoutTimerInicioDeSecuencia(self):
        self.inicioDeSecuenciaRelay2()
        self.bandera_relay=2
        self.timerInicioDeSecuenciaRelay2.start(self.tiempoConmutacionAires)
        self.timerInicioDeSecuenciaRelay.stop()
        
    def timeoutTimerInicioDeSecuencia2(self):
        self.inicioDeSecuenciaRelay()
        self.bandera_relay=1
        self.timerInicioDeSecuenciaRelay.start(self.tiempoConmutacionAires)
        self.timerInicioDeSecuenciaRelay2.stop()

if __name__ == "__main__":
    app = QtCore.QCoreApplication([])  
    prueba = programa_prueba()
    #prueba.modoSistemRelay()
    sys.exit(app.exec_())

