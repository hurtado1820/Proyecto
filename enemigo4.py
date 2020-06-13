import pygame
from enemigo import *
from const import *
import random

class Enemigo4(Enemigo):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        self.image.fill(VERDOSC)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.velx = 0
        self.vely = 0
        self.type = "rival4"
        self.vidas = 1
        self.damage = 4
        self.estado = 1 #1 activo, 2 explosion 3, inactivo

   def morir(self):
       if self.vidas <= 0:
           self.estado = 3
