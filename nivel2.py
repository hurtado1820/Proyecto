from jugador import *
from clases import *
from const import *
from enemigo3 import *
from enemigo4 import *
from modificadores import *
import pygame
import random

def Nivel2(ventana):
    #Grupos
    jugadores = pygame.sprite.Group()
    rivales3 = pygame.sprite.Group()
    rivales4 = pygame.sprite.Group()
    jefe2 = pygame.sprite.Group()
    ondas = pygame.sprite.Group()
    piedras = pygame.sprite.Group()
    gen = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    boost = pygame.sprite.Group()
    health = pygame.sprite.Group()

    #Creacion personajes
    j = Jugador([50,100])
    jugadores.add(j)
    r3 = Enemigo3([320,30])
    rivales3.add(r3)
    r4 = Enemigo4([410,190])
    rivales4.add(r4)
    jf2 = Jefe2([120,380])
    jefe2.add(jf2)

    #generadores
    g=Generador([900,100])
    gen.add(g)

    #modificadores
    v = Boost([200,460])
    boost.add(v)
    s = Salud([560,345])
    health.add(s)

    #Creacion plataformas
    p2 = Plataforma([400,250])
    plataformas.add(p2)
    p3 = Plataforma([100,450])
    plataformas.add(p3)
    p4 = Plataforma([300,100])
    plataformas.add(p4)

    j.plataformas = plataformas
    r3.plataformas = plataformas

    for r3 in rivales3:
        r3.mover()

    fin=False
    reloj = pygame.time.Clock()
    while not fin:
        #movimiento del jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if j.estado == 1:
                        j.velx = 5
                        j.dir = 1
                    if j.estado == 2:
                        j.velx = 7
                        j.dir = 1
                    if j.estado == 4:
                        j.velx = 2
                        j.dir=1
                if event.key  == pygame.K_LEFT:
                    if j.estado == 1:
                        j.velx = -5
                        j.dir = 2
                    if j.estado == 2:
                        j.velx = -7
                        j.dir = 2
                    if j.estado == 4:
                        j.velx = -2
                        j.dir= 2
                if event.key == pygame.K_SPACE:
                    if j.estado == 1:
                        j.vely = -15
                    if j.estado == 2:
                        j.vely = -18
                    if j.estado == 4:
                        j.vely = -10
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

        for jf2 in jefe2:
            jf2.morir()
            if jf2.estado == 2:
                jefe2.remove(jf2)
                jf2.damage = 0
                g.estado = 2
            if jf2.temp < 0:
                direccion = random.randrange(250)
                o = Onda(jf2.rect)
                if direccion < 125:
                    o.velx = 5
                elif direccion < 250:
                    o.velx = -5
                ondas.add(o)
                jf2.temp = random.randrange(100)

        for g in gen:
            if g.estado == 1:
                if g.temp < 0:
                    pi = Piedra(g.rect)
                    pi.vely = 5
                    piedras.add(pi)
                    g.temp = random.randrange(100)

        for b in balas:
            dispj2 = pygame.sprite.spritecollide(b,jefe2,False)
            choq = pygame.sprite.spritecollide(b,plataformas,False)
            disp3 = pygame.sprite.spritecollide(b,rivales3,False)
            disp4 = pygame.sprite.spritecollide(b,rivales4,False)
            dispo = pygame.sprite.spritecollide(b,ondas,False)
            dispd = pygame.sprite.spritecollide(b,piedras,False)
            if choq:
                balas.remove(b)
            if b.rect.x < 0:
                balas.remove(b)
            if b.rect.x > ANCHO:
                balas.remove(b)
            for r3 in disp3:
                if r3.estado == 1:
                    balas.remove(b)
            for r4 in disp4:
                if r4.estado == 1:
                    r4.estado = 2
                    r4.vidas -= 1
                    balas.remove(b)
            for jf2 in dispj2:
                if jf2.estado == 1:
                    jf2.vidas -= 1
                    balas.remove(b)
            for o in ondas:
                ondas.remove(o)
                o.damage = 0
                balas.remove(b)
            for pi in piedras:
                piedras.remove(pi)
                pi.damage = 0
                balas.remove(b)

        colj2 = pygame.sprite.spritecollide(jf2,jugadores,False)
        col3 = pygame.sprite.spritecollide(r3,jugadores,False)
        col4 = pygame.sprite.spritecollide(r4,jugadores,False)
        if colj2:
            if jf2.damage > 0:
                impacto = True
                j.velx *= -1
                j.vely = -2
                j.vidas -= jf2.damage
                print("vidas = ", j.vidas)
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

            #recoger modificadores
        speed = pygame.sprite.spritecollide(v,jugadores,False)
        sal = pygame.sprite.spritecollide(s,jugadores,False)

        if speed:
            boost.remove(v)
            j.inventario[2] += 1
            j.mayo_rakuin()

        if sal:
            health.remove(s)
            j.vidas += s.poder
            s.poder = 0
            j.velx *= -1
            print("vidas = ", j.vidas)

        for pi in piedras:
            if pi.rect.bottom > ALTO:
                piedras.remove(pi)
                pi.damage = 0
            pied = pygame.sprite.spritecollide(pi,jugadores,False)
            plat = pygame.sprite.spritecollide(pi,plataformas,False)
            if plat:
                piedras.remove(pi)
                pi.damage = 0
            if pied:
                j.vidas -= pi.damage
                #print("vidas = ",j.vidas)
                piedras.remove(pi)
                pi.damage = 0

        for o in ondas:
            if o.rect.x < 0 or o.rect.x > ANCHO:
                ondas.remove(o)
                o.damage = 0
            on = pygame.sprite.spritecollide(o,jugadores,False)
            if on:
                if o.damage > 0:
                    impacto = True
                    j.velx *= -1
                    j.aturdido = 1
                    ondas.remove(o)
                    o.damage = 0
            j.aturdir()

        for r3 in rivales3:
            r3.morir()
            if r3.estado == 2:
                rivales3.remove(r3)

        for r4 in rivales4:
            r4.morir()
            if r4.estado == 3:
                rivales4.remove(r4)
                r4.damage = 0

        j.morir()
        if j.estado==5:
            jugadores.remove(j)
            fin = True

        jugadores.update()
        balas.update()
        ondas.update()
        piedras.update()
        rivales3.update()
        rivales4.update()
        jefe2.update()
        gen.update()
        plataformas.update()
        ventana.fill(NEGRO)
        rivales3.draw(ventana)
        rivales4.draw(ventana)
        ondas.draw(ventana)
        piedras.draw(ventana)
        gen.draw(ventana)
        balas.draw(ventana)
        boost.draw(ventana)
        health.draw(ventana)
        jugadores.draw(ventana)
        jefe2.draw(ventana)
        plataformas.draw(ventana)
        pygame.display.flip()
        reloj.tick(20)
