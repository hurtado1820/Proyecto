import pygame
from enemigo import *
from const import *
import random

#el jefe 1 es un generador, por eso está en este archivo :p
class Jefe1(Enemigo):
    def __init__ (self,pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.x = pos[0]
        self.rect.y = pos[1]
        self.type = "jefe1"
        self.velx = 0
        self.f_velxs = 0
        self.f_velys = 0
        self.vidas = 6
        self.damage = 1
        self.estado = 1 # 1 estándar, 2 muerto
        self.temp = random.randrange(100)
        self.stop = None

    def update(self):
        self.rebotar()
        self.temp -= 1
        self.rect.x += self.velx
        self.rect.y += self.f_velys
        self.rect.x += self.f_velxs
        self.camino()
        if self.con < 3:
            self.con += 1
        else:
            self.con = 0
            self.accion = self.accion
        self.image = self.animacion[self.accion][self.con]

    def morir(self):
        if self.vidas <= 0:
            self.estado = 2

    def rebotar(self):
        ls_col = pygame.sprite.spritecollide(self,self.stop,False)
        if ls_col:
            self.velx *= -1

    def camino(self):
        if self.velx != 0:
            if self.velx < 0:
                self.accion = 0
            else:
                self.accion = 1

    def RetPos(self):
        x = (self.rect.x) + 10
        y = self.rect.y + 20
        return [x,y]

    def mover(self):
        self.velx = 7
        self.estado = 1

#el enemigo2 también es un generador
class Enemigo2(Enemigo):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("genera.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0
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
       self.rect.y += self.f_velys

   def morir(self):
       if self.vidas <= 0:
           self.estado = 2

#los objetos que caerán en el enfrentamiento con el jefe2 son generados por este objeto
class Generador(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("nada.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0
        self.velx = 0
        self.vely = 0
        self.type = "rival2"
        self.estado = 1 # 1 activo, 2 apagado
        self.temp = random.randrange(100)

   def update(self):
       self.temp -= 1
       self.rect.x += self.f_velxs
       self.rect.y += self.f_velys

class Explode(pygame.sprite.Sprite):
    def __init__ (self,pos,m):#m
        pygame.sprite.Sprite.__init__(self)
        self.accion = 0
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0
        self.estado = 1

    def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys
        if self.accion < 1:
            self.accion += 1
            if self.con < 3:
                self.con += 1
            else:
                self.con = 0
                self.accion = self.accion
            self.image = self.animacion[self.accion][self.con]
        else:
            self.estado = 2

#misiles del enemigo2
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
        self.f_velys = 0

    def update(self):
        self.rect.x = self.rect.x + self.velx
        self.rect.y = self.rect.y + self.vely
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys

#balas del jugador
class Bala(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("laser.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0
        self.velx = 0
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
        self.rect.x = self.rect.x + self.velx
        self.rect.y = self.rect.y + self.vely
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys

#el jefe 2 lanza ondas que "aturden" al jugador
class Proyectil(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("proyectil.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0
        self.velx = 0
        self.vely = 0
        self.damage = 2

    def update(self):
        self.rect.x = self.rect.x + self.velx
        self.rect.y = self.rect.y + self.vely
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys

#objetos que caen durante el enfrentamiento del jefe2
class Piedra(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("piedra.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0
        self.f_velxs = 0
        self.f_velys = 0
        self.damage = 1

    def update(self):
        self.rect.y = self.rect.y + self.vely
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys

#Objeto monumento
class Monumento(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Monument.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys

class Gem1(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gem1.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys

class Gem2(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("gem2.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys

class Stop(pygame.sprite.Sprite):
    def __init__ (self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("nada.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0

    def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys
