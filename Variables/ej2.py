from mailbox import NoSuchMailboxError


#Método 1
nombre = input("Introduzca el nombre: ")
dni = input("Introduzca el DNI: ")
edad = input("Introduzca la edad: ")

print(f"\nEl nombre es {nombre}, el dni es {dni} y la edad es {edad}\n" )

#Método 2
nombre, dni, edad = input("Introduca nombre, dni y edad: ").split()
print(f"\nEl nombre es {nombre}, el dni es {dni} y la edad es {edad}\n")