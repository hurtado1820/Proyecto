from jugador import *
from clases import *
from const import *
from enemigo1 import *
from jefe1 import *
import pygame
import random

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])

    #Grupos
    jugadores = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    rivales1 = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    misiles = pygame.sprite.Group()
    jefe = pygame.sprite.Group()

    #Creacion personajes
    j = Jugador([50,100])
    jugadores.add(j)
    r1 = Enemigo1([200,100])
    rivales1.add(r1)
    r2 = Enemigo2([750,570])
    rivales2.add(r2)

    #el jefe solo se crea, no tiene comportamiento
    jf = Jefe1([800,280])
    jefe.add(jf)

    #Creacion de plataformas
    p = Plataforma([120,250])
    plataformas.add(p)
    p2 = Plataforma([450,250])
    plataformas.add(p2)
    p3 = Plataforma([750,380])
    plataformas.add(p3)
    p4 = Plataforma([300,100])
    plataformas.add(p4)

    #gravedad
    j.plataformas = plataformas
    r1.plataformas = plataformas
    jf.plataformas = plataformas

    for r1 in rivales1:
        r1.mover()

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
            #Eliminacion de las balas al chocar con bordes y personajes (al impactarlos les baja vida)
            disp1 = pygame.sprite.spritecollide(b,rivales1,False)
            disp2 = pygame.sprite.spritecollide(b,rivales2,False)
            dispm = pygame.sprite.spritecollide(b,misiles,False)
            choq = pygame.sprite.spritecollide(b,plataformas,False)
            if choq:
                balas.remove(b)
            if b.rect.x < 0:
                balas.remove(b)
            if b.rect.x > ANCHO:
                balas.remove(b)
            for r1 in disp1:
                r1.vidas -= 1
                balas.remove(b)
            for r2 in disp2:
                rivales2.remove(r2)
                r2.vidas -= 1
                r2.damage = 0
                balas.remove(b)
            for m in dispm:
                misiles.remove(m)
                m.damage = 0
                balas.remove(b)

        #choque de los jugadores con los enemigos, si todavía están en juego le quitan vida al jugador
        col = pygame.sprite.spritecollide(r1,jugadores,False)
        col2 = pygame.sprite.spritecollide(r2,jugadores,False)
        if col:
            if r1.damage > 0:
                impacto = True
                j.velx *= -1
                j.vidas -= r1.damage
                print("vidas = ", j.vidas)
        if col2:
            if r2.damage > 0:
                impacto = True
                j.velx *= -1
                j.vidas -= r2.damage
                print("vidas = ", j.vidas)

        #control de muerte de los rivales
        for r1 in rivales1:
            r1.morir()
            if r1.estado == 3:
                rivales1.remove(r1)
                r1.damage = 0

        for r2 in rivales2:
            r2.morir()
            if r2.estado == 2:
                temp = -1
            if r2.temp < 0:
                m = Misil(r2.rect)
                m.velx = -5
                misiles.add(m)
                r2.temp = random.randrange(100)

        #eliminación de los misiles cuando tocan al jugador (le bajan vida) o llegan a los bordes
        for m in misiles:
            if m.rect.x < 0 or m.rect.x > ANCHO:
                misiles.remove(m)
                m.damage = 0
            en = pygame.sprite.spritecollide(m,jugadores,False)
            if en:
                j.vidas -= m.damage
                print("vidas = ",j.vidas)
                misiles.remove(m)
                m.damage = 0

        #muerte del jugador
        j.morir()
        if j.estado==4:
            jugadores.remove(j)
            fin = True


        jugadores.update()
        rivales1.update()
        rivales2.update()
        balas.update()
        misiles.update()
        jefe.update()
        ventana.fill(NEGRO)
        rivales1.draw(ventana)
        rivales2.draw(ventana)
        misiles.draw(ventana)
        balas.draw(ventana)
        jugadores.draw(ventana)
        plataformas.draw(ventana)
        jefe.draw(ventana)
        pygame.display.flip()
