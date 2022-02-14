from imports import *
class player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        vec = py.math.Vector2
        self.pos = vec((0,500))
        self.acc = vec((0,0))
        self.vel = vec((0,0))
        self.image = py.image.load("projectnuo\images\dick.png")
        self.rect = self.image.get_rect()
        self.speed = 2

    def movement(self):
        keys = py.key.get_pressed()
        self.vel.x = 0
        self.vel.y = 0
        if keys[K_w]: 
            self.pos.y -= self.speed
            self.vel.y = -1
        if keys[K_s]:
            self.pos.y += self.speed
            self.vel.y = 1
        if keys[K_d]:
            self.pos.x += self.speed
            self.vel.x = 1
        if keys[K_a]:
            self.pos.x -= self.speed
            self.vel.x = -1
        self.rect.midbottom = self.pos
        if self.pos.x <= 10:
            self.pos.x = 10
        if self.pos.x >= 490:
            self.pos.x = 490
        if self.pos.y <= 38:
            self.pos.y = 38
        if self.pos.y >= 500:
            self.pos.y = 500
    def direct(self):
        if self.vel.x > 0:
            self.image = py.image.load("projectnuo\images\dickr.png")
        if self.vel.x < 0:
            self.image = py.image.load("projectnuo\images\dickl.png")
        if self.vel.y > 0:
            self.image = py.image.load("projectnuo\images\dickd.png")
        if self.vel.y < 0:
            self.image = py.image.load("projectnuo\images\dick.png")
        
        if self.vel.x and self.vel.y > 0:
            self.image = py.image.load("projectnuo\images\dickdr.png")
        if self.vel.x and self.vel.y < 0:
            self.image = py.image.load("projectnuo\images\dickul.png")
        if self.vel.y > 0 and self.vel.x < 0:
            self.image = py.image.load("projectnuo\images\dickdl.png")
        if self.vel.y < 0 and self.vel.x > 0:
            self.image = py.image.load("projectnuo\images\dickur.png")

        

        
        