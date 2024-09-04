import curses

class Display:
    def __init__(self, stdscr):
        self.stdscr = stdscr

        # Mapeo de los números en formato de 7 segmentos
        self.DIGITOS_7_SEGMENTOS_GRANDES = {
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
        self.DIGITOS_7_SEGMENTOS_CHICOS = {
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
    def dibujar_digito_grande(self, digito, y, x, color):
        for i, linea in enumerate(self.DIGITOS_7_SEGMENTOS_GRANDES[digito]):
            self.stdscr.addstr(y + i, x, linea, curses.color_pair(color))

    def dibujar_digito_chico(self, digito, y, x, color):
        for i, linea in enumerate(self.DIGITOS_7_SEGMENTOS_CHICOS[digito]):
            self.stdscr.addstr(y + i, x, linea, curses.color_pair(color))


    def dibujar_marco(self):

        # Dimensiones del marco
        alto = 22
        ancho = 59

        # Dibujar el marco superior e inferior
        for x in range(ancho):
            self.stdscr.addstr(0, x, "-", curses.color_pair(1))    # Línea superior
            self.stdscr.addstr(alto - 1, x, "-", curses.color_pair(1))  # Línea inferior

        # Dibujar los laterales
        for y in range(1, alto - 1):
            self.stdscr.addstr(y, 0, "|", curses.color_pair(1))    # Lateral izquierdo
            self.stdscr.addstr(y, ancho - 1, "|", curses.color_pair(1))  # Lateral derecho

        # Esquinas
        self.stdscr.addstr(0, 0, "+", curses.color_pair(1))              # Esquina superior izquierda
        self.stdscr.addstr(0, ancho - 1, "+", curses.color_pair(1))      # Esquina superior derecha
        self.stdscr.addstr(alto - 1, 0, "+", curses.color_pair(1))       # Esquina inferior izquierda
        self.stdscr.addstr(alto - 1, ancho - 1, "+", curses.color_pair(1)) # Esquina inferior derecha


    # Función para dibujar el marcador
    def dibujar_scoreboard(self, minutos, segundos, milisegundos, cuarto, local_puntos, visita_puntos, local_faltas, visita_faltas):

        # Inicializar colores
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK) 
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK) 
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK) 

        self.stdscr.clear()
        
        self.dibujar_marco()

        # Título
        self.stdscr.addstr(1, 19, "TABLERO UNION VECINAL", curses.A_BOLD)

        # Dibujar minutos
        for idx, digito in enumerate(str(minutos).zfill(2)): 
            self.dibujar_digito_grande(digito, 3, 16 + idx * 6, 4)

        # signo dos puntos
        self.stdscr.addstr(4, 29, "*")
        self.stdscr.addstr(6, 29, "*")
        
        # Dibujar segundos
        for idx, digito in enumerate(str(segundos).zfill(2)): 
            self.dibujar_digito_grande(digito, 3, 32 + idx * 6, 4)

        # Dibujar milis
        for idx, digito in enumerate(str(milisegundos)): 
            self.dibujar_digito_chico(digito, 5, 45 + idx * 6, 4)

        # Nombres de los equipos
        self.stdscr.addstr(9, 8, "Local", curses.A_UNDERLINE)
        self.stdscr.addstr(9, 44, "Visitante", curses.A_UNDERLINE)
        
        # Dibujar el score del equipo local
        for idx, digito in enumerate(str(local_puntos).zfill(3)):  # zfill(3) asegura 3 dígitos
            self.dibujar_digito_grande(digito, 11, 2 + idx * 6, 2)
        
        # Dibujar el score del equipo visitante
        for idx, digito in enumerate(str(visita_puntos).zfill(3)):
            self.dibujar_digito_grande(digito, 11, 40 + idx * 6 , 2)

        # Nombres de los equipos
        self.stdscr.addstr(17, 2, "Faltas L", curses.A_UNDERLINE)
        self.stdscr.addstr(17, 26, "Cuartos", curses.A_UNDERLINE)
        self.stdscr.addstr(17, 49, "Faltas V", curses.A_UNDERLINE)

        # Dibujar local faltas
        for idx, digito in enumerate(str(local_faltas)): 
            self.dibujar_digito_chico(digito, 18, 4 + idx * 6, 3)

        # Dibujar cuartos
        for idx, digito in enumerate(str(cuarto)): 
            self.dibujar_digito_chico(digito, 18, 28 + idx * 6, 3)

        # Dibujar visita faltas
        for idx, digito in enumerate(str(visita_faltas)): 
            self.dibujar_digito_chico(digito, 18, 51 + idx * 6, 3)
