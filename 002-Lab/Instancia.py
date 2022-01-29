
#Importando clases
from clases.clase_1 import Humano
from clases.clase_2 import Dog


#Creando Instancias
print('*********************************')
print('Creando instancias del objeto Dog')
print('*********************************')
d = Dog('Fido')
e = Dog('Buddy')
print('*********************************')
print('Imprimiendo atributos del objeto')
print('*********************************')
print(d.kind)
print(e.kind)   
print(d.name)
print(e.name)

print('\n\n\n')

print('************************************')
print('Creando instancias del objeto Humano')
print('************************************')
Persona1 = Humano(31, "Raymundo", "Desconocido") #Instancia
#Llamamos al método
print('********************************************')
print('Imprimos los atributos a traves de un metodo')
print('********************************************')
Persona1.presentar() 
print('******************************')
print('Asignamos un valor a la altura')
print('******************************')
Persona1.altura = '1.78'
print('Y se me olvido comentarles que mido ',Persona1.altura,' metros.')
