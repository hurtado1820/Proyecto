from jugador import *
from clases import *
from const import *
from enemigo1 import *
from enemigo3 import *
from enemigo4 import *
import pygame
import random

def recortar(sabana,size,filas,columnas):
    animacion = []
    for f1 in range(filas):
        fila1=[]
        for c1 in range(columnas):
            cuadro1 = sabana.subsurface(size[0]*c1,size[1]*f1,size[0],size[1])
            fila1.append(cuadro1)
        animacion.append(fila1)
    return animacion

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])

    #Grupos
    jugadores = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    balas = pygame.sprite.Group()
    rivales1 = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    rivales3 = pygame.sprite.Group()
    rivales4 = pygame.sprite.Group()
    explosiones = pygame.sprite.Group()
    misiles = pygame.sprite.Group()

    #Creacion jugador
    #j = Jugador([500,190])
    j = Jugador([50,100])
    jugadores.add(j)
    #rivales
    r1 = Enemigo1([200,100])
    rivales1.add(r1)
    r2 = Enemigo2([750,570])
    rivales2.add(r2)
    r3 = Enemigo3([320,30])
    rivales3.add(r3)
    r4 = Enemigo4([410,190])
    rivales4.add(r4)
    #Creacion de plataforma
    p = Plataforma([120,250])
    plataformas.add(p)
    p2 = Plataforma([400,250])
    plataformas.add(p2)
    p3 = Plataforma([750,380])
    plataformas.add(p3)
    p4 = Plataforma([300,100])
    plataformas.add(p4)

    j.plataformas = plataformas
    r1.plataformas = plataformas
    r3.plataformas = plataformas

    for r1 in rivales1:
        r1.mover()

    for r3 in rivales3:
        r3.mover()

    fin=False
    while not fin:
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
            #Eliminacion al salir de pantalla
            disp1 = pygame.sprite.spritecollide(b,rivales1,False)
            disp2 = pygame.sprite.spritecollide(b,rivales2,False)
            disp4 = pygame.sprite.spritecollide(b,rivales4,False)
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
            for r4 in disp4:
                if r4.estado == 1:
                    r4.estado = 2
                    r4.vidas -= 1
                    balas.remove(b)
            for m in dispm:
                misiles.remove(m)
                m.damage = 0
                balas.remove(b)

        col = pygame.sprite.spritecollide(r1,jugadores,False)
        col2 = pygame.sprite.spritecollide(r2,jugadores,False)
        col3 = pygame.sprite.spritecollide(r3,jugadores,False)
        col4 = pygame.sprite.spritecollide(r4,jugadores,False)
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
        if col3:
            if r3.estado == 1:
                impacto = True
                j.velx *= -1
                j.vidas = 0
                print("vidas = ", j.vidas)
        if col4:
            if r4.estado == 1:
                impacto = True
                r4.estado = 2
                r4.vidas -= 1

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

        for r3 in rivales3:
            r3.morir()
            if r3.estado == 2:
                rivales3.remove(r3)

        for r4 in rivales4:
            if r4.estado == 2:
                e = Explosion(r4.rect)
                explosiones.add(e)
                ex = pygame.sprite.spritecollide(e,jugadores,False)
                if ex:
                    j.vidas -= e.damage
                    j.velx *= -1
                    print("vidas = ",j.vidas)
                    explosiones.remove(e)
                    e.damage = 0
            r4.morir()
            if r4.estado == 3:
                rivales4.remove(r4)
                r4.damage = 0


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

        j.morir()
        if j.estado==4:
            jugadores.remove(j)
            fin = True


        jugadores.update()
        rivales1.update()
        rivales2.update()
        rivales3.update()
        rivales4.update()
        balas.update()
        misiles.update()
        explosiones.update()
        ventana.fill(NEGRO)
        rivales1.draw(ventana)
        rivales2.draw(ventana)
        rivales3.draw(ventana)
        rivales4.draw(ventana)
        balas.draw(ventana)
        misiles.draw(ventana)
        explosiones.draw(ventana)
        jugadores.draw(ventana)
        plataformas.draw(ventana)
        pygame.display.flip()
