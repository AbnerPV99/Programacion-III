import pygame
from pygame.locals import *
import sys

pygame.init()
ancho = 300
altura = 300
celda_tamanio = ancho // 3
blanco = (255,255,255)
negro = (0,0,0)
fps = 30

pantalla = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption("Totito")
fuente = pygame.font.Font(None, 36)

jugador = 'X'
tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def dibujar_tablero():
    for fila in tablero:
        print('|'.join(fila))
        print('-'*5)

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

def movimiento_jugador():
    while True:
        try:
            fila = int(input("Turno del jugador\nIngrese la coordenada de la fila (0-2): "))
            col = int(input("Ingrese la coordenada de la columna (0-2): "))

            if (0 <= fila <= 2 and 0 <= col <= 2 and tablero[fila][col] == ' '):
                tablero[fila][col] = jugador
                break
            else:
                print("Movimiento no valido. Por favor, ingrese nuevamente una coordenada valida de fila y columna")
        except ValueError:
            print("Por favor, ingrese un valor entero para las filas y columnas")

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
    print("El valor de la mejor jugada es :", mejor_puntaje) 
    return mejor_jugada

def dibujar_X(x, y):
    pygame.draw.line(pantalla, negro, (x + 20, y +  20), (x + celda_tamanio - 20, y + celda_tamanio - 20), 2)
    pygame.draw.line(pantalla, negro, (x + celda_tamanio - 20, y + 20), (x + 20, y + celda_tamanio - 20), 2)

def dibujar_O(x,y):
    pygame.draw.circle(pantalla, negro, (x + celda_tamanio // 2, y + celda_tamanio // 2), celda_tamanio // 2 - 20, 2)

def juego(posicion_mouse):
    fila = posicion_mouse[1] // celda_tamanio
    col = posicion_mouse[0] // celda_tamanio
    return int(fila), int(col)

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

def main():
    global tablero, jugador, pantalla

    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == MOUSEBUTTONDOWN:
                if jugador == 'X':
                    fila, col = juego(pygame.mouse.get_pos())
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
            pygame.quit()
            sys.exit()

        pantalla.fill(blanco)
        dibujar_tablero(tablero)

        pygame.display.flip()
        reloj.tick(fps)

        if jugador == 'O':
            filaM, colM = movimiento_maquina()
            if tablero[filaM][colM] == ' ':
                tablero[filaM][colM] = 'O'
                jugador = 'X'

if __name__ == '__main__':
    main()