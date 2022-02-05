
# Writing document xml with ElemtTree

import xml.etree.ElementTree as ET

# Create the file structure
data = ET.Element('data')               #Nodo padre #Contiene toda la estructura xml

items = ET.SubElement(data, 'items')    #Nodo hijo

item1 = ET.SubElement(items, 'item')    #Nodo hijo de items
item2 = ET.SubElement(items, 'item')    #Nodo hijo de items
item3 = ET.SubElement(items, 'item')    #Nodo hijo de items
item1.set('name', 'item1')
item2.set('name', 'item2')
item3.set('nuevo','Nuevo Atributo')
item1.text = 'item_1value'
item2.text = 'item_2value'
item3.text = 'Texto de item3'

# Create a new XML file
mydata = ET.tostring(data)
myfile = open("items2.xml", "w")            #Si el archivo no existe lo crea, y si existe lo reescribe
#myfile.write(mydata)                        # Error de casteo en funcion write()
myfile.write(mydata.decode("utf-8"))       # Decodifica a un string de bytes