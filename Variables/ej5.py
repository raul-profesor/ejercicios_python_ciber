frase = input("Introduzca su frase: ")
old, new = input("\nIntroduzca, separadas por comas, la letra a reemplazar y la letra de reemplazo: ").split(",")

print("\n" + frase.replace(old, new))