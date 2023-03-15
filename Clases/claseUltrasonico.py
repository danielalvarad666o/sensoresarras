
import RPi.GPIO as GPIO
import time

class SensorUltrasónico:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def medir_distancia(self):
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
        return distancia
