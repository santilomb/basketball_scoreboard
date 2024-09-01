import time

def iniciar_contador(pausado):
    """
    Función para inicializar las variables del contador.
    """
    tiempo_anterior = int(time.time() * 1000)
    return tiempo_anterior, pausado

def actualizar_contador(tiempo_anterior, tiempo_restante, pausado):
    """
    Función para calcular el tiempo restante.
    """
    tiempo_actual = int(time.time() * 1000)
    if not pausado:
        tiempo_restante = tiempo_restante - (tiempo_actual - tiempo_anterior)
            
    tiempo_anterior = tiempo_actual

    if tiempo_restante <= 0:
        tiempo_restante = 0

    return tiempo_anterior, tiempo_restante, pausado


def toggle_pause(pausado):
    """
    Función para pausar y reanudar el contador.
    """
    return not pausado
