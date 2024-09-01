import curses

# Mapeo de los números en formato de 7 segmentos
DIGITOS_7_SEGMENTOS_GRANDES = {
    '0': [' ### ', '#   #', '#   #', '#   #', ' ### '],
    '1': ['  #  ', '  #  ', '  #  ', '  #  ', '  #  '],
    '2': [' ### ', '    #', ' ### ', '#    ', ' ### '],
    '3': [' ### ', '    #', ' ### ', '    #', ' ### '],
    '4': ['#   #', '#   #', ' ### ', '    #', '    #'],
    '5': [' ### ', '#    ', ' ### ', '    #', ' ### '],
    '6': [' ### ', '#    ', ' ### ', '#   #', ' ### '],
    '7': [' ### ', '    #', '    #', '    #', '    #'],
    '8': [' ### ', '#   #', ' ### ', '#   #', ' ### '],
    '9': [' ### ', '#   #', ' ### ', '    #', ' ### ']
}

# Mapeo de números en formato de 7 segmentos chicos
DIGITOS_7_SEGMENTOS_CHICOS = {
    '0': [' _ ', '| |', '|_|'],
    '1': ['   ', '  |', '  |'],
    '2': [' _ ', ' _|', '|_ '],
    '3': [' _ ', ' _|', ' _|'],
    '4': ['   ', '|_|', '  |'],
    '5': [' _ ', '|_ ', ' _|'],
    '6': [' _ ', '|_ ', '|_|'],
    '7': [' _ ', '  |', '  |'],
    '8': [' _ ', '|_|', '|_|'],
    '9': [' _ ', '|_|', ' _|']
}

# Función para dibujar un número usando caracteres de 7 segmentos
def dibujar_digito_grande(stdscr, digito, y, x, color):
    for i, linea in enumerate(DIGITOS_7_SEGMENTOS_GRANDES[digito]):
        stdscr.addstr(y + i, x, linea, curses.color_pair(color))

def dibujar_digito_chico(stdscr, digito, y, x, color):
    for i, linea in enumerate(DIGITOS_7_SEGMENTOS_CHICOS[digito]):
        stdscr.addstr(y + i, x, linea, curses.color_pair(color))


def dibujar_marco(stdscr):

    # Dimensiones del marco
    alto = 22
    ancho = 59

    # Dibujar el marco superior e inferior
    for x in range(ancho):
        stdscr.addstr(0, x, "-", curses.color_pair(1))    # Línea superior
        stdscr.addstr(alto - 1, x, "-", curses.color_pair(1))  # Línea inferior

    # Dibujar los laterales
    for y in range(1, alto - 1):
        stdscr.addstr(y, 0, "|", curses.color_pair(1))    # Lateral izquierdo
        stdscr.addstr(y, ancho - 1, "|", curses.color_pair(1))  # Lateral derecho

    # Esquinas
    stdscr.addstr(0, 0, "+", curses.color_pair(1))              # Esquina superior izquierda
    stdscr.addstr(0, ancho - 1, "+", curses.color_pair(1))      # Esquina superior derecha
    stdscr.addstr(alto - 1, 0, "+", curses.color_pair(1))       # Esquina inferior izquierda
    stdscr.addstr(alto - 1, ancho - 1, "+", curses.color_pair(1)) # Esquina inferior derecha



# Función para dibujar el marcador
def dibujar_scoreboard(stdscr, minutos, segundos, milisegundos, cuarto, local_puntos, visita_puntos, local_faltas, visita_faltas, pausado):

    # Inicializar colores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK) 
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK) 

    stdscr.clear()
    
    dibujar_marco(stdscr)

    # Título
    stdscr.addstr(1, 19, "TABLERO UNION VECINAL", curses.A_BOLD)

    # Dibujar minutos
    for idx, digito in enumerate(str(minutos).zfill(2)): 
        dibujar_digito_grande(stdscr, digito, 3, 16 + idx * 6, 4)

    # signo dos puntos
    stdscr.addstr(4, 29, "*")
    stdscr.addstr(6, 29, "*")
    
    # Dibujar segundos
    for idx, digito in enumerate(str(segundos).zfill(2)): 
        dibujar_digito_grande(stdscr, digito, 3, 32 + idx * 6, 4)

    # Dibujar milis
    for idx, digito in enumerate(str(milisegundos)): 
        dibujar_digito_chico(stdscr, digito, 5, 45 + idx * 6, 4)

    # Nombres de los equipos
    stdscr.addstr(9, 8, "Local", curses.A_UNDERLINE)
    stdscr.addstr(9, 44, "Visitante", curses.A_UNDERLINE)
    
    # Dibujar el score del equipo local
    for idx, digito in enumerate(str(local_puntos).zfill(3)):  # zfill(3) asegura 3 dígitos
        dibujar_digito_grande(stdscr, digito, 11, 2 + idx * 6, 2)
    
    # Dibujar el score del equipo visitante
    for idx, digito in enumerate(str(visita_puntos).zfill(3)):
        dibujar_digito_grande(stdscr, digito, 11, 40 + idx * 6 , 2)

    # Nombres de los equipos
    stdscr.addstr(17, 2, "Faltas L", curses.A_UNDERLINE)
    stdscr.addstr(17, 26, "Cuartos", curses.A_UNDERLINE)
    stdscr.addstr(17, 49, "Faltas V", curses.A_UNDERLINE)

    # Dibujar local faltas
    for idx, digito in enumerate(str(local_faltas)): 
        dibujar_digito_chico(stdscr, digito, 18, 4 + idx * 6, 3)

    # Dibujar cuartos
    for idx, digito in enumerate(str(cuarto)): 
        dibujar_digito_chico(stdscr, digito, 18, 28 + idx * 6, 3)

    # Dibujar visita faltas
    for idx, digito in enumerate(str(visita_faltas)): 
        dibujar_digito_chico(stdscr, digito, 18, 51 + idx * 6, 3)

    if pausado:
        pausado_texto = " (Pausado)"
    else:
        pausado_texto = "           "

    stdscr.refresh()

def inicializar_tablero(stdscr, minutos, segundos, milisegundos, cuarto, local_puntos, visita_puntos, local_faltas, visita_faltas):
    """
    Inicializa el tablero en la consola.
    """

    dibujar_marco(stdscr)

    stdscr.addstr(0, 0, f"PUNTOS LOCAL - {local_puntos} | {visita_puntos} - PUNTOS VISITA")
    stdscr.addstr(1, 0, f"FALTAS LOCAL - {local_faltas} | {visita_faltas} - FALTAS VISITA")
    stdscr.addstr(3, 0, f"TIEMPO: {minutos:02}:{segundos:02} {milisegundos:1}")
    stdscr.addstr(4, 0, f"CUARTO: {cuarto:1}")
    stdscr.refresh()

def actualizar_tablero(stdscr, minutos, segundos, milisegundos, cuarto, local_puntos, visita_puntos, local_faltas, visita_faltas, pausado):
    """
    Actualiza el tablero en la consola con el tiempo y puntajes actuales.
    """
    if pausado:
        pausado_texto = " (Pausado)"
    else:
        pausado_texto = "           "

    stdscr.addstr(0, 0, f"PUNTOS LOCAL - {local_puntos} | {visita_puntos} - PUNTOS VISITA")
    stdscr.addstr(1, 0, f"FALTAS LOCAL - {local_faltas} | {visita_faltas} - FALTAS VISITA")
    stdscr.addstr(3, 0, f"TIEMPO: {minutos:02}:{segundos:02} {milisegundos:1} {pausado_texto}")
    stdscr.addstr(4, 0, f"CUARTO: {cuarto:1}")
    stdscr.refresh()
