#Practica 24 While
x = 0

while x <= 15:
    print(x)
    x=x+5

x = 0

while x >= -100:
    print(x)
    x=x-20


x = 10

while x >= 0:
    print("El valor del bucle es: ",x)
    x=x-1

#Practica 25 While if
x = 0

while x <= 30:
    if x == 4 or x == 6 or x == 10:
        print("Se saltó el valor ", x , "de x")
    else:
        print(x)
    x=x+1
    if x == 15:
        print("Se rompió la ejecución del bucle cuando x valia: ",x)
        break
   