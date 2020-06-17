import pygame

def Inicio(ventana):
    fondo = pygame.image.load("MainTitle.jpg")
    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fin = True
        ventana.blit(fondo,[0,0])
        pygame.display.flip()
        reloj.tick(20)
