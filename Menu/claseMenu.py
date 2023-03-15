class Menus: 
    
    def Optiones(self):
     try:
        print("1)Agregar sensores")
        print("2)Led opciones")
        print("3)Sensor Temperatura opciones")
        print("4)Sensor Ultrasonico opciones")
        print("5)Ver sensores registrados")
        print("6)Salir")
        print("")
        option =int(input("Escoje una opcion: "))
        return option
     except:
         return "Opcion no valida intenta de nuevo"
        