numero = int(input("Introduce un número del 1 al 10: "))

# Método 1
tabla = f"""{numero} x 1 = {numero*1}
{numero} x 2 = {numero*2}
{numero} x 3 = {numero*3}
{numero} x 4 = {numero*4}
{numero} x 5 = {numero*5}
{numero} x 6 = {numero*6}
{numero} x 7 = {numero*7}
{numero} x 8 = {numero*8}
{numero} x 9 = {numero*9}
{numero} x 10 = {numero*10}"""

print(tabla+'\n')

#Método 2 
for i in range(1,10):
    print(f"{numero} x {i} = {numero*i}")