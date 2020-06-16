import pygame
from const import *
import random

class Salud(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("vida.png")
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
        self.image = pygame.image.load("boost.png")
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
        self.image = pygame.image.load("reloj.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.activo = 1
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
         self.rect.x += self.f_velxs
         self.rect.y += self.f_velys

class Pistola(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pistola.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.activo = 1
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
         self.rect.x += self.f_velxs
         self.rect.y += self.f_velys
