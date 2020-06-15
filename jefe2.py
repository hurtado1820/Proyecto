import pygame
import random
from const import *
from enemigo import *

class Jefe2(Enemigo):
    def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion = 1
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "jefe2"
        self.velx = 0
        self.x = pos[0]
        self.vely = 0
        self.f_velxs = 0
        self.f_velys = 0
        self.radius = 60
        self.x = pos[0]
        self.vidas = 8
        self.damage = 1
        self.estado = 1 # 1 estándar, 2 rondando, 3 muerto
        self.temp = random.randrange(100)

    def morir(self):
        if self.vidas <= 0:
            self.estado = 3

    def camino(self):
        if self.velx != 0:
            if self.velx < 0:
                self.accion = 1
            else:
                self.accion = 0

    def update(self):
        #Colision en x
        if self.rect.x > self.x + 200:
            self.velx = -3
        elif self.rect.x < self.x -200:
            self.velx = 3
        self.rect.x += self.velx
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys
        self.camino()
        if self.con < 3:
            self.con += 1
        else:
            self.con = 0
            self.accion = self.accion
        self.image = self.animacion[self.accion][self.con]

    def mover(self):
        self.velx = 3
        self.estado = 2
