import Adafruit_DHT

class SensorTemperaturaHumedad:
    def __init__(self, pin):
        self.pin = pin
        
    def medir_temperatura_humedad(self):
        # Especificamos que usaremos el sensor DHT11 y el pin que utilizaremos
        sensor = Adafruit_DHT.DHT11
        # Intentamos leer la temperatura y humedad
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, self.pin)
        # Si la lectura falla, regresamos valores nulos
        if humedad is None or temperatura is None:
            return None, None
        # Regresamos los valores leídos
        return temperatura, humedad

