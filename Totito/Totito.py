import pygame, sys
from pygame.locals import *
import pygame_menu
import pygame_menu.events
import pygame_menu.themes

pygame.init() #Inicializa pygame
ancho = 300 #Ancho de ventana
altura = 300 #Altura de ventana
celda_tamanio = ancho // 3 #Calcula el espacio de casilla dividiendo en 3 el ancho de la pantalla
blanco = (255,255,255) #Color predefinido
negro = (0,0,0) #Color predefinido
fps = 30 #Limite de los fps

pantalla = pygame.display.set_mode((ancho, altura)) #Crea la ventana
pygame.display.set_caption("Menu") #Agrega un titulo a la ventana
fuente = pygame.font.Font(None, 36)

jugador = 'X'
tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def verificar_ganador():
    for i in range(3):
        #Verifica las columnas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        #Verifica las filas
        elif tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]
        #Verifica en diagonal
        elif tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
            return tablero[0][0]
        #Verifica en diagonal inversa
        elif tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
            return tablero[0][2]
    #Verifica si todo el tablero esta lleno y si hay empate    
    if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
        return 'Empate'
    #No hay ganador aun
    return None

#Este es un algoritmo recursivo que determina el mejor movimiento para la maquina evaluando todas las posibilidades de juego
def minimax(tablero, profundidad, maximizado):

    puntaje = {'X': -10, "O": 10, "Empate": 0}
    
    resultado = verificar_ganador()
    if resultado:
        return puntaje[resultado]
    
    if maximizado:
        mejor_puntaje = float("-inf")
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'O'
                    punteo = minimax(tablero, profundidad + 1, False)
                    tablero[i][j] = ' '
                    mejor_puntaje = max(punteo, mejor_puntaje)
        return mejor_puntaje
    
    else:
        mejor_puntaje = float("inf")
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'X'
                    punteo = minimax(tablero, profundidad + 1, True)
                    tablero[i][j] = ' '
                    mejor_puntaje = min(punteo, mejor_puntaje)
        return mejor_puntaje

def movimiento_maquina():
    mejor_puntaje = float("-inf")
    mejor_jugada = (-1,-1)

    for i in range(3):
        for j in range(3):
            if tablero[i][j] == ' ':
                tablero[i][j] = 'O'
                punteo = minimax(tablero, 0, False)
                tablero[i][j] = ' '

                if punteo > mejor_puntaje:
                    mejor_puntaje = punteo
                    mejor_jugada = (i, j)
    print("El valor de la mejor jugada es: ", mejor_puntaje) 
    print("La posicion de la mejor jugada es: ", mejor_jugada)
    return mejor_jugada

def dibujar_X(x, y):
    pygame.draw.line(pantalla, negro, (x + 20, y +  20), (x + celda_tamanio - 20, y + celda_tamanio - 20), 2) #Dibuja una linea recta inclinada hacia la derecha
    pygame.draw.line(pantalla, negro, (x + celda_tamanio - 20, y + 20), (x + 20, y + celda_tamanio - 20), 2) #Dibuja una linea recta inclinada hacia la izquierda

def dibujar_O(x,y):
    pygame.draw.circle(pantalla, negro, (x + celda_tamanio // 2, y + celda_tamanio // 2), celda_tamanio // 2 - 20, 2) #Dibuja el circulo

def juego(posicion_mouse):
    fila = posicion_mouse[1] // celda_tamanio
    col = posicion_mouse[0] // celda_tamanio
    return int(fila), int(col) #Guarda la posicion de la fila y columna de la tupla y lo retorna como entero

def dibujar_tablero(tablero):
    for i in range(1, 3):
        pygame.draw.line(pantalla, negro, (i * celda_tamanio, 0), (i * celda_tamanio, altura), 2)
        pygame.draw.line(pantalla, negro, (0, i * celda_tamanio), (ancho, i * celda_tamanio), 2)

    for fila in range(3):
        for col in range(3):
            jugador = tablero[fila][col]
            if jugador == 'X':
                dibujar_X(col * celda_tamanio, fila * celda_tamanio)
            elif jugador == 'O':
                dibujar_O(col * celda_tamanio, fila * celda_tamanio)

def historial():
    print("Aun no esta listo")

def integrantes():
    print("Aun no esta listo")

def partida():
    global tablero, jugador, pantalla
    
    reloj = pygame.time.Clock()
    #Bucle del juego
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit() #Cierra la ventana
                sys.exit() #Cierra el programa
            elif evento.type == MOUSEBUTTONDOWN: #Cuando el evento es presionar un boton del mouse
                if jugador == 'X':
                    fila, col = juego(pygame.mouse.get_pos()) #Obtiene la coordenada de la fila y columna del tablero
                    if tablero[fila][col] == ' ':
                        tablero[fila][col] = 'X'
                        jugador = 'O'

        ganador = verificar_ganador()
        if ganador:
            dibujar_tablero(tablero)
            if ganador == "Empate":
                print("Partida empatada")
            else:
                print(f"El jugador {ganador} ha ganado!")
            
            menu.mainloop(pantalla) #Regresa al menu principal
            tablero = [
                [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']
            ]
            #pygame.quit() #Cierra la ventana
            #sys.exit() #Cierra el programa

        pantalla.fill(blanco) #Rellena la pantalla de color blanco
        dibujar_tablero(tablero)

        pygame.display.flip() #Genera la ventana
        reloj.tick(fps) #Limita los fps a 30

        if jugador == 'O':
            filaM, colM = movimiento_maquina()
            if tablero[filaM][colM] == ' ':
                tablero[filaM][colM] = 'O'
                jugador = 'X' 

menu = pygame_menu.Menu("Menu Principal", 300,300, theme=pygame_menu.themes.THEME_BLUE) #Crea nuestra ventana del menu
menu.add.button("Jugar", partida) #Agrega un boton de Jugar que envia a la funcion de partida
menu.add.button("Ver Historial", historial) #Agrega un boton de Historial que envia a la funcion de Historial
menu.add.button("Integrantes", integrantes) #Agrega un boton de Integrantes que muestra la informacion del grupo
menu.add.button("Salir", pygame_menu.events.EXIT) #Sale del programa


if __name__ == '__main__':
    menu.mainloop(pantalla)
