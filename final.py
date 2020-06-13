import pygame

def Victoria(ventana):
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                fin = True
        ventana.fill([255,0,255])
        pygame.display.flip()


def Perdida(ventana):
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                fin = True
        ventana.fill([0,255,0])
        pygame.display.flip()
