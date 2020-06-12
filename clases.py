import pygame
from enemigo import *
from const import *
import random

class Enemigo2(Enemigo):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("genera.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.velx = 0
        self.vely = 0
        self.type = "rival2"
        self.vidas = 1
        self.damage = 1
        self.estado = 1
        self.temp = random.randrange(100)

   def update(self):
       self.temp -= 1
       self.rect.x += self.f_velxs

   def morir(self):
       if self.vidas <= 0:
           self.estado = 2

class Misil(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.damage = 1
        self.f_velxs = 0

    def update(self):
        self.rect.x = self.rect.x + self.velx
        self.rect.y = self.rect.y + self.vely
        self.rect.x += self.f_velxs

class Bala(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0

    def update(self):
        self.rect.x = self.rect.x + self.velx
        self.rect.y = self.rect.y + self.vely

class Explosion(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([100,100])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0
        self.damage = 2

class Plataforma(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200,80])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
