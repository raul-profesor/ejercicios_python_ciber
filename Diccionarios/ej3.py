usuarios = {  
    "mmacia": {  
        "nombre": "Martí",  
        "apellido": "Macià",  
        "password": "123123"  
    },  
    "fmuguruza": {  
        "nombre": "Fermín",  
        "apellido": "Muguruza",  
        "password": "654321"  
    },  
    "cbiriukov": {  
        "nombre": "Chechu",  
        "apellido": "Biriukov",  
        "password": "123456"  
    }  
}

usuario = input("Introduzca usuario: ")
contrasenya = input("Introduzca contraseña: ")

if usuario in usuarios.keys() and contrasenya == usuarios[usuario]["password"]:
    nom = usuarios[usuario]["nombre"]
    cognom = usuarios[usuario]["apellido"]
    print(f"Bienvenido {nom} {cognom}")
else:   
    print("Usuario o contraseña incorrecta")