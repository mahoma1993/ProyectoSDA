from PyQt5 import uic, QtCore, QtGui
import Adafruit_DHT
import RPi.GPIO as GPIO
import sys
import smtplib
import ssl
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
        self.temperaturaEstablecida=25
        self.modo_operacion=0
        self.tiempoConmutacionAires = 20000
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
        self.timerCheckSensorTemp.start(1000)
        
        self.correo_enviado = False
        self.timer_enviar_correo = QtCore.QTimer()
        self.timer_enviar_correo.timeout.connect(self.resetear_correo_enviado)
        self.intervalo_correo = 900000  # 15 minutos en milisegundos
    # checkeo la temperatura y actualizo el estado de operacion    
    def timeouttimerCheckSensorTemp(self):
        self.humedad, self.temperatura = Adafruit_DHT.read_retry(self.sensor, self.pin_sensor)
        #print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(self.temperatura, self.humedad))
        #print ('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(self.temperaturaEstablecida, self.humedad))
        if (self.temperatura >= self.temperaturaEstablecida):
            self.modo_operacion = 1
            if (self.correo_enviado == False):
                self.enviar_correo()
                self.correo_enviado = True
                self.timer_enviar_correo.start(self.intervalo_correo)
                
        elif (self.temperatura < self.temperaturaEstablecida - 3):
            self.modo_operacion = 0
            self.correo_enviado = False
            self.timer_enviar_correo.stop()
            
        self.modoSistemRelay()
            
    def modoSistemRelay(self):
        if (self.modo_operacion == 1 ):
            print ("hola entre para q se prendan los dos")
            GPIO.output(self.pin_relay1, GPIO.LOW)
            GPIO.output(self.pin_relay2, GPIO.LOW)
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
            #print ("secuencia 1 1 vez")
            self.bandera_Relay=1
            self.timerInicioDeSecuenciaRelay.start(self.tiempoConmutacionAires)
          

            
    def inicioDeSecuenciaRelay2(self):
        GPIO.output(self.pin_relay1, GPIO.HIGH)
        GPIO.output(self.pin_relay2, GPIO.LOW)
        if not self.timerInicioDeSecuenciaRelay2.isActive():
            #print ("secuencia 2 1 vez")
            self.bandera_Relay=2
            self.timerInicioDeSecuenciaRelay2.start(self.tiempoConmutacionAires)
           

    def timeoutTimerInicioDeSecuencia(self):
        #self.inicioDeSecuenciaRelay2()
        #print ("termino el conteo 1")
        self.bandera_Relay=2
        self.timerInicioDeSecuenciaRelay.stop()
        
    def timeoutTimerInicioDeSecuencia2(self):
        #self.inicioDeSecuenciaRelay()
        #print ("termino el conteo 2")
        self.bandera_Relay=1
        self.timerInicioDeSecuenciaRelay2.stop()
        
    def enviar_correo(self):
        # Configuración para SMTP
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
        smtp_encryption = 'STARTTLS'
        ccorreo_emisor = 'mierarpi2024@hotmail.com'
        contrasena_correo = 'yrxputkygbrjapbp'  # Reemplaza con la contraseña de aplicación generada

        # Mensaje a enviar
        mensaje = MIMEMultipart()
        mensaje['From'] = ccorreo_emisor
        mensaje['To'] = 'mohamed_hamudi@hotmail.com'
        mensaje['Subject'] = 'Temperatura alta'
        mensaje.attach(MIMEText(f"La temperatura actual ({self.temperatura}°C) supera la temperatura establecida ({self.temperaturaEstablecida}°C).", 'plain'))

                

               # Configuración de contexto SSL para SMTP
        context_smtp = ssl.create_default_context()

        try:
            # Enviar correo utilizando SMTP
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls(context=context_smtp)
                server.login(ccorreo_emisor, contrasena_correo)
                server.sendmail(ccorreo_emisor, 'mohamed_hamudi@hotmail.com', mensaje.as_string())
                print("Correo enviado exitosamente.")

        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            
            
    def resetear_correo_enviado(self):
        self.correo_enviado = False
        self.timer_enviar_correo.stop()

if __name__ == "__main__":
    app = QtCore.QCoreApplication([])  
    prueba = programa_prueba()
    #prueba.modoSistemRelay()
    sys.exit(app.exec_())



