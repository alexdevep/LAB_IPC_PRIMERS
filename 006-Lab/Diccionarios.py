
d = {}
print(type(d))

d = {"Enero":1, "Abril":4, "Agosto":8, "Diciembre":12}
print(type(d))

print("---------------- Insertando nuevos elementos:  ----------------")
print(d)
d["Marzo"] = 3
print(d)

print("---------------- Obteniendo un elemento e imprimirlo ----------------")
print(d.get("Abril"))
print(d.get("Noviembre")) #No existe objeto

print("---------------- Devuelve la lista en pares clave:valor ----------------")
print(d.items())

print("---------------- Devuelve la lista de claves ----------------")
print(d.keys())

print("---------------- Devuelve la lista de valores ----------------")
print(d.values())

print("---------------- Elimina una clave especifica y la devuelve ----------------")
print(d)
print(d.pop("Agosto"))
print(d)
#print(d.pop("Febrero")) #No existe la clave

try:
    print(d.pop("Febrero")) #No existe la clave
except:
    print("[Error] Ha ocurrido un error")

print("---------------- Agrega un nuevo par clave:valor ----------------")
print(d)
d.update({"Junio":6})
print(d)

print("---------------- Devuelve la cantidad de elementos dentro del diccionario ----------------")
print(len(d))

print("---------------- Eliminando elementos del diccionario ----------------")
print(d)
d.clear()
print(d)

print("---------------- Creando un diccionarion con el constructor dist() ----------------")
d = dict(Enero=1, Abril=4, Agosto=8, Diciembre=12)
print(type(d))
print(d)
d = dict({"Enero":1, "Abril":4, "Agosto":8, "Diciembre":12})
print(type(d))

