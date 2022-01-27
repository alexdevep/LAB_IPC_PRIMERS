#Execute command
#python3 test.py

print('********************************')
print('******* TIPO DE VARIABLE *******')
print('********************************')
print("Hello, World!")
a = 1                   #Variable tipo int
b = 'dos'               #Variable tipo string
c = 3.14                #Variable tipo float
d = True                #Variable tipo booleano
e = False               #Variable tipo booleano
f = [a,b,c,d,e]         #Variable tipo lista
g = None
print('************ Impresion tipo ************')
print(type (a), a)
print(type (b), b)
print(type (c), c)
print(type (d), d)
print(type (e), e)
print(type (f), f)
print(type (g), g)

print('************ Impresion For ************')
print([(x, type(x)) for x in f])

print('Cambio de variable')
print(type (f))
g=1
print(type(g))
g = 'nuevo valor'
print(type (g))

print('********************************')
print('*********** FUNCIONES **********')
print('********************************')
def impresion(info):
    print(info)
    print(info)

def moreThan(v1, v2):
    if(v1 > v2):
        print('El primer valor es mayor que el segundo valor.')
    else:
        print('El segundo valor es mayor o igual que el primer valor.')

def sumados(a, b):
    suma = a + b
    return suma

impresion('Spam')
impresion(17)
moreThan(5,7)
x = sumados(3,5)
print(x)


print('********************************')
print('****** CICLOS O ITERACIONES ****')
print('********************************')
n = 5
while(n > 0):
    if n == 3:
        break
    print('iteracion: ', n)
    n = n - 1
print('!Fin!')

print('********************************')
amigos = ['Joseph', 'Glenn', 'Sally', 'Alex']

n = 0

for amigo in amigos:
    #amigo='joseph' -> 'glenn' -> 'Sally'
    print('[',n,']Feliz dia : ', amigo)
    n=n+1
print('Final de linea')