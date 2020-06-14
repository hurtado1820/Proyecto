import pygame
from spritesMapa import *
import configparser
from const import *

def CargaMapa1(suelos,plataformas,muros,pinchos,puentes):

    archivo = configparser.ConfigParser()
    archivo.read("level-one.map")

    info_mapa = archivo.get("info","mapa")
    mapa = info_mapa.split("\n")

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
