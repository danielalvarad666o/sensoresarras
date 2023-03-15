from Clases import claseUltrasonico,claseTemperatura,claseLed

sensor_temperatura = claseTemperatura.SensorTemperaturaHumedad(4)
sensor = claseUltrasonico.SensorUltrasónico(trigger_pin=18, echo_pin=24)
led=claseLed.Led(21)

while True:
 
 distancia = sensor.medir_distancia()
 temperatura = sensor_temperatura.medir_temperatura_humedad()

# Imprimir resultados
 if distancia:
    print(f"Distancia: {distancia} cm")
 else:
    print("No se pudo medir la distancia.")

 if temperatura:
    print(f"Temperatura: {temperatura} °C")
 else:
    print("No se pudo leer la temperatura.")

 print()
 print("QUIERES PRENDER EL LED")
 op=int(input("Escoje una opcion: "))
 if op==1:
     led.encender()
 else:
     led.apagar()
