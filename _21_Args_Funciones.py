def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
#4 Argumentos
colores('lila', 'negro', 'rojo')
#3 Argumentos
colores('rosa')
#1 Argumento
colores('marrón', 'naranja')
#2 Argumentos

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores("Verde","Azul")

def suma(*args):
	total=args[0]+args[1]+args[2]+args[3]+args[4]
	print("La suma de todos los numeros te da como resultado: ",total)
	
suma(34,455,67,12,10)
	
	
