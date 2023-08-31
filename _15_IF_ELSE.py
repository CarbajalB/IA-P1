#Practica 20 IF
num1 = 15
num2 = 20

if num1 <= num2:
	print('Se ejecuta el 1er if.')
	
num3 = 1450
num4 = 60

if num3 > num4:
	print('Se ejecuta el 2do if.')
	
num5 = 60
num6 = 60

if num1 != num6:
	print('Se ejecuta el 3er if.')
	
#Practica 21 IF ELSE
color = "rojo"

if color != "rojo":
	print("El color no es rojo")
else:
	print("El color es rojo")

#Practica 22

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad < 45:
	print("Eres de mediana edad")
elif edad >= 45 and edad < 100:
	print('Eres mayor de edad.')
elif edad >= 100 and edad <= 120:
	print("Ya estas muy muy viejo.")
else:
	print('Edad no válida.')