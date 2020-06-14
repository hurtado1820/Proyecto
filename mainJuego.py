import pygame
from nivel1 import *
from nivel2 import *
from cargarmapa1 import *
from cargarmapa2 import *

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    reloj = pygame.time.Clock()
    Nivel1(ventana)
    print("sali de nivel uno")
    Nivel2(ventana)
    print("sali del juego")
