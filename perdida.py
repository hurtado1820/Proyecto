import pygame

def Perdida(ventana):
    fondo = pygame.image.load("LoseTitle.jpg")
    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                fin = True
        ventana.blit(fondo,[0,0])
        pygame.display.flip()
        reloj.tick(20)
