import RPi.GPIO as GPIO
import dht11
import time

class SensorTemperaturaHumedad:
    def __init__(self, pin):
        self.pin = pin
        self.instance = dht11.DHT11(pin=self.pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def medir_temperatura_humedad(self):
        time.sleep(2)  # Esperar 2 segundos antes de leer los valores
        result = self.instance.read()
        if result.is_valid:
            temperatura = result.temperature
            humedad = result.humidity
            print(f"Temperatura: {temperatura}°C, Humedad: {humedad}%")
            return temperatura, humedad
        else:
            print("Error al leer los valores del sensor")
            return None, None


