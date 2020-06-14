import pygame
from const import *
import random

class Salud(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,15])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.poder = 1
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
         self.rect.x += self.f_velxs
         self.rect.y += self.f_velys

class Boost(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,15])
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.activo = 1
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
         self.rect.x += self.f_velxs
         self.rect.y += self.f_velys

class Tiempo(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,15])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.activo = 1
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
         self.rect.x += self.f_velxs
         #self.rect.y += self.f_velys

class Pistola(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,15])
        self.image.fill(MORADO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.activo = 1
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
         self.rect.x += self.f_velxs
         #self.rect.y += self.f_velys
