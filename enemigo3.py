import pygame
import random
from const import *
from enemigo import *

class Enemigo3(Enemigo):
    def __init__ (self,pos):#m
        pygame.sprite.Sprite.__init__(self)
        '''self.accion = 1
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]
        self.rect = self.image.get_rect()'''
        self.image = pygame.Surface([60,60])
        self.image.fill(NARANJA)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "rival3"
        self.velx = 0
        self.vely = 0
        self.f_velxs = 0
        self.f_velys = 0
        self.radius = 60
        self.vidas = 1
        self.damage = 4
        self.estado = 1 # 1 cayendo, 2 muerto
        self.bloques = None
        self.pared = None
        self.piso = False
        self.plataformas = None

    def gravedad(self):
        if self.vely ==  0:
            self.vely = 0.5
        else:
            self.vely += 0.5

    def RetPos(self):
        x = self.rect.x + 20
        y = self.rect.bottom
        return [x,y]

    def detener(self):
        self.velx=0
        self.vely=0

    def mover(self):
        self.velx = 1

    def morir(self):
        if self.rect.bottom == ALTO:
            self.estado = 2
            self.detener()

    '''def camino(self):
        if self.velx != 0:
            if self.velx < 0:
                self.accion = 1
            else:
                self.accion = 0
        else:
            self.accion = 2'''

    def update(self):
        #Colision en x
        self.mover()
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

        '''if self.con < 5:
            self.con += 1
        else:
            self.con = 0
            self.accion = self.accion
        self.image = self.animacion[self.accion][self.con]'''
