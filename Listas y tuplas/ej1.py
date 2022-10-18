lista_original = [12, 23, 5, 29, 92, 64]

lista_original.insert(0,lista_original[len(lista_original) - 1])
lista_original.pop()
print(lista_original)

item = lista_original[1]
lista_original.remove(item)
lista_original.append(item)
print(lista_original)

lista_original.insert(0, 14)
print(lista_original)


suma = 0
for item in lista_original:
    suma = suma + item
lista_original.append(suma)    
print(lista_original)

fusion = [4, 11, 32]
lista_original.extend(fusion)
print(lista_original)


print("\n" + "Impares método 1")
lista_copia = []
for item in lista_original:
    if item % 2 ==0:
        lista_copia.append(item)
    else:
        pass
print(lista_copia)

print("\n" + "Impares método 2, con list comprehensions")
lista_original = [item for indice, item in enumerate(lista_original) if item % 2 ==0]
print(lista_original)

lista_original.sort()
print(lista_original)

lista_original.clear()
print(lista_original)
        