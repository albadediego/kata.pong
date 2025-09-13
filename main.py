from pongapp.controlador_pantallas import *

juego = PantallaControlador()
juego.start()

'''
from pantallas import *

menu = Menu()
valor = menu.bucle_pantalla() 

if valor == "partida":
    juego = Partida()
    juego.bucle_fotograma()
    resultado_partida = juego.finalizacion_juego()
    if resultado_partida:
        resultado = Resultado(resultado_partida)
        resultado.bucle_pantalla()
elif valor == "record":
    record = Record()
    record.bucle_pantalla()
'''