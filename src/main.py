import curses
import time
from contador import iniciar_contador, actualizar_contador, toggle_pause
from tablero import inicializar_tablero, actualizar_tablero, dibujar_scoreboard

from classes.juego import Juego

# Variables globales para el estado del tablero
juego = Juego()

def main(stdscr):
    #objeto que guarda los valores del juego actual
    global juego

    tiempo_anterior = 0
    tiempo_restante = 0


    # Inicialización del tablero y las teclas
    stdscr.clear()

    inicializar_tablero(stdscr, 0, 0, 0, juego.cuarto, juego.local_puntos, juego.visita_puntos, juego.local_faltas, juego.visita_faltas)

    # Desactivar el cursor
    curses.curs_set(0)
    
    while True:

        #actualizar tiempo restante
        tiempo_anterior, tiempo_restante, juego.pausado = actualizar_contador(tiempo_anterior, tiempo_restante, juego.pausado)
        
        # Obtener los minutos y segundos actuales
        juego.actualizar_tiempo(tiempo_restante)
        
        # Actualizar el tablero con los valores actuales
        dibujar_scoreboard(stdscr, juego.minutos, juego.segundos, juego.milisegundos, juego.cuarto, juego.local_puntos, juego.visita_puntos, juego.local_faltas, juego.visita_faltas, juego.pausado)
        
        # Esperar por una tecla durante 100ms
        stdscr.timeout(100)
        key = stdscr.getch()
        
        # Manejar las teclas presionadas
        if key == ord('t'):  # Pausar/Reanudar con la tecla 't'
            juego.toggle_pause()
        elif key == ord('s'):  # Sumar puntos al equipo local con la tecla 's'
            juego.sumar_puntos_local()
        elif key == ord('d'):  # Sumar puntos al equipo visitante con la tecla 'd'
            juego.sumar_puntos_visita()
        elif key == ord('x'):  # Resta puntos al equipo local con la tecla 'x'
            juego.restar_puntos_local()
        elif key == ord('c'):  # Resta puntos al equipo visita con la tecla 'c'
            juego.restar_puntos_visita()
        elif key == ord('g'):  # Suma 1 al cuarto con la tecla 'g'
            juego.incrementar_cuarto()
        elif key == ord('w'):  # Suma 1 al faltas local con la tecla 'w'
            juego.incrementar_faltas_local()
        elif key == ord('e'):  # Suma 1 al faltas visita con la tecla 'e'
            juego.incrementar_faltas_visita()
        elif key == ord('m'):  # Sumar minutos con la tecla 'm'
            tiempo_restante += 60 * 1000
            #iniciar contador con nuevo tiempo
            tiempo_anterior, juego.pausado = iniciar_contador(juego.pausado)

if __name__ == "__main__":
    curses.wrapper(main)
