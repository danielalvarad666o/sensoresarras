
from Clases import claseUltrasonico,claseTemperatura,claseLed
led=claseLed.Led(21)

class interface:
    
    
    def led():
      try:
        print("Opciones del led")
        print("--"*100)
        print("1)Prender led")
        print("2)Apagar led")
        opcion=int(input("Escoje una opcio: "))
        if opcion==1:
         led.encender()
        elif opcion==2:
            led.apagar()
        else:
            print("Opcion no valida ")
      except:
          print("Opcion no valida")