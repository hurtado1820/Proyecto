import pygame
from const import *
import random

class BarraJugador(pygame.sprite.Sprite):
    def __init__ (self,pos,m):#m
        pygame.sprite.Sprite.__init__(self)
        self.nivel = 5
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.nivel]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.nivel = self.nivel
        self.image = self.animacion[self.nivel]

class BarraJefe1(pygame.sprite.Sprite):
    def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.nivel = 5
        self.animacion = m
        self.image = self.animacion[self.nivel]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.f_velxs = 0
        self.f_velys = 0
        self.stop = None

    def rebotar(self):
        ls_col = pygame.sprite.spritecollide(self,self.stop,False)
        if ls_col:
            self.velx *= -1

    def update(self):
        #Colision en x
        self.rebotar()
        self.rect.x += self.velx
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys
        self.nivel = self.nivel
        self.image = self.animacion[self.nivel]

    def mover(self):
        self.velx = 7

class BarraJefe2(pygame.sprite.Sprite):
    def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.nivel = 5
        self.animacion = m
        self.image = self.animacion[self.nivel]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.f_velxs = 0
        self.f_velys = 0
        self.stop = None

    def rebotar(self):
        ls_col = pygame.sprite.spritecollide(self,self.stop,False)
        if ls_col:
            self.velx *= -1

    def update(self):
        #Colision en x
        self.rebotar()
        self.rect.x += self.velx
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys
        self.nivel = self.nivel
        self.image = self.animacion[self.nivel]

    def mover(self):
        self.velx = 7
