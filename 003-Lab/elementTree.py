
import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()

print('Item #2 attribute:')
print(root[0][1].attrib)            #Obtenemos objeto
print(root[0][1].attrib['name'])    #Obtenemos el valor


print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)
        print(subelem.attrib['name'])   # Especificando el atributo

print('\nItem #2 data:')
print(root[0][1].text)

print('\nAll item data:')
for elem in root:
    for subelem in elem:
        print(subelem.text)

#=======================================================================================
## Contando elementos del xml
print('\nCantidad de elementos:')
print(len(root[0]))

#=======================================================================================
## Buscando elementos del xml
print('\nBuscando elementos del xml:')
for elem in root:
    for subelem in elem.findall('item'):    # Cambiar 'item' a 'nodo'; agregar al xml 
                                            # <nodo name="nodox">nodo_xvalue</nodo>
                                            # <item name="item3">item_3value</item>
        print(subelem.attrib)
        #print(subelem.get('name'))

#=======================================================================================
