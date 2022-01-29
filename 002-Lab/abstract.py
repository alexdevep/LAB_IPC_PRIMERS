from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    @abstractmethod
    def showName(self):
        pass

    @abstractmethod
    def showAge(self):
        pass


class Man(Person): #superclass into

    def __init__(self, name, height):
        self.height = height
        # Person.__init__(self, name, 10)
        super().__init__(name, 10)  # same as Person.__init__(self, name, 10)
        # basically used to call the superclass init . This is used incase you want to call subclass init
        # and then also call superclass's init.

    def showIdentity(self):
        return self.name, self.age, self.height #Makes possible call the other params

    def showName(self):
        pass

    def showAge(self):
        pass


a = Man("piyush", "179")

#Entiendase en el tipo de acceso que manejan las clases abstractas
print(a.showIdentity())
print(a.height)
print(a.name)
print(a.age)

###########################################
# ENCAPSULAMIENTO Y ABSTRACTA SON SIMILARES
###########################################