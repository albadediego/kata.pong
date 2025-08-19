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

    def comprobar_choque(self, r1, r2):
        #logica de choque
        #raqueta izquierda
        if self.derecha >= r1.izquierda and\
            self.izquierda <= r1.derecha and\
            self.abajo >= r1.arriba and\
            self.arriba <= r1.abajo:
            self.vx *= -1

        #raqueta derecha
        if self.derecha >= r2.izquierda and\
            self.izquierda <= r2.derecha and\
            self.abajo >= r2.arriba and\
            self.arriba <= r2.abajo:
            self.vx *= -1

    def comprobarChoque(self, *raquetas):
        for r in raquetas:
            if self.derecha >= r.izquierda and\
                self.izquierda <= r.derecha and\
                self.abajo >= r.arriba and\
                self.arriba <= r.abajo:
                self.vx *= -1

    def mostrar_marcador(self, pantalla):
        fuente = pg.font.Font(None, 30)
        jugador1 = fuente.render("Jugador 1", True, (255,255,255))
        jugador2 = fuente.render("Jugador 2", True, (255,255,255))
        marcador1 = fuente.render(str(self.contadorDerecho), True, (255,255,255))
        marcador2 = fuente.render(str(self.contadorIzquierdo), True, (255,255,255))

        pantalla.blit(marcador1, (300, 50))
        pantalla.blit(marcador2, (450, 50))
        pantalla.blit(jugador1, (250, 20))
        pantalla.blit(jugador2, (420, 20))

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
