import pygame

class Suelo(pygame.sprite.Sprite):
   def __init__(self,pos,num):
        pygame.sprite.Sprite.__init__(self)
        if num == 1:
            self.image = pygame.image.load("resources/1.png")
        if num == 2:
            self.image = pygame.image.load("resources/2.png")
        if num == 3:
            self.image = pygame.image.load("resources/3.png")
        if num == 13:
            self.image = pygame.image.load("resources/d.png")
        if num == 14:
            self.image = pygame.image.load("resources/e.png")
        if num == 15:
            self.image = pygame.image.load("resources/f.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0

   def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys

class Plataforma(pygame.sprite.Sprite):
   def __init__(self,pos,num):
        pygame.sprite.Sprite.__init__(self)
        if num == 4:
            self.image = pygame.image.load("resources/4.png")
        if num == 5:
            self.image = pygame.image.load("resources/5.png")
        if num == 6:
            self.image = pygame.image.load("resources/6.png")
        if num == 16:
            self.image = pygame.image.load("resources/g.png")
        if num == 17:
            self.image = pygame.image.load("resources/h.png")
        if num == 18:
            self.image = pygame.image.load("resources/i.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0

   def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys


class Muro(pygame.sprite.Sprite):
   def __init__(self,pos,num):
        pygame.sprite.Sprite.__init__(self)
        if num == 7:
            self.image = pygame.image.load("resources/7.png")
        if num == 8:
            self.image = pygame.image.load("resources/8.png")
        if num == 9:
            self.image = pygame.image.load("resources/9.png")
        if num == 11:
            self.image = pygame.image.load("resources/b.png")
        if num == 12:
            self.image = pygame.image.load("resources/c.png")
        if num == 19:
            self.image = pygame.image.load("resources/j.png")
        if num == 20:
            self.image = pygame.image.load("resources/k.png")
        if num == 21:
            self.image = pygame.image.load("resources/l.png")
        if num == 24:
            self.image = pygame.image.load("resources/o.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0

   def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys


class Pincho(pygame.sprite.Sprite):
   def __init__(self,pos,num):
        pygame.sprite.Sprite.__init__(self)
        if num == 26:
            self.image = pygame.image.load("resources/q.png")
        if num == 27:
            self.image = pygame.image.load("resources/r.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.damage = 1
        self.f_velxs = 0
        self.f_velys = 0

   def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys


class Puente(pygame.sprite.Sprite):
   def __init__(self,pos,num):
        pygame.sprite.Sprite.__init__(self)
        if num == 29:
            self.image = pygame.image.load("resources/t.png")
        if num == 30:
            self.image = pygame.image.load("resources/u.png")
        if num == 31:
            self.image = pygame.image.load("resources/v.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0

   def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys

class Lava(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resources/y.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.damage = 1
        self.f_velxs = 0
        self.f_velys = 0

   def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys


class Vacio(pygame.sprite.Sprite):
   def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("resources/z.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.f_velxs = 0
        self.f_velys = 0

   def update(self):
        self.rect.x += self.f_velxs
        self.rect.y += self.f_velys
