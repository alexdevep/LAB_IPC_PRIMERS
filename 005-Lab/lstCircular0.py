class Node(object):
    # Crear una clase de nodo
    def __init__(self, data):
        self.data = data
        self.next = None
 
class circular_simple(object):
    # Crear una clase que cree una lista circular vinculada
    
    def __init__(self):
        self.head = None
 
    def is_empty(self):
        # Determine si la lista circular está vacía
        return self.head is None
 
    def agregarInicio(self, data):
        # Agregar un nodo en la cabeza
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            # Mueva el puntero al nodo de cola
            while cur.next is not self.head:
                cur = cur.next
            # El nodo de cola apunta al nuevo nodo
            cur.next = node
            # El nuevo nodo apunta al nodo principal original
            node.next = self.head
            # Luego dele el título del nodo principal al nuevo nodo
            self.head = node
 
    def agregarFinal(self, data):
        # Agregar un nodo al final
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            # Mueve el puntero al final
            while cur.next is not self.head:
                cur = cur.next
            # El nodo de cola apunta al nuevo nodo
            cur.next = node
            # El nuevo nodo apunta al nodo principal
            node.next = self.head
 
    def recorrer(self):
        # Recorriendo la lista vinculada
        if self.is_empty():
            return
        cur = self.head
        print(cur.data)
        while cur.next != self.head:
            cur = cur.next
            print(cur.data)


 
lists = circular_simple()
lists.agregarFinal(2)
lists.agregarInicio(1)
lists.agregarInicio(0)
lists.agregarFinal(3)
lists.recorrer()