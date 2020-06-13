import pygame
from final import *

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([400,400])
    Victoria(ventana)
    Perdida(ventana)
