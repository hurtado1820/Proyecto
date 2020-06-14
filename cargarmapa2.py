import pygame
from spritesMapa import *
import configparser
from const import *

def CargaMapa2(suelos,plataformas,muros,pinchos,puentes):

    archivo = configparser.ConfigParser()
    archivo.read("level-two.map")

    info_mapa = archivo.get("info","mapa")
    mapa = info_mapa.split("\n")

    j = 0
    for f in mapa:
        i = 0
        for c in f:
            tipo = archivo.get(c,"tipo")
            spr = int(archivo.get(c,"spr"))
            if tipo == "suelo":
                s = Suelo([48*i,48*j],spr)
                suelos.add(s)
            if tipo == "plataforma":
                p = Plataforma([48*i,48*j],spr)
                plataformas.add(p)
            if tipo == "muro":
                m = Muro([48*i,48*j],spr)
                muros.add(m)
            if tipo == "pincho":
                pi = Pincho([48*i,48*j],spr)
                pinchos.add(pi)
            if tipo == "puente":
                pue = Puente([48*i,48*j],spr)
                puentes.add(pue)
            i += 1
        j += 1
