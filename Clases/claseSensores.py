from ClaseLista import lista
import datetime

class sensores(lista.Lista):
    
    def __init__(self):
        super().__init__()
        self.clave=[]
        
    def add_Sensores(self):
        
        
          print("Hola usuario :D se detecto un sensor nuevo")
          sensor_id=input(f"Por favor,proporcione la clave ")
          self.clave.append(sensor_id)
          tipo=input(f"Por favor,proporcione el tipo ")
          
          ubicacion = input(f"Por favor, proporcione una ubicación para el sensor  ")
          descripcion = input(f"Por favor, proporcione una descripción para el sensor  ")
                

                # Agregar el sensor a la lista
          sensor_info = {"Clave": sensor_id, "tipo": tipo, "ubicacion": ubicacion, "descripcion": descripcion, "fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
          self.lista.append(sensor_info)
          
          super().crearjson(self.clave,"claves")
          super().crearjson(self.lista,"sensorinfo")
          print("el sesnor fue registrado correctamente: ")
        
        
        
     
    
    