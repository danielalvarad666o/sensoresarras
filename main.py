from Clases import claseUltrasonico,claseTemperatura



while True:
 sensor_temperatura = claseTemperatura.SensorTemperatura(sensor_id='28-000000000000')
 sensor = claseUltrasonico.SensorUltrasónico(trigger_pin=18, echo_pin=24)
 distancia = sensor.medir_distancia()
 temperatura = sensor_temperatura.leer_temperatura()

# Imprimir resultados
 if distancia:
    print(f"Distancia: {distancia} cm")
 else:
    print("No se pudo medir la distancia.")

 if temperatura:
    print(f"Temperatura: {temperatura} °C")
 else:
    print("No se pudo leer la temperatura.")
