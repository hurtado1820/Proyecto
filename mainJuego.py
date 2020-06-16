import pygame
from nivel1 import *
from nivel2 import *
from cargarmapa1 import *
from cargarmapa2 import *
from inicio import *
from victoria import *
from perdida import *
from historia1 import *
from historia2 import *

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    reloj = pygame.time.Clock()
    Inicio(ventana)
    H1(ventana)
    primer = Nivel1(ventana)
    # 1 perdio 0 gano
    if primer == 1:
        Perdida(ventana)
    elif primer == 0:
        H2(ventana)
        segundo = Nivel2(ventana)
        if segundo == 0:
            Victoria(ventana)
        else:
            Perdida(ventana)
