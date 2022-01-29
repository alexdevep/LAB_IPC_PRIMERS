
class Humano(): #Creamos la clase Humano

    altura = ''
    
    def __init__(self, edad, nombre, ocupacion): #Constructor #Definimos el parametro edad , nombre y ocupacion
        self.edad = edad # Definimos el atributo edad
        self.nombre = nombre # Definimos el atributo nombre
        self.ocupacion = ocupacion #Definimos el atributo ocupacion
        
        #Creación de un nuevo método
    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}") #Mensaje
        print(presentacion.format(self.nombre, self.edad, self.ocupacion)) #Usamos FORMAT

#Instanciando la clase
#Persona1 = Humano(31, "Pedro", "Desocupado") 
#Llamamos al método
#Persona1.presentar() 
#Asignar valores a los atributos del objeto
#Persona1.altura = 1.75
#print('La altura es ',Persona1.altura, ' metros')