import os
import glob
import time

class SensorTemperatura:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        self.device_file = '/sys/bus/w1/devices/{}/w1_slave'.format(sensor_id)

    def leer_temperatura(self):
        try:
            f = open(self.device_file, 'r')
            lineas = f.readlines()
            f.close()
            while lineas[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                f = open(self.device_file, 'r')
                lineas = f.readlines()
                f.close()
            igual_pos = lineas[1].find('t=')
            if igual_pos != -1:
                temperatura_str = lineas[1][igual_pos+2:]
                temperatura = float(temperatura_str) / 1000.0
                return temperatura
        except:
            return None
