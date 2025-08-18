import pygame as pg
from figura_class import Pelota, Raqueta

pg.init()

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("Pong")

#definir tasa de refresco en nuestro bucle de fotogramas, fps=fotograma por segundo
tasa_refresco = pg.time.Clock()

#agregar marcadores
#asignacion de fuente y tamaño de letra
marcador1_font = pg.font.SysFont("verdana", 30)
marcador2_font = pg.font.SysFont("verdana", 30)

#Creamos un objeto de la clase Pelota o instanciamos la clase Pelota
pelota = Pelota(400,300,(107, 7, 157), 15)

#Raqueta izquierda
raqueta1 = Raqueta(10,300)

#Raqueta derecha
raqueta2 = Raqueta(790, 300)

game_over = True

while game_over:
    #obtener la tasa de refresco en milisegundos
    valor_tasa = tasa_refresco.tick(360) #variable para controlar la velocidad entre fotogramas
    #print(valor_tasa)
    for eventos in pg.event.get():
        #print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla_principal.fill( (7, 157, 107) )

    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), 10)
    
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    raqueta1.mover(pg.K_w, pg.K_s)
    raqueta2.mover(pg.K_UP, pg.K_DOWN)
    pelota.mover(800,600)

    print("Jugador derecho: ", pelota.contadorIzquierdo)
    print("Jugador izquierdo: ", pelota.contadorDerecho)

    #asignacion de color y texto
    marcador1 = marcador1_font.render(str(pelota.contadorDerecho), True, (255,255,255))
    marcador2 = marcador2_font.render(str(pelota.contadorIzquierdo), True, (255,255,255))

    pantalla_principal.blit(marcador1, (350, 50))
    pantalla_principal.blit(marcador2, (450, 50))

    pg.display.flip()
