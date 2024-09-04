import curses
from clases.juego import Juego
from clases.timer import Timer
from clases.display_curses import Display
#from controles import Controles


def main(stdscr):
    juego = Juego()
    timer = Timer()
    display = Display(stdscr)
    #controles = Controles(stdscr, juego)

    curses.curs_set(0) # Desactivar el cursor
    stdscr.nodelay(True)  # No bloquea la entrada del teclado

    while True:
        # Esperar por una tecla durante 100ms
        stdscr.timeout(100)
        key = stdscr.getch()
        
        # Manejar las teclas presionadas
        if key == ord('t'):  # Pausar/Reanudar con la tecla 't'
            timer.cambiar_estado()
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
            timer.sumar_minutos(1)
        elif key == ord('q'): #salir
            exit()

        minutos, segundos, milisegundos = timer.mostrar_restante()

        display.dibujar_scoreboard(minutos, segundos, milisegundos, juego.cuarto, juego.local_puntos, juego.visita_puntos, juego.local_faltas, juego.visita_faltas)

        stdscr.refresh()
        timer.actualizar()

curses.wrapper(main)
