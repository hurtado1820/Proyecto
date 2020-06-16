import pygame
from enemigo import *
from const import *
import random

class Enemigo4(Enemigo):
   def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.con = 0
        self.accion = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velxs = 0
        self.velx = 0
        self.vely = 0
        self.type = "rival4"
        self.vidas = 1
        self.damage = 4
        self.estado = 1 #1 activo, 2 explosion 3, inactivo

   def update(self):
       self.rect.x += self.f_velxs
       self.rect.y += self.f_velys
       if self.accion < 3:
           self.accion += 1
           if self.con < 3:
               self.con += 1
           else:
               self.con = 0
               self.accion = self.accion
           self.image = self.animacion[self.accion][self.con]
       else:
           self.accion = 0


   def morir(self):
       if self.vidas <= 0:
           self.estado = 2
