
class node:
    def __init__(self, data = None, siguiente = None):
        self.data = data
        self.siguiente = siguiente

# Creamos la clase lista_simple
class lista_simple: 
    def __init__(self):
        self.root = None
    
    # Método para agregar elementos en el frente de la linked list
    def insertar_inicio(self, data):
        self.root = node(data=data, siguiente=self.root)  

    # Método para agregar elementos al final de la linked list
    def insertar_fin(self, data):
        if self.root is None:
            self.root = node(data=data)
            return
        aux = self.root
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = node(data=data)
    
    # Método para eleminar nodos
    def eliminar_nodo(self, key):
        aux = self.root
        prev = None
        while aux and aux.data != key:
            prev = aux
            aux = aux.siguiente
        if prev is None:
            self.root = aux.siguiente
        elif aux:
            prev.siguiente = aux.siguiente
            aux.siguiente = None

    # Método para obtener el ultimo nodo
    def obtener_ultimo_nodo(self):
        temp = self.root
        while(temp.siguiente is not None):
            temp = temp.siguiente
        return temp.data

    # Método para imprimir la lista de nodos
    def imprimir_lista( self ):
        node = self.root
        while node != None:
            print('Nodo: ',node.data)
            node = node.siguiente

    def ordenacion(self):
        intercambio = True
        contador = 0
        while intercambio:
            intercambio = False
            temp = self.root
            while temp.siguiente != None:
                temp2 = temp.siguiente
                if temp.data > temp2.data:
                    aux = temp.data
                    temp.data = temp2.data
                    temp2.data = aux
                    intercambio = True
                contador = contador + 1
            contador = contador + 1

            if(contador < 25):
                print("Trono!")
                break
    
    def ordenamiento(self): #Se ordenan los nodos
        cambio = True
        while cambio:
            actual = self.root
            anterior = None
            siguiente =self.root.siguiente
            cambio = False
            while siguiente != None:
                # print("Segundo while!")
                if actual.data >= siguiente.data: #Ordenar por strings
                    cambio = True
                    if anterior != None: #Significa estamos en el primer nodo
                        sig = siguiente.siguiente
                        anterior.siguiente = siguiente
                        actual.siguiente = sig #apuntor siguiente de nodo actual
                    else:
                        sig = siguiente.siguiente
                        self.root = siguiente
                        siguiente.siguiente = actual
                        actual.siguiente = sig #apuntador siguiente de nodo segundo
                    anterior = siguiente
                    siguiente = actual.siguiente
                else:
                    anterior = actual
                    actual = siguiente
                    siguiente = siguiente.siguiente
                        


print("Lista añadiendo al final")
s = lista_simple() # Instancia de la clase
s.insertar_fin(5) # Agregamos un elemento al inicio del nodo
s.insertar_fin(2) # Agregamos un elemento al inicio del nodo
s.insertar_fin(1) # Agregamos otro elemento al inicio del nodo
s.insertar_fin(3) # Agregamos otro elemento al inicio del nodo
s.insertar_fin(4) # Agregamos otro elemento al inicio del nodo
s.imprimir_lista() # Imprimimos la lista de nodos
s.ordenamiento()
print("Ya ordenado!")
s.imprimir_lista()
