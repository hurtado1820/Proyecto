from jugador import *
from clases import *
from const import *
from enemigo1 import *
from modificadores import *
import pygame
import random
import time
from cargarmapa1 import *
from spritesMapa import *

def Nivel1(ventana):
    pygame.font.init()

    fondo = pygame.image.load("background.png")
    ventana.blit(fondo,[0,0])

    #Info mapa en x
    f_info = fondo.get_rect()
    f_velx = 0
    f_posx = 0
    lim_der = ANCHO - 200
    lim_izq = 200
    f_lim_izq = 0
    f_lim_der = ANCHO - f_info[2]

    #Info mapa en y
    f_vely = 0
    f_posy = 0
    lim_arri = 200
    lim_aba = ALTO - 200
    f_lim_arri = 0
    f_lim_aba = ALTO - f_info[3]

    #Grupos
    jugadores = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    rivales1 = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    misiles = pygame.sprite.Group()
    pistolas = pygame.sprite.Group()
    tiempos = pygame.sprite.Group()
    jefe = pygame.sprite.Group()
    suelos = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    proyectiles = pygame.sprite.Group()
    pinchos = pygame.sprite.Group()
    puentes = pygame.sprite.Group()
    vacios = pygame.sprite.Group()
    monumentos = pygame.sprite.Group()
    nada = pygame.sprite.Group()
    gemas = pygame.sprite.Group()

    #sabanas y recortes
    en1_spr = pygame.image.load("enemigo1.png")
    en1 = []
    for f in range(4):
        fila=[]
        for c in range(4):
            cuadro = en1_spr.subsurface(80*c,79*f,80,79)
            fila.append(cuadro)
        en1.append(fila)

    jf1_spr = pygame.image.load("jefe1.png")
    jef1 = []
    for f1 in range(2):
        fila1=[]
        for c1 in range(4):
            cuadro1 = jf1_spr.subsurface(100*c1,102*f1,100,102)
            fila1.append(cuadro1)
        jef1.append(fila1)

    CargaMapa1(suelos,plataformas,muros,pinchos,puentes,vacios)

    #Creacion personajes
    j = Jugador([266,90])
    jugadores.add(j)
    r1 = Enemigo1([720,240],en1)
    rivales1.add(r1)
    r1 = Enemigo1([2544,670],en1)
    rivales1.add(r1)
    r2 = Enemigo2([4120,1114])
    rivales2.add(r2)
    r2 = Enemigo2([4120,826])
    rivales2.add(r2)
    jf = Jefe1([2100,332],jef1)
    jefe.add(jf)

    #Stop
    n1=Stop([570,240])
    nada.add(n1)
    n2=Stop([870,240])
    nada.add(n2)
    n3=Stop([2244,670])
    nada.add(n3)
    n4=Stop([2844,670])
    nada.add(n4)
    n5=Stop([1800,346])
    nada.add(n5)
    n6=Stop([3300,332])
    nada.add(n6)

    #modificadores
    gun = Pistola([960,2112])
    pistolas.add(gun)
    t = Tiempo([4656,1536])
    tiempos.add(t)

    #Sprites con los que colisionan
    j.plataformas = plataformas
    j.suelos = suelos
    j.muros = muros
    jf.suelos = suelos
    jf.pared = muros
    jf.stop = nada
    for r1 in rivales1:
        r1.stop = nada

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


    #Movimiento inicial rival1 y jefe
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
            if j.inventario[3] > 0:
                p = 100.00
                alarm = time.time() + p
                j.inventario[3] = 0
            else:
                fin = True
                return 1

        #control del jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = 7
                    j.dir=1
                if event.key  == pygame.K_LEFT:
                    j.velx = -7
                    j.dir=2
                if event.key == pygame.K_SPACE:
                    j.vely = -12
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

        #Control movimiento en x jugador con mapa
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

        #Control movimiento en y jugador con mapa
        if j.rect.y > lim_aba:
            j.rect.y = lim_aba
            if f_posy > f_lim_aba:
                f_vely = -5
            else:
                f_vely = 0

        elif j.rect.y < lim_arri:
            j.rect.y = lim_arri
            if f_posy < f_lim_arri:
                f_vely = 5
            else:
                f_vely = 0

        else:
            f_vely = 0


        #Control movimiento objetos junto con mapa
        for plat in plataformas:
            plat.f_velxs = f_velx
            plat.f_velys = f_vely
        for bal in balas:
            bal.f_velxs = f_velx
            bal.f_velys = f_vely
        for na in nada:
            na.f_velxs = f_velx
            na.f_velys = f_vely
        for riv in rivales1:
            riv.f_velys = f_vely
            riv.f_velxs = f_velx
        for ri in rivales2:
            ri.f_velxs = f_velx
            ri.f_velys = f_vely
        for mis in misiles:
            mis.f_velxs = f_velx
            mis.f_velys = f_vely
        for pi in pistolas:
            pi.f_velxs = f_velx
            pi.f_velys = f_vely
        for tiem in tiempos:
            tiem.f_velxs = f_velx
            tiem.f_velys = f_vely
        for je in jefe:
            je.f_velys = f_vely
            je.f_velxs = f_velx
        for sue in suelos:
            sue.f_velxs = f_velx
            sue.f_velys = f_vely
        for pro in proyectiles:
            pro.f_velxs = f_velx
            pro.f_velys = f_vely
        for mur in muros:
            mur.f_velxs = f_velx
            mur.f_velys = f_vely
        for pin in pinchos:
            pin.f_velxs = f_velx
            pin.f_velys = f_vely
        for pue in puentes:
            pue.f_velxs = f_velx
            pue.f_velys = f_vely
        for mon in monumentos:
            mon.f_velxs = f_velx
            mon.f_velys = f_vely
        for va in vacios:
            va.f_velxs = f_velx
            va.f_velys = f_vely
        for gm in gemas:
            gm.f_velxs = f_velx
            gm.f_velys = f_vely

        for b in balas:
            #Eliminacion de las balas al chocar con bordes y personajes (al impactarlos les baja vida)
            disp1 = pygame.sprite.spritecollide(b,rivales1,False)
            disp2 = pygame.sprite.spritecollide(b,rivales2,False)
            dispj = pygame.sprite.spritecollide(b,jefe,False)
            dispr = pygame.sprite.spritecollide(b,proyectiles,False)
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
            for pr in dispr:
                proyectiles.remove(pr)
                pr.damage = 0
                balas.remove(b)
            for m in dispm:
                misiles.remove(m)
                m.damage = 0
                balas.remove(b)

        #choque de los jugadores con los enemigos, si todavía están en juego le quitan vida al jugador

        colj = pygame.sprite.spritecollide(jf,jugadores,False)
        for r1 in rivales1:
            col = pygame.sprite.spritecollide(r1,jugadores,False)
            if col:
                if r1.damage > 0:
                    impacto = True
                    j.vidas -= r1.damage
                    j.velx *= -1
                    j.vely = 5
                    vidas = "Vidas: " + str(j.vidas)
        for r2 in rivales2:
            col2 = pygame.sprite.spritecollide(r2,jugadores,False)
            if col2:
                if r2.damage > 0:
                    impacto = True
                    j.vidas -= r2.damage
                    j.velx *= -1
                    vidas = "Vidas: " + str(j.vidas)
        for pc in pinchos:
            col3 = pygame.sprite.spritecollide(pc,jugadores,False)
            if col3:
                if pc.damage > 0:
                    impacto = True
                    j.vidas -= pc.damage
                    j.velx *= -1
                    j.vely *= -1
                    pc.damage = 0
                    vidas = "Vidas: " + str(j.vidas)
        if colj:
            if jf.damage > 0:
                impacto = True
                j.vidas -= jf.damage
                j.velx *= -1
                vidas = "Vidas: " + str(j.vidas)


        #recoger modificadores
        ars = pygame.sprite.spritecollide(gun,jugadores,False)
        tie = pygame.sprite.spritecollide(t,jugadores,False)
        monu = pygame.sprite.spritecollide(j,monumentos,False)
        ge = pygame.sprite.spritecollide(j,gemas,True)

        if ars:
            pistolas.remove(gun)
            j.arma = 1

        if tie:
            tiempo.remove(t)
            j.inventario[3] = 1

        if monu:
            if j.inventario[0] > 0:
                fin = True
                j.inventario[0] = 0
                return 0

        if ge:
            j.inventario[0] += 1

        #Muere al tocar el vacio
        muer =  pygame.sprite.spritecollide(j,vacios,False)
        if muer:
            j.vidas = 0
            return 1

        #control de muerte de los rivales
        for r1 in rivales1:
            r1.morir()
            if r1.estado == 3:
                rivales1.remove(r1)
                r1.damage = 0

        for r2 in rivales2:
            r2.morir()
            if r2.estado == 2:
                r2.temp = -1
                r2.damage = 0
            if r2.temp < 0:
                direccion = random.randrange(250)
                m = Misil(r2.rect)
                if direccion < 125:
                    m.velx = 5
                elif direccion < 250:
                    m.velx = -5
                misiles.add(m)
                r2.temp = random.randrange(100)

        for jf in jefe:
            jf.morir()
            if jf.estado == 3:
                jefe.remove(jf)
                jf.damage = 0
            if jf.temp < 0:
                posj = jf.RetPos()
                pr = Proyectil(posj)
                pr2 = Proyectil(posj)
                if jf.accion == 0:
                    pr.velx = 5
                elif jf.accion == 1:
                    pr.velx = -5
                proyectiles.add(pr)
                proyectiles.add(pr2)
                pr2.vely = -5
                jf.temp = random.randrange(100)


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

        for pr in proyectiles:
            pry = pygame.sprite.spritecollide(pr,jugadores,False)
            if pry:
                if pr.damage > 0:
                    impacto = True
                    j.velx *= -1
                    j.vidas -= 1
                    proyectiles.remove(pr)
                    pr.damage = 0
            prym = pygame.sprite.spritecollide(pr,muros,False)
            if prym:
                proyectiles.remove(pr)
                pr.damage = 0

        #muerte del jugador
        j.morir()
        vidas = "Vidas: " + str(j.vidas)
        if j.estado==5:
            jugadores.remove(j)
            fin = True
            return 1

        #Refresco
        #Update
        monumentos.update()
        suelos.update()
        plataformas.update()
        muros.update()
        puentes.update()
        pinchos.update()
        vacios.update()
        jugadores.update()
        rivales1.update()
        rivales2.update()
        balas.update()
        misiles.update()
        proyectiles.update()
        jefe.update()
        pistolas.update()
        tiempos.update()
        gemas.update()
        nada.update()
        #Dibujo de fondo
        ventana.blit(fondo,[f_posx,f_posy])
        #Dibujo objetos
        monumentos.draw(ventana)
        suelos.draw(ventana)
        nada.draw(ventana)
        proyectiles.draw(ventana)
        plataformas.draw(ventana)
        muros.draw(ventana)
        puentes.draw(ventana)
        pinchos.draw(ventana)
        vacios.draw(ventana)
        rivales1.draw(ventana)
        rivales2.draw(ventana)
        misiles.draw(ventana)
        balas.draw(ventana)
        jugadores.draw(ventana)
        pistolas.draw(ventana)
        tiempos.draw(ventana)
        jefe.draw(ventana)
        gemas.draw(ventana)
        #Mensajes
        info_vidas = info_t.render(vidas,True,BLANCO)
        ventana.blit(info_vidas,[190,10])
        ventana.blit(info_restante,[10,10])
        pygame.display.flip()
        reloj.tick(40)

        #Movimiento fondo
        f_posx += f_velx
        f_posy += f_vely
