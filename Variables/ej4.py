inicio, long, frase = input("Introduce dos números y una frase, separado por comas: ").split(",")

print(frase[int(inicio):int(inicio)+int(long)])