import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("Pong")

game_over = True

while game_over:
    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla_principal.fill( (7, 157, 107) )

    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), 10)

    pg.display.flip()
