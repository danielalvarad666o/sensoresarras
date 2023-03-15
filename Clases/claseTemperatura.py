import adafruit_dht

class SensorTemperaturaHumedad:
    def __init__(self, pin):
        self.pin = pin
        self.dht_device = adafruit_dht.DHT11(self.pin)

    def medir_temperatura_humedad(self):
        try:
            temperatura = self.dht_device.temperature
            humedad = self.dht_device.humidity
            return temperatura, humedad
        except RuntimeError as error:
            print(f"Error al leer el sensor DHT11: {error}")
            return None, None

