from ClaseLista import lista
import datetime

class sensores(lista.Lista):
    
    def __init__(self):
        super().__init__()
        self.clave=[]
        
    def add_Sensores(self,CLAVE):
        
        
          print("Hola usuario :D se detecto un sensor nuevo")
          
          
          tipo=input(f"Por favor,proporcione el tipo CLAVE{CLAVE} : ")
          
          ubicacion = input(f"Por favor, proporcione una ubicación para el sensor CLAVE{CLAVE} :  ")
          descripcion = input(f"Por favor, proporcione una descripción para el sensor CLAVE{CLAVE} : ")
                

                # Agregar el sensor a la lista
          sensor_info = {"Clave": CLAVE, "tipo": tipo, "ubicacion": ubicacion, "descripcion": descripcion, "fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
          self.lista.append(sensor_info)
          
          
          super().crearjson(self.lista,"sensorinfo")
          print("el sesnor fue registrado correctamente: ")
        
        
        
     
    
    