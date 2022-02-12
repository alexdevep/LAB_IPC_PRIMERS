
class node:
    def __init__(self, data = None, siguiente = None): #Constructor
        self.data = data #Este el atributo, puede mas atributo
        self.siguiente = siguiente  #Apunta al siguiente nodo

# Creamos la clase lista_simple
class lista_simple: 
    def __init__(self):#constructor
        self.root = None # root es el primer apuntador

    # Método para agregar elementos en el frente de la lista simple
    def insertar_inicio(self, data):
        self.root = node(data=data, siguiente=self.root)  

    # Método para agregar elementos al final de la lista simple
    def insertar_fin(self, midato): 

        if self.root is None: #Si root es nula. Esto pasa si y si solo es el primer nodo que se esta agregando a la lista
            self.root = node(data=midato) #Creando mi primer y asignando a root
            return #finaliza
        #En caso de que root ya tenga un nodo
        auxRoot = self.root
        while auxRoot.siguiente: #Mientras exista un nodo
            auxRoot = auxRoot.siguiente
        auxRoot.siguiente = node(data=midato) #mi nuevo nodo
    
    # Método para imprimir la lista de nodos
    def imprimir_lista( self ):
        nodeAux = self.root #Obtiene raiz o inicial de mi lista
        while nodeAux != None:
            print('Nodo: ',nodeAux.data)
            nodeAux = nodeAux.siguiente


print("Lista añadiendo al final")
s = lista_simple() # Instancia de la clase
s.insertar_fin(5) # Agregamos un elemento al inicio del nodo
s.insertar_fin(8) # Agregamos un elemento al inicio del nodo
s.insertar_fin(9) # Agregamos otro elemento al inicio del nodo
s.imprimir_lista() # Imprimimos la lista de nodos

print("Lista añadiendo al final")
s0 = lista_simple() # Instancia de la clase
s0.insertar_inicio(5) # Agregamos un elemento al final del nodo
s0.insertar_inicio(8) # Agregamos un elemento al final del nodo
s0.insertar_inicio(9) # Agregamos otro elemento al final del nodo
s0.imprimir_lista() # Imprimimos la lista de nodos