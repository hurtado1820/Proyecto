import pygame
from const import *

class Jugador(pygame.sprite.Sprite):
    def __init__ (self,pos):#m
        pygame.sprite.Sprite.__init__(self)
        '''self.accion = 1
        self.con = 0
        self.animacion = m
        self.image = self.animacion[self.accion][self.con]'''
        self.image = pygame.Surface([20,40])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        #self.lim = [7,7,2,2,7,7,2,2]
        self.dir = 1 #1: derecha, 2:izquierda
        self.velx = 0
        self.vely = 0
        self.vidas = 20
        self.aturdido = 0
        self.arma = 0
        self.estado = 1  # 1 estándar, 2 velocidad, 3 con las gemas, 4 aturdido, 5 muerto
        self.muros = None
        self.suelos = None
        self.plataformas = None
        self.piso = False #Bandera, gravedad
        self.inventario = [0,0,0,0] #gemas, vidas, velocidad, tiempo

    '''def animar(self):
        if self.velx != self.vely:
            if self.con < self.lim[self.accion]:
                self.con += 1
            else:
                self.con = 0
                self.accion = self.accion
            self.image = self.animacion[self.accion][self.con]'''

    def gravedad(self):
        if self.vely ==  0:
            self.vely = 0.5
        else:
            self.vely += 0.5

    def update(self):
        #Colision en x
        self.rect.x += self.velx
        ls_col_p = pygame.sprite.spritecollide(self,self.plataformas,False)
        ls_col_s = pygame.sprite.spritecollide(self,self.suelos,False)
        ls_col_m = pygame.sprite.spritecollide(self,self.muros,False)
        #Colision con plataformas
        for b in ls_col_p:
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    self.velx = 0
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    self.velx = 0

        #Colision con suelo
        for m in ls_col_s:
            if self.velx > 0:
                if self.rect.right > m.rect.left:
                    self.rect.right = m.rect.left
                    self.velx = 0
            else:
                if self.rect.left < m.rect.right:
                    self.rect.left = m.rect.right
                    self.velx = 0

        #Colision con muro
        for p in ls_col_m:
            if self.velx > 0:
                if self.rect.right > p.rect.left:
                    self.rect.right = p.rect.left
                    self.velx = 0
            else:
                if self.rect.left < p.rect.right:
                    self.rect.left = p.rect.right
                    self.velx = 0

        #Colision en y
        self.rect.y += self.vely
        ls_col_p = pygame.sprite.spritecollide(self,self.plataformas,False)
        ls_col_s = pygame.sprite.spritecollide(self,self.suelos,False)
        ls_col_m = pygame.sprite.spritecollide(self,self.muros,False)
        #Colision con plataformas
        for bp in ls_col_p:
            if self.vely > 0:
                if self.rect.bottom > bp.rect.top:
                    self.rect.bottom = bp.rect.top
                    self.vely = 0
                    self.piso = True
            '''else:
                if self.rect.top < bp.rect.bottom:
                    self.rect.top = bp.rect.bottom
                    self.vely = 0'''

        #Colision con suelo
        for m in ls_col_s:
            if self.vely > 0:
                if self.rect.bottom >= m.rect.top:
                    self.rect.bottom = m.rect.top
                    self.vely = 0

        #Colision con muro
        for f in ls_col_m:
            if self.vely > 0:
                if self.rect.bottom > f.rect.top:
                    self.rect.bottom = f.rect.top
                    self.vely = 0
            else:
                if self.rect.top < f.rect.bottom:
                    self.rect.top = f.rect.bottom
                    self.vely = 0

        #Caida en el aire
        if not self.piso:
            self.gravedad()
        #Contacto con el piso
        '''if self.rect.bottom > ALTO:
            self.vely = 0
            self.rect.bottom = ALTO
            self.piso = True'''

        #self.animar()

    def RetPos(self):
        x = self.rect.x
        y = self.rect.y + 5
        return [x,y]

    def detener(self):
        self.velx=0
        self.vely=0
        self.estado = 1


    def aturdir(self):
        if self.aturdido == 1:
            self.estado = 4

    #cuando recoge el buff activa el estado de velocidad
    def mayo_rakuin(self):
         if self.inventario[2] > 0:
             self.aturdido = 0
             self.estado = 2
             self.inventario[2] -= 1

    #cuando tiene ambos objetos pasa al estado 5 (en el que puede ganar?)
    def gemas(self):
        if self.inventario[0] == 2:
            self.estado = 3

    # Muerte ; cuando las vidas llegan a 0
    def morir(self):
         if self.vidas <= 0:
            self.detener()
            self.estado = 5
