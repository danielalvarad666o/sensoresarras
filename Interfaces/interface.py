
from Clases import claseLed,claseUltrasonico,claseTemperatura
import time
led=claseLed.Led(21)
sensorU = claseUltrasonico.SensorUltrasónico(trigger_pin=18, echo_pin=24)
sensorT= claseTemperatura.SensorTemperaturaHumedad(5)

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
     
        i = 0
        while i < 8:
         distancia = sensorU.medir_distancia()
         print(f"Distancia: {distancia} cm")
         i += 1
    
         if i == 8:
          respuesta = input("¿Desea continuar? (s/n): ")
          if respuesta.lower() == "n":
            
                break
          else :
              i=0

            
     
    def leersensorTemperatura(self):
        
        i = 0
        while i < 8:
          temperatura = sensorT.medir_temperatura_humedad()
    # Imprimir resultados si han pasado 15 segundos desde el último mensaje
          print(temperatura)
          i += 1
    
          if i == 8:
             respuesta = input("¿Desea continuar? (s/n): ")
             if respuesta.lower() == "n":
               break
             else:
              i = 0 # Reiniciar i si el usuario desea continuar
