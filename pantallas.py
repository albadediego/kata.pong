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
        self.fuente = pg.font.Font(None, 30)
        self.fuente_tiempo = pg.font.Font(None, 45)
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
        self.quienMarco = ""
        self.temporizador = TIEMPO_JUEGO
        self.game_over = True

    def bucle_fotograma(self):
        while self.game_over:
            self.valor_tasa = self.tasa_refresco.tick(TS)
           
            for eventos in pg.event.get():
                if eventos.type == pg.QUIT:
                    self.game_over = False
                    
            self.finalizacion_juego()

            #self.pantalla_principal.fill(COLOR_PISTA)
            if self.temporizador <= 5000:
                self.pantalla_principal.fill(PISTA_ROJA)
            elif self.temporizador <= 10000:
                self.pantalla_principal.fill(PISTA_NARANJA)
            else:
                self.pantalla_principal.fill(COLOR_PISTA)
            self.mostar_linea_central()

            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.quienMarco = self.pelota.mover(ANCHO,ALTO)

            self.pelota.comprobarChoque(self.raqueta1, self.raqueta2)
            self.mostrar_marcador()


            pg.display.flip()

        pg.quit()

    def mostar_linea_central(self):
            #pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2, 0), (ANCHO//2, ALTO), 10)
            for i in range(0,ALTO, ALTO//41):
                pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2, 0+i), (ANCHO//2, i+10), 10)

    def mostrar_marcador(self):
        if self.quienMarco == "Derecha":
            self.contadorDerecho +=1
        elif self.quienMarco == "Izquierda":
            self.contadorIzquierdo +=1

        jugador1 = self.fuente.render("Jugador 1", True, COLOR_AZUL)
        jugador2 = self.fuente.render("Jugador 2", True, COLOR_AZUL)
        marcador1 = self.fuente.render(str(self.contadorDerecho), True, COLOR_BLANCO)
        marcador2 = self.fuente.render(str(self.contadorIzquierdo), True, COLOR_BLANCO)
        tiempo_juego = self.fuente_tiempo.render(str(int(self.temporizador/1000)), True, COLOR_ROJO)

        self.pantalla_principal.blit(marcador1, ((ANCHO//2)-100, 50))
        self.pantalla_principal.blit(marcador2, ((ANCHO//2)+50, 50))
        self.pantalla_principal.blit(jugador1, ((ANCHO//2)-150, 20))
        self.pantalla_principal.blit(jugador2, ((ANCHO//2)+20, 20))
        self.pantalla_principal.blit(tiempo_juego, ((ANCHO//2), 20))

    def finalizacion_juego(self):
        #Finalizacion del juego por puntos
        if self.contadorDerecho == 7:
            print("El ganador es el Jugador 1")
            self.game_over = False
        if self.contadorIzquierdo == 7:
            print("El ganador es el Jugador 2")
            self.game_over = False

        #Finalizacion del juego por tiempo
        self.temporizador = self.temporizador - self.valor_tasa
        if self.temporizador <= 0:
            print("Fin del juego")
            self.game_over = False
            

class Menu:
    pg.init()
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Menu")
        self.tasa_refresco = pg.time.Clock()


    def bucle_pantalla(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

class Resultado:
    def __init__(self, resultado):
        pg.init()
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Resultado")
        self.tasa_refresco = pg.time.Clock()
        self.fuenteResultado = pg.font.Font(FUENTE1, 20)
        self.resultado = resultado

    def bucle_pantalla(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True 

            self.pantalla_principal.fill(COLOR_BLANCO)
            texto_resultado = self.fuenteResultado.render(str(self.resultado), True, COLOR_ROJO)
            self.pantalla_principal.blit(texto_resultado,(200, ALTO//2))           
            pg.display.flip()

        pg.quit() 