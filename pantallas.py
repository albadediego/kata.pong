import pygame as pg
from pongapp.figura_class import Pelota, Raqueta
from pongapp.utils import *

class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Pong")
        self.tasa_refresco = pg.time.Clock()

        self.pelota = Pelota(ANCHO//2, ALTO//2, COLOR_PELOTA)
        self.raqueta1 = Raqueta(10, ALTO//2)
        self.raqueta2 = Raqueta(ANCHO-10, ALTO//2)

    def bucle_fotograma(self):
        game_over = True
        while game_over:
            self.valor_tasa = self.tasa_refresco.tick(TS)
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    game_over = False

            self.pantalla_principal.fill(COLOR_PISTA)

            #pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2, 0), (ANCHO//2, ALTO), 10)
            for i in range(0,ALTO, ALTO//41):
                pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2, 0+i), (ANCHO//2, i+10), 10)

            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.pelota.mover(ANCHO,ALTO)
            self.pelota.comprobarChoque(self.raqueta1, self.raqueta2)

            self.pelota.mostrar_marcador(self.pantalla_principal)

            pg.display.flip()

        pg.QUIT()
