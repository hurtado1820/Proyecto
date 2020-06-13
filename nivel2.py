from jugador import *
from clases import *
from const import *
from enemigo3 import *
from enemigo4 import *
from jefe2 import *
import pygame
import random

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])

    #grupos
    jugadores = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    rivales3 = pygame.sprite.Group()
    rivales4 = pygame.sprite.Group()
    jefe2 = pygame.sprite.Group()
    #explosiones = pygame.sprite.Group()

    #creación de personajes
    j = Jugador([50,100])
    jugadores.add(j)
    r3 = Enemigo3([320,30])
    rivales3.add(r3)
    r4 = Enemigo4([410,190])
    rivales4.add(r4)

    #solo se crea el jefe, no se implementa
    jf2 = Jefe2([800,280])
    jefe2.add(jf2)

    #plataformas
    p = Plataforma([120,250])
    plataformas.add(p)
    p2 = Plataforma([400,250])
    plataformas.add(p2)
    p3 = Plataforma([750,380])
    plataformas.add(p3)
    p4 = Plataforma([300,100])
    plataformas.add(p4)

    j.plataformas = plataformas
    r3.plataformas = plataformas
    jf2.plataformas = plataformas

    for r3 in rivales3:
        r3.mover()

    fin=False
    while not fin:
        #control del jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = 5
                    j.dir=1
                if event.key  == pygame.K_LEFT:
                    j.velx = -5
                    j.dir=2
                if event.key == pygame.K_SPACE:
                    j.vely = -15
                    j.piso = False
                if event.key == pygame.K_s:
                    #Estado de disparo y creacion de bala
                    pos = j.RetPos()
                    b = Bala(pos)
                    if j.dir == 1:
                        b.velx = 15
                        b.vely = 0
                        #j.accion = 3
                    if j.dir == 2:
                        b.velx = -15
                        b.vely = 0
                        #j.accion = 7
                    balas.add(b)
            if event.type == pygame.KEYUP:
                j.velx = 0

            for b in balas:
                #Eliminacion al salir de pantalla y chocar con rivales (les baja la vida). el enemigo 3 no puede ser herido -
                #debido a que se trata solo de un "objeto" que rueda tras el jugador
                disp4 = pygame.sprite.spritecollide(b,rivales4,False)
                choq = pygame.sprite.spritecollide(b,plataformas,False)
                if choq:
                    balas.remove(b)
                if b.rect.x < 0:
                    balas.remove(b)
                if b.rect.x > ANCHO:
                    balas.remove(b)
                for r4 in disp4:
                    if r4.estado == 1:
                        r4.estado = 2
                        r4.vidas -= 1
                        balas.remove(b)

            #control de colision del jugador con los enemigos, le baja vida al jugador
            col3 = pygame.sprite.spritecollide(r3,jugadores,False)
            col4 = pygame.sprite.spritecollide(r4,jugadores,False)

            if col3:
                if r3.estado == 1:
                    impacto = True
                    j.vidas = 0
                    print("vidas = ", j.vidas)
            if col4:
                if r4.estado == 1:
                    impacto = True
                    r4.estado = 3
                    j.velx *= -1
                    j.vidas -= r4.damage
                    print("vidas = ", j.vidas)
                    r4.vidas -= 1


            #control vida de los rivales, mueren al llegar a 0
            for r3 in rivales3:
                r3.morir()
                if r3.estado == 2:
                    rivales3.remove(r3)

            for r4 in rivales4:
                '''if r4.estado == 2:
                    e = Explosion(r4.rect)
                    explosiones.add(e)
                    ex = pygame.sprite.spritecollide(e,jugadores,False)
                    if ex:
                        j.vidas -= e.damage
                        j.velx *= -1
                        print("vidas = ",j.vidas)
                        explosiones.remove(e)
                        e.damage = 0'''
                r4.morir()
                if r4.estado == 3:
                    rivales4.remove(r4)
                    r4.damage = 0

            #muerte del jugador
            j.morir()
            if j.estado==4:
                jugadores.remove(j)
                fin = True

            jugadores.update()
            rivales3.update()
            rivales4.update()
            #explosiones.update()
            balas.update()
            jefe2.update()
            ventana.fill(NEGRO)
            rivales3.draw(ventana)
            rivales4.draw(ventana)
            balas.draw(ventana)
            #explosiones.draw(ventana)
            jugadores.draw(ventana)
            jefe2.draw(ventana)
            plataformas.draw(ventana)
            pygame.display.flip()
