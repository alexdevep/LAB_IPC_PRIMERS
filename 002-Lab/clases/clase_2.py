class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name): #Constructor
        self.name = name