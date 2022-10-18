nombres = {
    'Mikel': 3,
    'Ana': 8,
    'Amaia': 12,
    'Unai': 5,
    'Jon': 8,
    'Ainhoa': 7,
    'Maite': 5
  }

lista_valores = []
for nombre, valor in nombres.items():    
    if lista_valores.count(valor) == 0:        
        lista_valores.append(nombres.get(nombre))
print(lista_valores)