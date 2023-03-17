import RPi.GPIO as GPIO
import time
from ClaseLista import lista

class Led(lista.Lista):
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        super().__init__()

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)

    def parpadear(self, duracion_encendido, duracion_apagado, repeticiones):
        for i in range(repeticiones):
            self.encender()
            time.sleep(duracion_encendido)
            self.apagar()
            time.sleep(duracion_apagado)
