import time

class Timer:
    def __init__(self):
        self.tiempo_anterior = 0
        self.tiempo_restante = 0
        self.tiempo_actual = int(time.time() * 1000) # todos los calculos seran en milisegundos
        self.estado = "detenido"

    def iniciar(self):
        if self.estado == "detenido":
            self.estado = "corriendo"
            self.tiempo_anterior = int(time.time() * 1000)

    def detener(self):
        if self.estado == "corriendo":
            self.estado = "detenido"

    def cambiar_estado(self):
        if self.estado == "detenido":
            self.iniciar()
        else:
            self.detener()

    def sumar_minutos(self, min = 1):
        self.tiempo_restante += (min * 60) * 1000

    def actualizar(self):
        self.tiempo_actual = int(time.time() * 1000)
        if self.estado == "corriendo":
            self.tiempo_restante = self.tiempo_restante - (self.tiempo_actual - self.tiempo_anterior)
        self.tiempo_anterior = self.tiempo_actual
        if self.tiempo_restante <= 0:
            self.tiempo_restante = 0

    def mostrar_restante(self):
        minutos = 0
        segundos = 0
        milisegundos = 0
        if self.tiempo_restante > 0:
            minutos = self.tiempo_restante // 60000
            segundos = (self.tiempo_restante % 60000) // 1000
            milisegundos = (self.tiempo_restante % 1000) // 100
        return minutos, segundos, milisegundos
