import curses
import time
from contador import iniciar_contador, actualizar_contador, toggle_pause
from tablero import inicializar_tablero, actualizar_tablero, dibujar_scoreboard

def main(stdscr):
    # Configuración inicial
    minutos = 0  # Configura aquí la cantidad de minutos desde donde comenzará el contador
    segundos = 0
    milisegundos = 0
    pausado = True  # Estado inicial: no está pausado
    tiempo_anterior = 0
    tiempo_restante = 0


    # Inicialización del tablero y las teclas
    stdscr.clear()
    cuarto = 0
    local_puntos = 0
    visita_puntos = 0
    local_faltas = 0
    visita_faltas = 0
    inicializar_tablero(stdscr, 0, 0, 0, cuarto, local_puntos, visita_puntos, local_faltas, visita_faltas)

    # Desactivar el cursor
    curses.curs_set(0)
    
    while True:

        #actualizar tiempo restante
        tiempo_anterior, tiempo_restante, pausado = actualizar_contador(tiempo_anterior, tiempo_restante, pausado)
        
        # Obtener los minutos y segundos actuales
        if tiempo_restante > 0:
            minutos = tiempo_restante // 60000  # 1 minuto = 60000 milisegundos
            segundos = (tiempo_restante % 60000) // 1000  # 1 segundo = 1000 milisegundos
            milisegundos = (tiempo_restante % 1000) // 100  #  Tomar el primer dígito de los milisegundos
        
        # Actualizar el tablero con los valores actuales
        dibujar_scoreboard(stdscr, minutos, segundos, milisegundos, cuarto, local_puntos, visita_puntos, local_faltas, visita_faltas, pausado)
        
        # Esperar por una tecla durante 100ms
        stdscr.timeout(100)
        key = stdscr.getch()
        
        # Manejar las teclas presionadas
        if key == ord('t'):  # Pausar/Reanudar con la tecla 't'
            pausado = toggle_pause(pausado)
        elif key == ord('s'):  # Sumar puntos al equipo local con la tecla 's'
            local_puntos += 1
        elif key == ord('d'):  # Sumar puntos al equipo visitante con la tecla 'd'
            visita_puntos += 1
        elif key == ord('x'):  # Resta puntos al equipo local con la tecla 'x'
            if local_puntos > 0:
                local_puntos -= 1
        elif key == ord('c'):  # Resta puntos al equipo visita con la tecla 'c'
            if visita_puntos > 0:
                visita_puntos -= 1
        elif key == ord('g'):  # Suma 1 al cuarto con la tecla 'g'
            cuarto += 1
            if cuarto >= 10:
                cuarto = 0
        elif key == ord('w'):  # Suma 1 al faltas local con la tecla 'w'
            local_faltas += 1
            if local_faltas >= 10:
                local_faltas = 0
        elif key == ord('e'):  # Suma 1 al faltas visita con la tecla 'e'
            visita_faltas += 1
            if visita_faltas >= 10:
                visita_faltas = 0
        elif key == ord('m'):  # Sumar minutos con la tecla 'm'
            tiempo_restante += 60 * 1000
            #iniciar contador con nuevo tiempo
            tiempo_anterior, pausado = iniciar_contador(pausado)

if __name__ == "__main__":
    curses.wrapper(main)
