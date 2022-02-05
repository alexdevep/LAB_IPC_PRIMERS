
from xml.dom import minidom                     # Importamos la libreria

mydoc = minidom.parse('items.xml')              # Creamos un objeto del documento

items = mydoc.getElementsByTagName('item')      # Obtenemos los nodos con el tag 'item'

print('Item #2 atribute.')
print(items[1].attributes['name'].value)        # Obtenemos el valor del atributo especificado

print('\nAll attributes.')
for elem in items:                              # Imprimiendo los valores de los atributos
    print(elem.attributes['name'].value)

print('\nItem #2 data: ')                       # Obtenemos el valor de los datos del nodo
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

print('\nAll item data:')
for elem in items:
    print(elem.firstChild.data)


## Contando elementos del xml
print('Cantidad de elementos del xml:')
print(len(items))

# Cuidado al tipear funciones nativas, utilizar siempre que se pueda el autocompletado.