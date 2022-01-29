class India():
    def capital(self):
        print("La capital de India es Nueva Delhi.")
 
    def language(self):
        print("En India es muy comun el lenguaje Hindi.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("En USA se habla ingles.")
 
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa): #obj_ind, obj_usa, es posible gracias a la ambiguedad de python, en otros no es posible
    country.capital()
    country.language()

#Muy comun hacer uso de Interface en otros lenguajes