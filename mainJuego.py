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
from tutorial import *

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    reloj = pygame.time.Clock()
    win = pygame.mixer.Sound("WinMenu.wav")
    firstLevel = pygame.mixer.Sound("FirstLevel.wav")
    secondLevel = pygame.mixer.Sound("SecondLevel.wav")
    death = pygame.mixer.Sound("LoseMenu.wav")
    start = pygame.mixer.Sound("MainMenu.wav")
    pygame.mixer.music.load
    #Pantalla inicio
    start.play()
    Inicio(ventana)
    #Tutorial de juego
    Tutorial(ventana)
    #Historia nivel 1
    H1(ventana)
    start.stop()
    #Llamado a primer nivel
    firstLevel.play()
    primer = Nivel1(ventana)
    # 1 perdio 0 gano
    firstLevel.stop()
    if primer == 1:
        death.play()
        Perdida(ventana)
    elif primer == 0:
        #Historia nivel 2
        H2(ventana)
        #Llamado a segundo nivel
        secondLevel.play()
        segundo = Nivel2(ventana)
        secondLevel.stop()
        if segundo == 0:
            win.play()
            Victoria(ventana)
        else:
            death.play()
            Perdida(ventana)
