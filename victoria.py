import pygame

def Victoria(ventana):
    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                fin = True
        ventana.fill([0,0,255])
        pygame.display.flip()
        reloj.tick(20)
