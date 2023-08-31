tupla = ("Azul","Rojo", "Amarillo", "Morado")

col=input("Ingresa un color: \n")
if col == tupla[0]:
    print("El color ",tupla[0]," esta admitido")
elif col == tupla[1]:
    print("El color ",tupla[1]," esta admitido")
elif col == tupla[2]:
    print("El color ",tupla[2]," esta admitido")
elif col == tupla[3]:
    print("El color ",tupla[3]," esta admitido")
else:
    print("El color no etsa admitido")