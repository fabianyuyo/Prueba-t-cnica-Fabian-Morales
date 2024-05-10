#marcador de tenis! estructura basica.
#estructura de nombres.
def configurar_nombres():
    global jugador1,jugador2
    jugador1 = input("Nombre del jugador 1:")
    jugador2 = input("Nombre del jugador 2:")
    
def mostrar_nombres():
    print("Nombre de los jugadores")
    print("Nombre del jugador1",jugador1)
    print("Nombre del jugador2",jugador2)
    
def jugar_punto(jugador):
    global puntos_jugador1,puntos_jugador2
    
    if jugador == 1:
        puntos_jugador1 += 1
    else:
            puntos_jugador2 += 1
def verificar_ganador():
    global puntos_jugador1,puntos_jugador2
    if puntos_jugador1>= 4 and puntos_jugador1 > puntos_jugador2 + 1:
        print("¡El ganador es:",jugador1,"!")
        return True
    elif puntos_jugador2 >= 4 and puntos_jugador2 > puntos_jugador1 + 1:
        print("¡El ganador es:", jugador2, "!")
        return True
    elif puntos_jugador1 == 4 and puntos_jugador2 == 4:
        print("¡Empate!")
        return True
    return False
#Etapa de configuracion
jugador1 = ""
jugador2 = ""
print("¡Bienvenido al juego de Tenis!")

while True:
    print("Menu:")
    print("1. configurar nombres de jugadores")
    print("2. Empezar el juego")
    
    opcion = int(input("Seleccione una opcion:"))
    
    if opcion == 1:
        configurar_nombres()
        mostrar_nombres()
    elif opcion == 2:
        if jugador1 == "" or jugador2 == "":
            print("por favor, configure los nombres de los jugadores primero.")
        else:
                # Etapa de juego
                puntos_jugador1 = 0
                puntos_jugador2 = 0
                
                while True:
                    mostrar_nombres()
                    print("puntos:")
                    print("jugador 1:", puntos_jugador1)
                    print("jugador 2:", puntos_jugador2)
                    
                    
                    jugador_que_anota = int(input("¿Que jugador anota un punto? (1/2):"))
                    
                    jugar_punto(jugador_que_anota)
                    
                    if verificar_ganador():
                        break
                    else:
                        print("Opcion invalida.")
                        
                

    
    