# Programa para jugar a adivinar un número
"""Este es un codigo de programa para adivinar un numero al azar
del 1 al 100, no hay limites de intentos, puedes realizarlo hasta acertar el numero,
y si aciertas te dira felicidades, haz acertado en tantos intentos. Tambien de la opcion
de elegir si deseas seguir con el juego nuevamente o si deseas salir"""
import random

# Función para jugar al juego de adivinar el número
def jugar_adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Ingresa un número entre 1 y 100: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades, has adivinado el número en {intentos} intentos!")
            break
        elif intento < numero_secreto:
            print("El número es más alto.")
        else:
            print("El número es más bajo.")

# Menú de opciones
while True:
    print("Juego de adivinar el número")
    print("1. Jugar")
    print("2. Salir")
    opcion = input("Ingrese una opción (1-2): ")

    if opcion == "1":
        jugar_adivinar_numero()
    elif opcion == "2":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")