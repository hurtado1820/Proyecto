import pygame
from const import *

class Jugador(pygame.sprite.Sprite):
    def __init__ (self,pos):#m
        pygame.sprite.Sprite.__init__(self)
        '''self.accion = 1
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]'''
        self.image = pygame.Surface([60,60])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        #self.lim = [7,7,2,2,7,7,2,2]
        self.dir = 1 #1: derecha, 2:izquierda
        self.velx = 0
        self.vely = 0
        self.vidas = 5
        self.aturdido = 0
        self.arma = 0
        self.estado = 1  # 1 estándar, 2 velocidad, 3 con las gemas, 4 aturdido, 5 muerto
        self.bloques = None
        self.pared = None
        self.piso = False
        self.plataformas = None
        self.inventario = [0,0,0,0] #gemas, vidas, buff, tiempo

    '''def animar(self):
        if self.velx != self.vely:
            if self.con < self.lim[self.accion]:
                self.con += 1
            else:
                self.con = 0
                self.accion = self.accion
            self.image = self.animacion[self.accion][self.con]'''

    def gravedad(self):
        if self.vely ==  0:
            self.vely = 0.5
        else:
            self.vely += 0.5

    def update(self):
        #Colision en x
        self.limites()
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

        #self.animar()

    #función temporal para mantener al jugador en la pantalla
    def limites(self):
        self.rect.x += self.velx
        if (self.rect.right > ANCHO - 1) and (self.velx > 0):
            self.velx = 0
        if (self.rect.left < 1) and (self.velx < 0):
            self.velx = 0

    def RetPos(self):
        x = (self.rect.x) + 10
        y = self.rect.y + 20
        return [x,y]

    def detener(self):
        self.velx=0
        self.vely=0
        self.estado = 1


    def aturdir(self):
        if self.aturdido == 1:
            self.estado = 4

    #cuando recoge el buff activa el estado de velocidad
    def mayo_rakuin(self):
         if self.inventario[2] > 0:
             self.aturdido = 0
             self.estado = 2
             self.inventario[2] -= 1

    #cuando tiene ambos objetos pasa al estado 5 (en el que puede ganar?)
    def gemas(self):
        if self.inventario[0] == 2:
            self.estado = 3

    # Muerte ; cuando las vidas llegan a 0
    def morir(self):
         if self.vidas <= 0:
            self.detener()
            self.estado = 5
