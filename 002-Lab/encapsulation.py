# Creating a base class
class Base:
    def __init__(self):
 
        # Protected member
        self._a = 2
        self._b = 'testing'
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        #Calling protected member of base class
        print("Llamando la variable protegida de la base: ",self._a)
 
        # Modify the protected variable:
        self._a = 3
        #Calling modified protected member outside class
        print("Variable modificada y llamada fuera de esta clase",self._a)
 
 
obj1 = Derived()
obj2 = Base()
 
# Calling protected member
# Can be accessed but should not be done due to convention
print("Accesando al miembro protegido de obj1: ", obj1._a)
 
# Accessing the protected variable outside
print("Accesando al miembro protegido de obj2: ", obj2._a)

print("Puede acceder con obj1: ", obj1._b)
print("Puede acceder con obj2: ", obj2._b)

##########################################
#ENCAPSULAMIENTO Y ABSTRACTA SON SIMILARES
##########################################