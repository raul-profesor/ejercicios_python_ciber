estudiantes_notas = {}
lista_aprobados = []
lista_suspensos = []
notas_sumadas=0

for i in range(1,4):
    estudiantes_notas[i] = {}
    nom, calif = input("Introduzca nombre y nota, separados por comas: ").split(",")
    estudiantes_notas[i]['nombre'] = nom
    estudiantes_notas[i]['nota'] = calif

for alumno in estudiantes_notas:
    calificacion = int(estudiantes_notas[alumno]['nota'])
    nombre_alumno = estudiantes_notas[alumno]['nombre']
    if calificacion >= 5:
        lista_aprobados.append(nombre_alumno)
    else:
        lista_suspensos.append(nombre_alumno)
    notas_sumadas = calificacion + notas_sumadas
    
print("Lista de aprobados:" )
for aprobado in lista_aprobados:
    print(aprobado)
print("\nLista de suspensos:" )
for suspenso in lista_suspensos:
    print(suspenso)    
    
print("\nAlumnos aprobados:" + str(lista_aprobados))
print("Alumnos suspensos:" + str(lista_suspensos))

nota_media = notas_sumadas/len(estudiantes_notas)
print(f"\nLa nota media de la clase ha sido {nota_media}")