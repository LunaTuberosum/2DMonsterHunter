import pygame as pg
from entity import Entity

class Player(Entity):
    def __init__(self, groups, imageRepo, x, y, sprites):
        super().__init__(groups, imageRepo, x, y)

        self.direction = pg.math.Vector2()
        self.speed = 3

        self.hitbox = self.rect.inflate(-28, -20)

        self.sprites = sprites

        self.running = False
        
        self.runningSpeed = self.speed*1.5
        self.prevTick = pg.time.get_ticks()
        self.rollingTimer = 400
        self.roll = False

    def update(self):
        self.input()

        if self.roll == True:
            self.hitbox.x += (self.direction.x * 64)
            self.collision('horizontal')
            self.hitbox.y += (self.direction.y * 64)
            self.collision('vertical')
            self.roll = False
        elif self.running == True:
            self.hitbox.x += self.direction.x * self.runningSpeed
            self.collision('horizontal')
            self.hitbox.y += self.direction.y * self.runningSpeed
            self.collision('vertical')
        else:
            self.hitbox.x += self.direction.x * self.speed
            self.collision('horizontal')
            self.hitbox.y += self.direction.y * self.speed
            self.collision('vertical')

        self.rect.center = self.hitbox.center

    def input(self):
        self.direction = pg.math.Vector2()
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.direction.y = -1
            self.image = self.idleUp
        elif keys[pg.K_s]:
            self.direction.y = 1
            self.image = self.idleDown

        if keys[pg.K_a]:
            self.direction.x = -1
            self.image = self.idleLeft
        elif keys[pg.K_d]:
            self.direction.x = 1
            self.image = self.idleRight

        if keys[pg.K_LSHIFT]:
            self.running = True
        else:
            self.running = False

        if keys[pg.K_LCTRL] and pg.time.get_ticks() - self.prevTick >= self.rollingTimer:
            self.prevTick = pg.time.get_ticks()
            self.roll = True

    def collision(self, direction):                        
        
        if direction == "horizontal":
            for sprite in self.sprites:
                if sprite.hitbox.colliderect(self.hitbox) and sprite != self:

                        
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                        
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                        
                        

        if direction == "vertical":
            for sprite in self.sprites:
                if sprite.hitbox.colliderect(self.hitbox) and sprite != self:

                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                        
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom