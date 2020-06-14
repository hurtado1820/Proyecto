from jugador import *
from clases import *
from const import *
from enemigo1 import *
from jefe1 import *
from modificadores import *
import pygame
import random
import time
from cargarmapa1 import *
from spritesMapa import *

def Nivel1(ventana):
    pygame.font.init()

    fondo = pygame.image.load("fondoj.jpg")
    ventana.blit(fondo,[0,0])

    #Info mapa en x
    f_info = fondo.get_rect()
    f_velx = 0
    f_posx = 0
    lim_der = ANCHO - 100
    lim_izq = 100
    f_lim_izq = 0
    f_lim_der = ANCHO - f_info[2]

    #Info mapa en y
    f_vely = 0
    f_posy = 0
    lim_arri = 50
    lim_aba = ALTO - 50
    f_lim_arri = 0
    f_lim_aba = ALTO - f_info[3]

    #Grupos
    jugadores = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    rivales1 = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    misiles = pygame.sprite.Group()
    pistola = pygame.sprite.Group()
    tiempos = pygame.sprite.Group()
    jefe = pygame.sprite.Group()
    suelos = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    pinchos = pygame.sprite.Group()
    puentes = pygame.sprite.Group()

    CargaMapa1(suelos,plataformas,muros,pinchos,puentes)

    #Creacion personajes
    j = Jugador([0,90])
    jugadores.add(j)
    r1 = Enemigo1([30,30])
    rivales1.add(r1)
    r2 = Enemigo2([220,0])
    rivales2.add(r2)
    jf = Jefe1([815,280])
    jefe.add(jf)

    #modificadores
    gun = Pistola([250,460])
    pistola.add(gun)
    t = Tiempo([400,20])
    tiempos.add(t)

    #gravedad
    j.plataformas = plataformas
    j.suelos = suelos
    j.muros = muros
    jf.plataformas = plataformas

    #Texto control vida jugador
    info = pygame.font.Font(None,30)
    vidas = "Vidas: " + str(j.vidas)
    info_vidas = info.render(vidas,True,BLANCO)

    #Timer del juego
    cont = 0
    tiempo = 0
    info_t = pygame.font.Font(None,30)
    restante = "Tiempo: " + str(tiempo) + "sg"
    info_restante = info_t.render(restante,True,BLANCO)
    p = 250.00
    alarm = time.time() + p

    for r1 in rivales1:
        r1.mover()

    for jf in jefe:
        jf.mover()

    fin=False
    reloj = pygame.time.Clock()
    while not fin:
        #Control del Tiempo
        n =  time.time()
        if n < alarm:
            tiempo = (round(alarm - n))
            restante = "Tiempo: " + str(tiempo) + "sg"
            info_restante = info_t.render(restante,True,BLANCO)
        else:
            fin = True
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
                    j.vely = -7
                    j.piso = False
                if event.key == pygame.K_s:
                    #Estado de disparo y creacion de bala
                    if j.arma == 1:
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
                    else:
                        print("no tiene arma")
            if event.type == pygame.KEYUP:
                j.velx = 0

        #Control movimiento jugador con mapa
        if j.rect.x > lim_der:
            j.rect.x = lim_der
            if f_posx > f_lim_der:
                f_velx = -5
            else:
                f_velx = 0

        elif j.rect.x < lim_izq:
            j.rect.x = lim_izq
            if f_posx < f_lim_izq:
                f_velx = 5
            else:
                f_velx = 0

        else:
            f_velx = 0


        #Control movimiento objetos junto con mapa
        for plat in plataformas:
            plat.f_velxs = f_velx
        for bal in balas:
            bal.f_velxs = f_velx
        for riv in rivales1:
            riv.f_velxs = f_velx
        for ri in rivales2:
            ri.f_velxs = f_velx
        for mis in misiles:
            mis.f_velxs = f_velx
        for pi in pistola:
            pi.f_velxs = f_velx
        for tiem in tiempos:
            tiem.f_velxs = f_velx
        for je in jefe:
            je.f_velxs = f_velx
        for sue in suelos:
            sue.f_velxs = f_velx
        for mur in muros:
            mur.f_velxs = f_velx
        for pin in pinchos:
            pin.f_velxs = f_velx
        for pue in puentes:
            pue.f_velxs = f_velx

        for b in balas:
            #Eliminacion de las balas al chocar con bordes y personajes (al impactarlos les baja vida)
            disp1 = pygame.sprite.spritecollide(b,rivales1,False)
            disp2 = pygame.sprite.spritecollide(b,rivales2,False)
            dispj = pygame.sprite.spritecollide(b,jefe,False)
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
            for jf in dispj:
                jf.vidas -= 1
                balas.remove(b)
            for m in dispm:
                misiles.remove(m)
                m.damage = 0
                balas.remove(b)

        #choque de los jugadores con los enemigos, si todavía están en juego le quitan vida al jugador
        col = pygame.sprite.spritecollide(r1,jugadores,False)
        col2 = pygame.sprite.spritecollide(r2,jugadores,False)
        colj = pygame.sprite.spritecollide(jf,jugadores,False)
        if col:
            if r1.damage > 0:
                impacto = True
                j.velx *= -1
                j.vidas -= r1.damage
                vidas = "Vidas: " + str(j.vidas)
        if col2:
            if r2.damage > 0:
                impacto = True
                j.velx *= -1
                j.vidas -= r2.damage
                vidas = "Vidas: " + str(j.vidas)
        if colj:
            if jf.damage > 0:
                impacto = True
                j.velx *= -1
                j.vidas -= jf.damage
                vidas = "Vidas: " + str(j.vidas)

        #recoger modificadores
        ars = pygame.sprite.spritecollide(gun,jugadores,False)
        tie = pygame.sprite.spritecollide(t,jugadores,False)

        if ars:
            pistola.remove(gun)
            j.arma = 1

        if tie:
            tiempo.remove(t)

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
                m.velx = 5
                misiles.add(m)
                r2.temp = random.randrange(100)

        for jf in jefe:
            jf.morir()
            if jf.estado == 3:
                jefe.remove(jf)
                jf.damage = 0


        #eliminación de los misiles cuando tocan al jugador (le bajan vida) o llegan a los bordes
        for m in misiles:
            if m.rect.x < 0 or m.rect.x > ANCHO:
                misiles.remove(m)
                m.damage = 0
            en = pygame.sprite.spritecollide(m,jugadores,False)
            if en:
                j.vidas -= m.damage
                vidas = "Vidas: " + str(j.vidas)
                misiles.remove(m)
                m.damage = 0

        #muerte del jugador
        j.morir()
        vidas = "Vidas: " + str(j.vidas)
        if j.estado==5:
            jugadores.remove(j)
            fin = True

        #Refresco
        #Update
        suelos.update()
        plataformas.update()
        muros.update()
        puentes.update()
        pinchos.update()
        jugadores.update()
        rivales1.update()
        rivales2.update()
        balas.update()
        misiles.update()
        jefe.update()
        #Dibujo de fondo
        ventana.blit(fondo,[f_posx,f_posy])
        #Dibujo objetos
        suelos.draw(ventana)
        plataformas.draw(ventana)
        muros.draw(ventana)
        puentes.draw(ventana)
        pinchos.draw(ventana)
        rivales1.draw(ventana)
        rivales2.draw(ventana)
        misiles.draw(ventana)
        balas.draw(ventana)
        jugadores.draw(ventana)
        plataformas.draw(ventana)
        pistola.draw(ventana)
        tiempos.draw(ventana)
        jefe.draw(ventana)
        #Mensajes
        info_vidas = info_t.render(vidas,True,BLANCO)
        ventana.blit(info_vidas,[190,10])
        ventana.blit(info_restante,[10,10])
        pygame.display.flip()
        reloj.tick(20)

        #Movimiento fondo
        f_posx += f_velx
