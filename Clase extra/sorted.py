
desordenado = [5, 2, 3, 1, 4]
numeros = [16, 4, 9, 1, 3, 20, 8]

print("=== Funcion Sort ===")

ordenado = desordenado.sort()
print(desordenado)
print(numeros.sort())
print("Dejen su F en chat, no funciona en esta version de python que tengo :(")

print("=== Funcion Sorted ===")
palabras = ["hola", "coche", "avión", "manzana", "perro", "gato"]
word = sorted(palabras)
print(palabras)
print(word)




print("=== Ordenamiento por inserción ===")
#Función para mostrar estado de la lista
def mostrarLista(lista, lon):
	listaordenada=""
	for i in range(0,lon):
		listaordenada+=str(lista[i])+" "
	print(listaordenada)   
	
arreglo = [5,2,4,1,3];
print(arreglo)
#Recorrer el arreglo
for i in range(1,len(arreglo)):
	clave = arreglo[i]
	j = i-1
	#Comparar el valor seleccionado con todos los valores anteriores
	while (j>=0 and arreglo[j] > clave):
		#Insertar el valor donde corresponda
		arreglo[j+1] = arreglo[j]
		j = j-1
	arreglo[j+1] = clave
	mostrarLista(arreglo, len(arreglo))

mostrarLista(arreglo, len(arreglo))  



print("=== Ordenamiento por burbuja ===")
def burbuja(lista):
    #Establecemos la variable intercambio en True para entrar en el bucle al menos una vez
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(lista) -1):
            if lista[i] > lista [i + 1]:
                #Intercambiamos los datos
                aux = lista[i]
                lista[i]=lista[i + 1]
                lista[i + 1]=aux
                #Cambiamos a True la variable ya que ha habido un intercambio
                intercambio = True
        print(lista)

numeros = [5,2,4,1,3]
print(numeros)
burbuja(numeros)
print(numeros)


print("=== Ordenamiento Quicksort ===")
miLista = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36]

def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0] #34
        for i in lista:
            if i < pivote:              #pivote=34                                              #
                izquierda.append(i)     #[19,12,28]
            elif i == pivote:
                centro.append(i)        #[34]
            elif i > pivote:
                derecha.append(i)       #[94,58,95,37,...]
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort([19,12,28])+centro+sort([94,58,95,37,...])
    else:
      return lista

print(miLista)
print(sort(miLista))

