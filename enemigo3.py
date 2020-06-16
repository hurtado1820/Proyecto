import pygame
import random
from const import *
from enemigo import *

class Enemigo3(Enemigo):
    def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.con]
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
        self.suelo = None

    def gravedad(self):
        if self.vely ==  0:
            self.vely = 0.3
        else:
            self.vely += 0.3

    def detener(self):
        self.velx=0
        self.vely=0

    def mover(self):
        self.velx = 2

    def morir(self):
        if self.rect.bottom == ALTO:
            self.estado = 2
            self.detener()

    def update(self):
        #Colision en x
        self.mover()
        self.rect.x += self.velx
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
        ls_col_s = pygame.sprite.spritecollide(self,self.suelos,False)
        for m in ls_col_s:
            if self.vely > 0:
                if self.rect.bottom >= m.rect.top:
                    self.rect.bottom = m.rect.top
                    self.vely = 0
        #Caida en el aire
        if not self.piso:
            self.gravedad()
        #Contacto con el piso
        if self.rect.bottom > ALTO:
            self.vely = 0
            self.rect.bottom = ALTO
            self.piso = True
        if self.con < 3:
            self.con += 1
        else:
            self.con = 0
        self.image = self.animacion[self.con]
