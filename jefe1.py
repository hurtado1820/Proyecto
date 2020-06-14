import pygame
import random
from const import *
from enemigo import *

class Jefe1(Enemigo):
    def __init__ (self,pos):#m
        pygame.sprite.Sprite.__init__(self)
        '''self.accion = 1
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]'''
        self.image = pygame.Surface([70,70])
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = "jefe1"
        self.velx = 0
        self.vely = 0
        self.f_velxs = 0
        self.f_velys = 0
        self.radius = 60
        self.x = pos[0]
        self.vidas = 5
        self.damage = 2
        self.estado = 1 # 1 estándar, 2 rondando, 3 muerto
        self.pared = None
        self.piso = False

    '''def gravedad(self):
        if self.vely ==  0:
            self.vely = 0.5
        else:
            self.vely += 0.5'''

    def RetPos(self):
        x = self.rect.x + 20
        y = self.rect.bottom
        return [x,y]

    def detener(self):
        self.velx=0
        self.vely=0
        self.estado=1

    def morir(self):
        if self.vidas <= 0:
            self.detener()
            self.estado = 3

    '''def camino(self):
        if self.velx != 0:
            if self.velx < 0:
                self.accion = 1
            else:
                self.accion = 0
        else:
            self.accion = 2'''

    '''def saltar(self):
        if self.rect.x > self.x + 60 or self.rect.x < self.x -60:
            self.vely = random.randint(-4,0)
        else:
             self.gravedad()'''

    def update(self):
        #Colision en x
        #self.saltar()
        if self.rect.x > self.x + 75:
            self.velx = -1
        elif self.rect.x < self.x -75:
            self.velx = 1
        self.rect.x += self.velx
        self.rect.x += self.f_velxs
        ls_col = pygame.sprite.spritecollide(self,self.piso,False)
        ls_col_m = pygame.sprite.spritecollide(self,self.pared,False)
        '''for b in ls_col:
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    self.velx = 0
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    self.velx = 0'''

        for mi in ls_col_m:
            if self.velx < 0:
                if self.rect.left < mi.rect.right:
                    self.rect.left = mi.rect.right
                    self.velx = 0

        #Colision en y
        self.rect.y += self.vely
        self.rect.y += self.f_velys
        ls_col = pygame.sprite.spritecollide(self,self.piso,False)
        for b in ls_col:
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.vely = 0
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.vely = 0
        #Caida en el aire
        '''if not self.piso:
            self.gravedad()'''
        #Contacto con el piso
        '''if self.rect.bottom > ALTO:
            self.vely = 0
            self.rect.bottom = ALTO
            self.piso = True'''

        #self.camino()
        '''if self.con < 5:
            self.con += 1
        else:
            self.con = 0
            self.accion = self.accion
        self.image = self.animacion[self.accion][self.con]'''

    def mover(self):
        self.velx = 2
        self.vely = -3
        #self.gravedad()
        self.estado = 2

    #si llega hasta alguno de los bordes cambiará la dirección en la que iba hacia el lado contrario
    '''def rebotar(self):
        self.rect.x += self.velx
        ls_col = pygame.sprite.spritecollide(self,self.bloques,False)
        ls_col2 = pygame.sprite.spritecollide(self,self.pared,False)
        if ls_col:
            self.velx *= -1

        if ls_col2:
            self.velx *= -1'''
