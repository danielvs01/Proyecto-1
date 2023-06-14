import random

puntos_jugador1 = 0
puntos_maquina = 0
deuce = 1
puntaje_juga1_deuce = 0
puntaje_maqui_deuce = 0
go = 0


print("\n---- Menú Principal ----")
print("\n1. Jugar contra otro jugador")
print("\n2. La máquina juegue contra la máquina")
opcion = input("\nSeleccione una opción: ")

if opcion == "1":
    nombre_jugador = input("\nEscriba el nombre del jugador 1: ")
    nom_jugador2 = input("\nEscriba el nombre del jugador 2: ")
else:
    nombre_jugador = "La Máquina"
    nom_jugador2 = "Máquina"

while True:
    if opcion == "1":
        input("\nPresione la tecla ENTER para tirar la pelota \n")
    else:
        print()

    punto_para = random.choice([0,1])

    if punto_para == 0:
        puntos_jugador1 += 1
    else:
        puntos_maquina += 1

    if puntos_maquina == puntos_jugador1 and puntos_maquina == 3 and puntos_jugador1 == 3:
        print("Deuce!")
        deuce = 2
    elif puntaje_juga1_deuce >= puntaje_maqui_deuce + 2:
        print(nombre_jugador + " ganó el juego")
        break
    elif puntaje_juga1_deuce + 2 <= puntaje_maqui_deuce:
        print(nom_jugador2 + " ganó el juego")
        break

    if puntos_jugador1 > 3 and deuce==1:
        print(nombre_jugador + " ganó el juego")
        break
    elif puntos_maquina > 3 and deuce==1:
        print(nom_jugador2 + " ganó el juego")
        break

    puntaje_juga1 = ""
    puntaje_maqui = ""

    if puntos_jugador1 == 0:
        puntaje_juga1 = "0"
    elif puntos_jugador1 == 1:
        puntaje_juga1 = "15"
    elif puntos_jugador1 == 2:
        puntaje_juga1 = "30"
    elif puntos_jugador1 == 3:
        puntaje_juga1 = "40"

    if puntos_maquina == 0:
        puntaje_maqui = "0"
    elif puntos_maquina == 1:
        puntaje_maqui = "15"
    elif puntos_maquina == 2:
        puntaje_maqui = "30"
    elif puntos_maquina == 3:
        puntaje_maqui = "40"

    print("Puntuación:")
    if go == 0:
        print(nombre_jugador + ": ", puntaje_juga1)
        print(nom_jugador2 + ": ", puntaje_maqui)
    elif go==1:
        print(nombre_jugador + ": ", puntaje_juga1_deuce)
        print(nom_jugador2 + ": ", puntaje_maqui_deuce)


    if deuce == 2:
        if go == 1:
            punto_para = random.choice([0,1])
            if punto_para == 0:
                puntaje_juga1_deuce += 1
            else:
                puntaje_maqui_deuce += 1
        else:   
            puntaje_juga1_deuce = 0
            puntaje_maqui_deuce = 0
            go=1