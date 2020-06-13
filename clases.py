import pygame
from enemigo import *
from const import *
import random

#el jefe 2 es un generador, que no sirve D:
class Jefe2(Enemigo):
    def __init__ (self,pos):#m
        pygame.sprite.Sprite.__init__(self)
        '''self.accion = 1
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]'''
        self.image = pygame.Surface([70,70])
        self.image.fill(MORADO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "jefe2"
        self.velx = 0
        self.vely = 0
        self.f_velxs = 0
        self.vidas = 10
        self.damage = 1
        self.estado = 1 # 1 estándar, 2 muerto
        self.temp = random.randrange(100)

    def update(self):
       self.temp -= 1
       self.rect.x += self.f_velxs

    def morir(self):
        if self.vidas <= 0:
            self.estado = 2

#el enemigo2 es un generador, por esto no tiene su propio archivo
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

#los objetos que caerán en el enfrentamiento con el jefe2 son generados por este objeto
class Generador(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40,40])
        self.image.fill(VERDOSC)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.velx = 0
        self.vely = 0
        self.type = "rival2"
        self.estado = 1 # 1 activo, 2 apagado
        self.temp = random.randrange(100)

   def update(self):
       self.temp -= 1
       self.rect.x += self.f_velxs

#misiles del enemigo estático 2

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

#balas del jugador

class Bala(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0
        self.velx = 0

    def update(self):
        self.rect.x = self.rect.x + self.velx
        self.rect.y = self.rect.y + self.vely

#el jefe 2 lanza ondas que "aturden" al jugador
class Onda(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,70])
        self.image.fill(GRIS)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.damage = 1

    def update(self):
        self.rect.x = self.rect.x + self.velx

#objetos que caen durante el enfrentamiento del jefe2
class Piedra(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10])
        self.image.fill(CELESTE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0
        self.damage = 1

    def update(self):
        self.rect.y = self.rect.y + self.vely

#plataformas
class Plataforma(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200,80])
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
