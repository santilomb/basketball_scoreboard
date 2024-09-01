import curses
import time
import threading
from flask import Flask, render_template_string
from contador import iniciar_contador, actualizar_contador, toggle_pause
from tablero import inicializar_tablero, actualizar_tablero, dibujar_scoreboard

# Crear la aplicación Flask
app = Flask(__name__)

# Variables globales para el estado del tablero
estado_tablero = {
    'minutos': 0,
    'segundos': 0,
    'milisegundos': 0,
    'cuarto': 0,
    'local_puntos': 0,
    'visita_puntos': 0,
    'local_faltas': 0,
    'visita_faltas': 0,
    'pausado': True,
}

# Template HTML básico para mostrar el tablero
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Tablero de Puntuación</title>
    <style>
        body { font-family: monospace; background-color: black; color: white; }
        pre { font-size: 20px; }
    </style>
</head>
<body>
    <pre>
Cuarto: {{ cuarto }}   |   Local: {{ local_puntos }}  Visitante: {{ visita_puntos }}
Faltas Local: {{ local_faltas }}   |   Faltas Visitante: {{ visita_faltas }}
Tiempo Restante: {{ minutos }}:{{ '%02d' % segundos }}:{{ milisegundos }}
Pausado: {{ pausado }}
    </pre>
</body>
</html>
"""

# Flask route para mostrar el tablero
@app.route("/")
def mostrar_tablero():
    return render_template_string(html_template, **estado_tablero)

# Función principal de ncurses
def main(stdscr):
    global estado_tablero  # Usamos la variable global para compartir el estado del tablero

    # Configuración inicial
    tiempo_anterior = 0
    tiempo_restante = 0

    # Inicialización del tablero
    stdscr.clear()
    inicializar_tablero(stdscr, 0, 0, 0, estado_tablero['cuarto'], estado_tablero['local_puntos'],
                        estado_tablero['visita_puntos'], estado_tablero['local_faltas'], estado_tablero['visita_faltas'])

    curses.curs_set(0)  # Desactivar el cursor
    
    while True:
        # Actualizar tiempo restante
        tiempo_anterior, tiempo_restante, estado_tablero['pausado'] = actualizar_contador(tiempo_anterior, tiempo_restante, estado_tablero['pausado'])
        
        if tiempo_restante > 0:
            estado_tablero['minutos'] = tiempo_restante // 60000
            estado_tablero['segundos'] = (tiempo_restante % 60000) // 1000
            estado_tablero['milisegundos'] = (tiempo_restante % 1000) // 100
        
        # Actualizar el tablero con los valores actuales
        dibujar_scoreboard(stdscr, estado_tablero['minutos'], estado_tablero['segundos'], estado_tablero['milisegundos'],
                           estado_tablero['cuarto'], estado_tablero['local_puntos'], estado_tablero['visita_puntos'],
                           estado_tablero['local_faltas'], estado_tablero['visita_faltas'], estado_tablero['pausado'])

        stdscr.timeout(100)
        key = stdscr.getch()

        # Manejar las teclas presionadas
        if key == ord('t'):
            estado_tablero['pausado'] = toggle_pause(estado_tablero['pausado'])
        elif key == ord('s'):
            estado_tablero['local_puntos'] += 1
        elif key == ord('d'):
            estado_tablero['visita_puntos'] += 1
        elif key == ord('x') and estado_tablero['local_puntos'] > 0:
            estado_tablero['local_puntos'] -= 1
        elif key == ord('c') and estado_tablero['visita_puntos'] > 0:
            estado_tablero['visita_puntos'] -= 1
        elif key == ord('g'):
            estado_tablero['cuarto'] += 1
            if estado_tablero['cuarto'] >= 10:
                estado_tablero['cuarto'] = 0
        elif key == ord('w'):
            estado_tablero['local_faltas'] += 1
            if estado_tablero['local_faltas'] >= 10:
                estado_tablero['local_faltas'] = 0
        elif key == ord('e'):
            estado_tablero['visita_faltas'] += 1
            if estado_tablero['visita_faltas'] >= 10:
                estado_tablero['visita_faltas'] = 0
        elif key == ord('m'):
            tiempo_restante += 60 * 1000
            tiempo_anterior, estado_tablero['pausado'] = iniciar_contador(estado_tablero['pausado'])

def ncurses_thread():
    curses.wrapper(main)

def iniciar_servidor_web():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    # Iniciar ncurses en un hilo separado
    ncurses_hilo = threading.Thread(target=ncurses_thread)
    ncurses_hilo.start()

    # Iniciar el servidor web
    iniciar_servidor_web()
