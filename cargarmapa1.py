import pygame
from spritesMapa import *
import configparser
from const import *

if __name__ == '__main__':

    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    fin = False
    reloj = pygame.time.Clock()

    archivo = configparser.ConfigParser()
    archivo.read("level-one.map")

    #ventana.fill([0,0,0])
    fondo = pygame.image.load("fondoj.jpg")
    ventana.blit(fondo,[0,0])

    info_mapa = archivo.get("info","mapa")
    mapa = info_mapa.split("\n")

    suelos = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    pinchos = pygame.sprite.Group()
    puentes = pygame.sprite.Group()

    j = 0
    for f in mapa:
        i = 0
        for c in f:
            tipo = archivo.get(c,"tipo")
            spr = int(archivo.get(c,"spr"))
            if tipo == "suelo":
                s = Suelo([16*i,16*j],spr)
                suelos.add(s)
            if tipo == "plataforma":
                p = Plataforma([16*i,16*j],spr)
                plataformas.add(p)
            if tipo == "muro":
                m = Muro([16*i,16*j],spr)
                muros.add(m)
            if tipo == "pincho":
                pi = Pincho([16*i,16*j],spr)
                pinchos.add(pi)
            if tipo == "puente":
                pue = Puente([16*i,16*j],spr)
                puentes.add(pue)
            i += 1
        j += 1

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True


        suelos.update()
        plataformas.update()
        muros.update()
        puentes.update()
        pinchos.update()
        ventana.blit(fondo,[0,0])
        suelos.draw(ventana)
        plataformas.draw(ventana)
        muros.draw(ventana)
        puentes.draw(ventana)
        pinchos.draw(ventana)
        pygame.display.flip()
        reloj.tick(20)
