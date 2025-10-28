"""
    Ejemplo
"""
# Solicitar la edad de la persona
print("Ingrese la edad de la persona:")
edad = input()
edad = int(edad)

# Solicitar el nombre de la persona
nombre = input("Ingrese el nombre de la persona: ")

# Solicitar la ciudad de nacimiento
ciudad = input("Ingrese la ciudad de nacimiento de la persona: ")


# Condicional para verificar edad y ciudad
if edad >= 18 and ciudad == "Loja":
    print(f"Acceso correcto {nombre}")
else:
    print(f"Acceso incorrecto {nombre}")
