class Juego:
    def __init__(self):
        self.minutos = 0
        self.segundos = 0
        self.milisegundos = 0
        self.cuarto = 0
        self.local_puntos = 0
        self.visita_puntos = 0
        self.local_faltas = 0
        self.visita_faltas = 0
        self.pausado = True
    
    def actualizar_tiempo(self, tiempo_restante):
        """ Actualiza el tiempo restante en minutos, segundos y milisegundos """
        if tiempo_restante > 0:
            self.minutos = tiempo_restante // 60000
            self.segundos = (tiempo_restante % 60000) // 1000
            self.milisegundos = (tiempo_restante % 1000) // 100

    def toggle_pause(self):
        """ Alterna el estado de pausa """
        self.pausado = not self.pausado
        return self.pausado

    def sumar_puntos_local(self):
        self.local_puntos += 1

    def sumar_puntos_visita(self):
        self.visita_puntos += 1

    def restar_puntos_local(self):
        if self.local_puntos > 0:
            self.local_puntos -= 1

    def restar_puntos_visita(self):
        if self.visita_puntos > 0:
            self.visita_puntos -= 1

    def incrementar_cuarto(self):
        self.cuarto += 1
        if self.cuarto >= 10:
            self.cuarto = 0

    def incrementar_faltas_local(self):
        self.local_faltas += 1
        if self.local_faltas >= 10:
            self.local_faltas = 0

    def incrementar_faltas_visita(self):
        self.visita_faltas += 1
        if self.visita_faltas >= 10:
            self.visita_faltas = 0

