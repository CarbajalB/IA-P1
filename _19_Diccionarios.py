#Practica 28 Diccionarios
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

consulta1 = teclado2["Modelo"]
consulta2 = teclado2['Precio']

print("El modelo ",consulta1, " cuesta ",consulta2,"$")

#Practica 29 Diccionarios for

for x in teclado1:
    print(x ," = ",teclado1[x])

#Practica 30 Metodos con diccionarios

del teclado1
del teclado2["Categoría"]
del teclado2["Precio"]
print(teclado2["Modelo"])