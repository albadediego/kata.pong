import pygame as pg
from figura_class import Pelota, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("Pong")

#Creamos un objeto de la clase Pelota o instanciamos la clase Pelota
pelota = Pelota(400,300,(107, 7, 157), 15)

#Raqueta izquierda
raqueta1 = Raqueta(10,300)

#Raqueta derecha
raqueta2 = Raqueta(790, 300)

game_over = True

while game_over:
    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla_principal.fill( (7, 157, 107) )

    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), 10)
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()
