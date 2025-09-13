import pygame as pg
from pongapp.utils import *

class Raqueta:
    def __init__(self, posX, posY, color=COLOR_BLANCO, w=20, h=120):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.w = w
        self.h = h

    def dibujar(self, surface):
        pg.draw.rect(surface, self.color,(self.posX-(self.w//2), self.posY-(self.h//2), self.w, self.h))

    def mover(self, teclado_arriba, teclado_abajo):
        estado_teclado = pg.key.get_pressed()
        if estado_teclado[teclado_arriba] == True and self.posY >= 0+(self.h//2):
            self.posY -= 1
        if estado_teclado[teclado_abajo] == True and self.posY <= ALTO-(self.h//2):
            self.posY += 1

    @property
    def derecha(self):
        return self.posX+(self.w//2) 
    @property
    def izquierda(self):
        return self.posX-(self.w//2)    
    @property
    def arriba(self):
        return self.posY-(self.h//2) 
    @property
    def abajo(self):
        return self.posY+(self.h//2)

class Pelota:
    def __init__(self, posX, posY, color=COLOR_BLANCO, radio=15, vx=1, vy=1):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.sonido = pg.mixer.Sound(SONIDO_PELOTA)

    def dibujar(self, surface):
        pg.draw.circle(surface, self.color,(self.posX, self.posY), self.radio)

    def mover(self, xMax=ANCHO, yMax=ALTO):
        self.posX += self.vx
        self.posY += self.vy

        if self.posX >= xMax+(5*self.radio) or self.posX <= 0-(5*self.radio):
            if self.posX >= xMax+(5*self.radio):
                self.posX = ANCHO//2
                self.posY = ALTO//2
                self.vx *= -1
                return "Derecha"
            elif self.posX <= 0-(5*self.radio):
                self.posX = ANCHO//2
                self.posY = ALTO//2
                self.vx *= -1
                return "Izquierda"

        if self.posY >= yMax-(self.radio) or self.posY <= 0+(self.radio):
            self.vy *= -1

    def comprobarChoque(self, *raquetas):
        for r in raquetas:
            if self.derecha >= r.izquierda and\
                self.izquierda <= r.derecha and\
                self.abajo >= r.arriba and\
                self.arriba <= r.abajo:
                self.vx *= -1
                pg.mixer.Sound.play(self.sonido)
                pg.mixer.Sound.set_volume(self.sonido, 0.1)


    @property
    def derecha(self):
        return self.posX + self.radio
    @property
    def izquierda(self):
        return self.posX - self.radio
    @property
    def arriba(self):
        return self.posY - self.radio
    @property
    def abajo(self):
        return self.posY + self.radio
