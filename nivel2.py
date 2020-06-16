from jugador import *
from clases import *
from const import *
from enemigo3 import *
from enemigo4 import *
from modificadores import *
import pygame
import random
import time
from cargarmapa2 import *
from spritesMapa import *
from jefe2 import *
from barras import *

def Nivel2(ventana):
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
    rivales3 = pygame.sprite.Group()
    rivales4 = pygame.sprite.Group()
    jefe2 = pygame.sprite.Group()
    piedras = pygame.sprite.Group()
    gen = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    boost = pygame.sprite.Group()
    health = pygame.sprite.Group()
    suelos = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    pinchos = pygame.sprite.Group()
    puentes = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    lava = pygame.sprite.Group()
    vacios = pygame.sprite.Group()
    monumentos = pygame.sprite.Group()
    gemas = pygame.sprite.Group()
    nada = pygame.sprite.Group()
    explosiones = pygame.sprite.Group()
    barrajug = pygame.sprite.Group()
    barrajef2 = pygame.sprite.Group()

    #sabanas y recortes
    en3_spr = pygame.image.load("enemigo3.png")
    en3 = []
    for c in range(4):
        cuadro = en3_spr.subsurface(48*c,0,48,54)
        en3.append(cuadro)

    en4_spr = pygame.image.load("enemigo4.png")
    en4 = []
    for f1 in range(4):
        fila1=[]
        for c1 in range(4):
            cuadro1 = en4_spr.subsurface(40*c1,53*f1,40,53)
            fila1.append(cuadro1)
        en4.append(fila1)

    boom_spr = pygame.image.load("explosion.png")
    exp = []
    for f2 in range(2):
        fila2=[]
        for c2 in range(5):
            cuadro2 = boom_spr.subsurface(70*c2,66*f2,70,66)
            fila2.append(cuadro2)
        exp.append(fila2)

    jf2_spr = pygame.image.load("jefe2.png")
    jef2 = []
    for f3 in range(2):
        fila3=[]
        for c3 in range(4):
            cuadro3 = jf2_spr.subsurface(101*c3,100*f3,101,100)
            fila3.append(cuadro3)
        jef2.append(fila3)

    bar_spr = pygame.image.load("bar.png")
    barra = []
    for f4 in range(6):
        cuadro4 = bar_spr.subsurface(106*0,30*f4,106,30)
        barra.append(cuadro4)

    CargaMapa2(suelos,plataformas,muros,pinchos,puentes,lava,vacios)

    #Creacion personajes
    j = Jugador([350,200])
    jugadores.add(j)
    r3 = Enemigo3([250,30],en3)
    rivales3.add(r3)
    r4a = Enemigo4([4320,427],en4)
    rivales4.add(r4a)
    r4b = Enemigo4([4320,235],en4)
    rivales4.add(r4b)
    jf2 = Jefe2([2074,485],jef2)
    jefe2.add(jf2)
    bjf2 = BarraJefe2([2024,435],barra)
    barrajef2.add(bjf2)
    monument = Monumento([1720,480])
    monumentos.add(monument)

    #Stop
    n1=Stop([1500,460])
    nada.add(n1)
    n2=Stop([2600,460])
    nada.add(n2)
    n3=Stop([1500,435])
    nada.add(n3)
    n4=Stop([2600,435])
    nada.add(n4)

    #generadores
    g1=Generador([1600,100])
    gen.add(g1)
    g2=Generador([1800,100])
    gen.add(g2)
    g3=Generador([2000,100])
    gen.add(g3)
    g4=Generador([2200,100])
    gen.add(g4)
    g5=Generador([2400,100])
    gen.add(g5)
    g6=Generador([2600,100])
    gen.add(g6)

    #modificadores
    v = Boost([560,385])
    boost.add(v)
    s = Salud([2352,1968])
    health.add(s)

    bj = BarraJugador([170,5],barra)
    barrajug.add(bj)


    #Sprites con los que colisionan
    j.plataformas = plataformas
    j.suelos = suelos
    j.muros = muros
    jf2.stop = nada
    r3.plataformas = plataformas
    r3.suelos = suelos
    bjf2.stop = nada

    #Texto control vida jugador
    '''info = pygame.font.Font(None,30)
    vidas = "Vidas: " + str(j.vidas)
    info_vidas = info.render(vidas,True,BLANCO)'''

    #Timer del juego
    cont = 0
    tiempo = 0
    info_t = pygame.font.Font(None,30)
    restante = "Tiempo: " + str(tiempo) + "sg"
    info_restante = info_t.render(restante,True,BLANCO)
    p = 250.00
    alarm = time.time() + p

    #Movimiento inicial rival 3
    for r3 in rivales3:
        r3.mover()

    for jf2 in jefe2:
        jf2.mover()

    for bjf2 in barrajef2:
        bjf2.mover()

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
            return 1
        #movimiento del jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if j.estado == 1:
                        j.velx = 7
                    if j.estado == 2:
                        j.velx = 10
                    if j.estado == 4:
                        j.velx = 5
                    j.dir=1
                if event.key  == pygame.K_LEFT:
                    if j.estado == 1:
                        j.velx = -7
                    if j.estado == 2:
                        j.velx = -10
                    if j.estado == 4:
                        j.velx = -5
                    j.dir= 2
                if event.key == pygame.K_SPACE:
                    if j.estado == 1:
                        j.vely = -12
                    if j.estado == 2:
                        j.vely = -16
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
        for ri in rivales4:
            ri.f_velxs = f_velx
            ri.f_velys = f_vely
        for pi in boost:
            pi.f_velxs = f_velx
            pi.f_velys = f_vely
        for tiem in health:
            tiem.f_velxs = f_velx
            tiem.f_velys = f_vely
        for je in jefe2:
            je.f_velxs = f_velx
            je.f_velys = f_vely
        for sue in suelos:
            sue.f_velxs = f_velx
            sue.f_velys = f_vely
        for mur in muros:
            mur.f_velxs = f_velx
            mur.f_velys = f_vely
        for pin in pinchos:
            pin.f_velxs = f_velx
            pin.f_velys = f_vely
        for pue in puentes:
            pue.f_velxs = f_velx
            pue.f_velys = f_vely
        for pie in piedras:
            pie.f_velxs = f_velx
            pie.f_velys = f_vely
        for ge in gen:
            ge.f_velxs = f_velx
            pue.f_velys = f_vely
        for mon in monumentos:
            mon.f_velxs = f_velx
            mon.f_velys = f_vely
        for lav in lava:
            lav.f_velxs = f_velx
            lav.f_velys = f_vely
        for va in vacios:
            va.f_velxs = f_velx
            va.f_velys = f_vely
        for gm in gemas:
            gm.f_velxs = f_velx
            gm.f_velys = f_vely
        for bo in explosiones:
            bo.f_velxs = f_velx
            bo.f_velys = f_vely
        for bjf in barrajef2:
            bjf.f_velxs = f_velx
            bjf.f_velys = f_vely

        #Control del jefe, se remueve al morir, controla los generadores de piedras
        for jf2 in jefe2:
            jf2.morir()
            if jf2.estado == 3:
                gemal = Gem2(jf2.rect)
                gemas.add(gemal)
                jefe2.remove(jf2)
                barrajef2.remove(bjf2)
                jf2.damage = 0
                for g in gen:
                    g.estado = 2

        #Generador de piedras
        for g in gen:
            if g.estado == 1:
                if g.temp < 0:
                    pi = Piedra(g.rect)
                    pi.vely = 5
                    piedras.add(pi)
                    g.temp = random.randrange(100)

        #Control de balas
        for b in balas:
            dispj2 = pygame.sprite.spritecollide(b,jefe2,False)
            choq = pygame.sprite.spritecollide(b,plataformas,False)
            disp3 = pygame.sprite.spritecollide(b,rivales3,False)
            disp4 = pygame.sprite.spritecollide(b,rivales4,False)
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
                    pos_ex = r4.rect
                    r4.estado = 2
                    balas.remove(b)
                    ex = Explode(pos_ex,exp)
                    explosiones.add(ex)
            '''for jf2 in dispj2:
                if jf2.estado < 3:
                    jf2.vidas -= 1
                    half = round(jf2.vidas / 2)
                    bjf2.nivel = half - 1
                    balas.remove(b)'''
            for pi in piedras:
                piedras.remove(pi)
                pi.damage = 0
                balas.remove(b)
            for mon in monumentos:
                mon.f_velxs = f_velx
                mon.f_velys = f_vely

        #Choque de jugador con enemigos
        colj2 = pygame.sprite.spritecollide(jf2,jugadores,False)
        col3 = pygame.sprite.spritecollide(r3,jugadores,False)
        if colj2:
            if jf2.damage > 0:
                impacto = True
                j.velx *= 0.2
                j.vely = -1
                #vidas = "Vidas: " + str(j.vidas)
        if col3:
            if r3.estado == 1:
                impacto = True
                j.vidas = 0
                #vidas = "Vidas: " + str(j.vidas)
        for r4 in rivales4:
            col4 = pygame.sprite.spritecollide(r4,jugadores,False)
            if col4:
                if r4.estado == 1:
                    pos_ex = r4.rect
                    impacto = True
                    r4.estado = 2
                    j.velx *= -1
                    j.vidas -= r4.damage
                    bj.nivel = j.vidas - 1
                    #vidas = "Vidas: " + str(j.vidas)
                    r4.vidas -= 1
                    ex = Explode(pos_ex,exp)
                    explosiones.add(ex)
        for lv in lava:
             colav = pygame.sprite.spritecollide(lv,jugadores,False)
             if colav:
                 if lav.damage > 0:
                     impacto = True
                     j.vidas -= lav.damage
                     bj.nivel = j.vidas - 1
                     j.velx *= -1
                     j.vely *= -1
                     pc.damage = 0
                     #vidas = "Vidas: " + str(j.vidas)

        #recoger modificadores
        speed = pygame.sprite.spritecollide(v,jugadores,False)
        sal = pygame.sprite.spritecollide(s,jugadores,False)
        monu = pygame.sprite.spritecollide(j,monumentos,False)
        ge = pygame.sprite.spritecollide(j,gemas,True)

        if speed:
            boost.remove(v)
            j.inventario[2] += 1
            j.mayo_rakuin()

        if sal:
            health.remove(s)
            j.vidas += s.poder
            bj.nivel = j.vidas - 1
            s.poder = 0

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

        #Control piedras generadas por jefe
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
                bj.nivel = j.vidas - 1
                #vidas = "Vidas: " + str(j.vidas)
                piedras.remove(pi)
                pi.damage = 0

        for r3 in rivales3:
            r3.morir()
            if r3.estado == 2:
                rivales3.remove(r3)

        for r4 in rivales4:
            if r4.estado == 2:
                rivales4.remove(r4)
                r4.damage = 0
        for ex in explosiones:
            if ex.estado == 2:
                explosiones.remove(ex)

        j.morir()
        #vidas = "Vidas: " + str(j.vidas)
        if j.estado==5:
            jugadores.remove(j)
            fin = True
            return 1

        #Refresco
        #Update
        monumentos.update()
        jugadores.update()
        balas.update()
        piedras.update()
        rivales3.update()
        rivales4.update()
        jefe2.update()
        gen.update()
        plataformas.update()
        suelos.update()
        nada.update()
        muros.update()
        puentes.update()
        pinchos.update()
        vacios.update()
        boost.update()
        health.update()
        gemas.update()
        explosiones.update()
        barrajug.update()
        barrajef2.update()
        lava.update()
        #Dibujo fondo
        ventana.blit(fondo,[f_posx,f_posy])
        #Dibujo objetos
        monumentos.draw(ventana)
        explosiones.draw(ventana)
        suelos.draw(ventana)
        nada.draw(ventana)
        rivales3.draw(ventana)
        rivales4.draw(ventana)
        piedras.draw(ventana)
        gen.draw(ventana)
        balas.draw(ventana)
        boost.draw(ventana)
        health.draw(ventana)
        jugadores.draw(ventana)
        jefe2.draw(ventana)
        plataformas.draw(ventana)
        vacios.draw(ventana)
        muros.draw(ventana)
        puentes.draw(ventana)
        pinchos.draw(ventana)
        boost.draw(ventana)
        health.draw(ventana)
        gemas.draw(ventana)
        barrajug.draw(ventana)
        barrajef2.draw(ventana)
        lava.draw(ventana)
        #Mensajes
        #info_vidas = info_t.render(vidas,True,BLANCO)
        #ventana.blit(info_vidas,[190,10])
        ventana.blit(info_restante,[10,10])
        pygame.display.flip()
        reloj.tick(40)

        #Movimiento fondo
        f_posx += f_velx
        f_posy += f_vely
