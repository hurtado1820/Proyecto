import pygame

def Inicio(ventana):
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                fin = True
        ventana.fill([255,0,0])
        pygame.display.flip()
