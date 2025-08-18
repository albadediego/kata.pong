import pygame as pg

class Raqueta:
    def __init__(self, posX, posY, color=(255,255,255), w=5, h=50):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.w = w
        self.h = h

    def dibujar(self, surface):
        pg.draw.rect(surface, self.color,(self.posX, self.posY, self.w, self.h))

class Pelota:
    def __init__(self, posX, posY, color=(255,255,255), radio=5):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.radio = radio

    def dibujar(self, surface):
        pg.draw.circle(surface, self.color,(self.posX, self.posY), self.radio)