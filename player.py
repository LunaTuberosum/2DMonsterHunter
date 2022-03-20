import pygame as pg
from entity import Entity

class Player(Entity):
    def __init__(self, groups, imageRepo, x, y):
        super().__init__(groups, imageRepo, x, y)

        self.direction = pg.math.Vector2()
        self.speed = 2

        self.running = False
        
        self.runningSpeed = self.speed*2

    def update(self):
        self.input()

        if self.running == True:
            self.rect.x += self.direction.x * self.runningSpeed
            self.rect.y += self.direction.y * self.runningSpeed
        else:
            self.rect.x += self.direction.x * self.speed
            self.rect.y += self.direction.y * self.speed

    def input(self):
        self.direction = pg.math.Vector2()
        keys = pg.key.get_pressed()

        if keys[pg.K_LSHIFT]:
            self.running = True
        else:
            self.running = False
        
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
            