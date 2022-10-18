lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
cuenta = dict()
cuenta2 = dict()


# Método 1
for item in lista:
    # Con .get estableemos un valor por defecto para la clave
    cuenta[item] = cuenta.get(item, 0) + 1   
print(cuenta)

# Método 2
for item in lista:
    if item in cuenta2:
        cuenta2[item]=cuenta2[item]+1
    else:
        cuenta2 [item] = 1
print("\n" + str(cuenta2))
