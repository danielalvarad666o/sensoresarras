
import datetime
import RPi.GPIO as GPIO
import time
from ClaseLista import lista

class SensorUltrasónico(lista.Lista):
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        super().__init__()
        

    def medir_distancia(self,lista):
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)
        start_time = time.time()
        stop_time = time.time()
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()
        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()
        tiempo_transcurrido = stop_time - start_time
        distancia = (tiempo_transcurrido * 34300) / 2
        self.distanciaInfo= {"Clave":lista[1],"Tipo":"Distancia","Valor":distancia,"fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        super().crearjson(self.distanciaInfo,"sensores")
        
        return distancia
