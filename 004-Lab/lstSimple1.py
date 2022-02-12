
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


def main():

    print("Lista añadiendo al final")
    s = lista_simple() # Instancia de la clase
    
    operacion = True;

    while(operacion):
        print("============================ MENU ============================")
        print("Ingrese la opcion que desee:")
        print("1 - Ingresar nodo al inicio")
        print("2 - Ingresar nodo al final")
        print("3 - Mostrar nodo")
        print("0 - Salir")
        print("==============================================================")
        operacion = int(input()) #Recibe string y lo convierte a int

        if operacion == 1:
            print('Ingresando nuevo nodo a la lista.')
            print('Ingrese el valor: ')
            valor = input() #Recibe string
            s.insertar_inicio(valor) # Agregamos un elemento al frente del nodo
        if operacion == 2:
            print('Ingresando nuevo nodo a la lista.')
            print('Ingrese el valor: ')
            valor = input() #Recibe string
            s.insertar_fin(valor) # Agregamos un elemento al frente del nodo
        elif operacion == 3:
            print('Mostrando informacion de lista.')
            s.imprimir_lista() # Imprimimos la lista de nodos    
        elif operacion == 0:
            print('Saliendo.')
            operacion = False     
        else:
            print('Debe Seleccionar una opccion del menu.')

    return 0

main()