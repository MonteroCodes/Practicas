7
# Programa que verifica si una persona es mayor de edad y de un género específico

# Solicitar edad y género al usuario
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (hombre o mujer): ").lower()  # Convertimos a minúsculas para facilitar la comparación

# Verificar condiciones
if edad >= 18 and (genero == "hombre" or genero == "mujer"):
    print(f"Eres un {genero} mayor de edad.")
else:
    print("No cumples con los criterios.")
