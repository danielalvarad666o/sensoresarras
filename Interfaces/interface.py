
from Clases import claseLed,claseUltrasonico,claseTemperatura
import time
led=claseLed.Led(21)
sensorU = claseUltrasonico.SensorUltrasónico(trigger_pin=18, echo_pin=24)
sensorT= claseTemperatura.SensorTemperaturaHumedad(4)

class interface:
    
    
    def led(self):
      try:
        print("Opciones del led")
        print("--"*100)
        print("1)Prender led")
        print("2)Apagar led")
        op=int(input("Escoje una opcio: "))
        if op==1:
         led.encender()
        elif op==2:
            led.apagar()
        else:
            print("Opcion no valida ")
      except:
          print("Opcion no valida")
       
       
       
          
    def leersesnorUltrasonico(self):
     tiempo_anterior = time.time()

     while True:
        distancia = sensorU.medir_distancia()
        tiempo_actual = time.time()

        # Imprimir resultados si han pasado 8 segundos desde el último mensaje
        if distancia and tiempo_actual - tiempo_anterior >= 15:
            print(f"Distancia: {distancia} cm")

            # Preguntar si desea continuar
            respuesta = input("¿Desea continuar? (s/n): ")
            if respuesta.lower() == "n":
                break

            tiempo_anterior = tiempo_actual
     
    def leersensorTemperatura(self):
        tiempo_anterior = time.time()
        while True:
            temperatura=sensorT.medir_temperatura_humedad()
            tiempo_actual=time.time()
            # Imprimir resultados si han pasado 8 segundos desde el último mensaje
            if temperatura and tiempo_actual - tiempo_anterior >= 15:
             print(temperatura)
             
            respuesta = input("¿Desea continuar? (s/n): ")
            if respuesta.lower() == "n":
                break
