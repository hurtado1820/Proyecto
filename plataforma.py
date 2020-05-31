import pygame
import random

ANCHO = 1200
ALTO = 600
NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO = [255,0,0]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos,dims):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(dims)
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.piso = False
        self.plataformas = None

    def gravedad(self,g=0.5):
        if self.vely ==  0:
            self.vely = g
        else:
            self.vely += g

    def update(self):
        #Colision en x
        self.rect.x += self.velx
        ls_col = pygame.sprite.spritecollide(self,self.plataformas,False)
        for b in ls_col:
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    self.velx = 0
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    self.velx = 0
        #Colision en y
        self.rect.y += self.vely
        ls_col = pygame.sprite.spritecollide(self,self.plataformas,False)
        for b in ls_col:
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.vely = 0
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.vely = 0

        #Caida en el aire
        if not self.piso:
            self.gravedad()
        #Contacto con el piso
        if self.rect.bottom > ALTO:
            self.vely = 0
            self.rect.bottom = ALTO
            self.piso = True

class Plataforma(pygame.sprite.Sprite):
    def __init__(self,pos,dims):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(dims)
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])

    #Grupos
    jugadores = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()

    #Creacion jugador
    j = Jugador([100,100],[50,70])
    jugadores.add(j)

    #Creacion de plataforma
    p = Plataforma([500,400],[150,50])
    plataformas.add(p)
    p2 = Plataforma([800,350],[150,50])
    plataformas.add(p2)

    j.plataformas = plataformas

    reloj = pygame.time.Clock()
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = 5
                if event.key  == pygame.K_LEFT:
                    j.velx = -5
                if event.key == pygame.K_SPACE:
                    j.vely = -15
                    j.piso = False
            if event.type == pygame.KEYUP:
                j.velx = 0

        #Control

        #Refresco
        jugadores.update()
        ventana.fill(NEGRO)
        jugadores.draw(ventana)
        plataformas.draw(ventana)
        reloj.tick(40)
        pygame.display.flip()
