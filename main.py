from pantallas import Partida, Menu


menu = Menu()
valor = menu.bucle_pantalla() 

if valor == "partida":
    juego = Partida()
    juego.bucle_fotograma()