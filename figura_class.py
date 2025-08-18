import pygame as pg

class Raqueta:
    def __init__(self, posX, posY, color=(255,255,255), w=20, h=120):
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
        if estado_teclado[teclado_abajo] == True and self.posY <= 600-(self.h//2):
            self.posY += 1

class Pelota:
    def __init__(self, posX, posY, color=(255,255,255), radio=5, vx=1, vy=1):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0

    def dibujar(self, surface):
        pg.draw.circle(surface, self.color,(self.posX, self.posY), self.radio)

    def mover(self, xMax, yMax):
        self.posX += self.vx
        self.posY += self.vy

        if self.posX >= xMax+(5*self.radio) or self.posX <= 0-(5*self.radio):
            if self.posX >= xMax+(5*self.radio):
                self.contadorDerecho += 1
            elif self.posX <= 0-(5*self.radio):
                 self.contadorIzquierdo += 1

            self.posX = 400
            self.posY = 300
            self.vx *= -1

        if self.posY >= yMax-(self.radio) or self.posY <= 0+(self.radio):
            self.vy *= -1