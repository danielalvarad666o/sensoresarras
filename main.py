from Clases import claseUltrasonico



sensor = claseUltrasonico.SensorUltrasónico(trigger_pin=18, echo_pin=24)
distancia = sensor.medir_distancia()
print(f"Distancia: {distancia} cm")
