lista_1 = []
lista_2 = []
lista_def = []

print("Introduzca 5 números: ")
for i in range(5):
    lista_1.append(input())
    
print("Introduzca otros 5 números")
for i in range(5):
    lista_2.append(input())

for item in lista_1:
    comparacion = lista_2.count(item)
    if comparacion == 1:
        lista_def.append(item)
        
print(lista_def)
    
    