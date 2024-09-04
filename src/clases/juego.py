class Juego:
    def __init__(self):
        self.cuarto = 1
        self.local_puntos = 0
        self.visita_puntos = 0
        self.local_faltas = 0
        self.visita_faltas = 0

    def reset(self):
        self.cuarto = 1
        self.local_puntos = 0
        self.visita_puntos = 0
        self.local_faltas = 0
        self.visita_faltas = 0

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
        if self.local_faltas >= 6:
            self.local_faltas = 0

    def incrementar_faltas_visita(self):
        self.visita_faltas += 1
        if self.visita_faltas >= 6:
            self.visita_faltas = 0

