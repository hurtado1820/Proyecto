import pygame
from nivel1 import *
from nivel2 import *
from cargarmapa1 import *
from cargarmapa2 import *

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    reloj = pygame.time.Clock()
    primer = Nivel1(ventana)
    # 1 perdio 0 gano
    if primer == 1:
        print("Perdiooooo")
    elif primer == 0:
        segundo = Nivel2(ventana)
        if segundo == 0:
            print("Ganooooooo")
        else:
            print("Perdiooooo")   
