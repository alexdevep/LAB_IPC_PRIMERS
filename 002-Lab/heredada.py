
class Person():#
       
    # Constructor
    def __init__(self, name):
        self.name = name
   
    # To get name
    def getName(self):
        return self.name
   
    # To check if this person is an employee
    def isEmployee(self):
        return False
   
   
# Heredando de la clase Person
class Employee(Person):
   
    #def getName(self):
    #    return super().getName()
        
    def isEmployee(self):
        return True
   
# Driver code
emp = Person("Josue")  # An Object of Person
print(emp.getName(), emp.isEmployee())
   
emp = Employee("Pablo") # An Object of Employee
print(emp.getName(), emp.isEmployee())
