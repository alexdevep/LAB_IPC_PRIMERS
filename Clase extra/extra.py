
cadena = "¡Hola, mundo!"

# Método 1, sin índice
print("\n================== SIN INDICE ====================\n")
for caracter in cadena:
    print(caracter)

# Método 2, con índice
print("\n================== CON INDICE ====================\n")
for indice in range(len(cadena)):
    caracter = cadena[indice]
    print("En el índice {} tenemos a '{}'".format(indice, caracter))

print("\n================== PESO DE STRINGS ====================\n")

def comparar(name, name2):
    if(len(name) > len(name2)):
        print('El segundo string se va a recorrer')
        for pos in range(len(name2)):
            print('Comparando {} con {}'.format(name2[pos], name[pos]))
            if ord(name2[pos]) < ord(name[pos]):
                print('primer caracter va antes')
                return name2
            elif ord(name2[pos]) == ord(name[pos]):
                print('son iguales')
            else:
                print('segundo carcater va antes')
                return name
    else:
        print('El primer string se va a recorrer')
        for pos in range(len(name)):
            print('Comparando {} con {}'.format(name[pos], name2[pos]))
            if ord(name[pos]) < ord(name2[pos]):
                print('primer caracter va antes')
                return name
            elif ord(name[pos]) == ord(name2[pos]):
                print('son iguales')
            else:
                print('segundo carcater va antes')
                return name2

name = 'Carlos'     #//6char
name2 = 'Carles'    #//7char

respuesta = comparar(name,name2)
if respuesta is None:
    print('AMBOS SON IGUALES')
else:
    print('El string que va primero es : {}'.format(respuesta))

            



