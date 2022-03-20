import pygame as pg
from entity import Entity

class Player(Entity):
    def __init__(self, groups, imageRepo, x, y, npcs):
        super().__init__(groups, imageRepo, x, y)

        self.speed = 3

        self.npcs = npcs

        self.running = False
        
        self.iFrame = False
        self.runningSpeed = self.speed*1.5
        self.prevTick = pg.time.get_ticks()
        self.rollingTimer = 400
        self.roll = False
        self.rollCount = 0

        self.weapon = Weapon(groups, self, 'Greatswords/Bone/OnBack')

        if self.image == self.idleDown:
            self.interactionHitbox.x = self.rect.x + 16
            self.interactionHitbox.top = self.rect.bottom
        elif self.image == self.idleUp:
            self.interactionHitbox.x = self.rect.x + 16
            self.interactionHitbox.bottom = self.rect.top
        elif self.image == self.idleRight:
            self.interactionHitbox.left = self.rect.right
            self.interactionHitbox.y = self.rect.y + 16
        elif self.image == self.idleLeft:
            self.interactionHitbox.right = self.rect.left
            self.interactionHitbox.y = self.rect.y + 16

    def update(self):
        super().update()
        
        self.weapon.rect.x = self.rect.x + 6
        if self.image == self.idleDown:
            self.weapon.rect.y = self.rect.y - 1 
        if self.image == self.idleUp:
            self.weapon.rect.y = self.rect.y + 1 

        self.input()

        if self.roll == True:
            self.hitbox.x += (self.direction.x * 10.6)
            self.collision('horizontal')
            self.hitbox.y += (self.direction.y * 10.6)
            self.collision('vertical')

            self.rollCount += 1
            if self.rollCount == 8:
                self.roll = False
                self.iFrame = False

            elif self.rollCount >= 3 and self.rollCount <= 5:
                self.iFrame = True

            else:
                self.iFrame = False

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

        if keys[pg.K_f]:
            for npc in self.npcs:
                if self.interactionHitbox.colliderect(npc.hitbox):
                    npc.talk()

        if keys[pg.K_LSHIFT]:
            self.running = True
        else:
            self.running = False

        if (keys[pg.K_LCTRL] and pg.time.get_ticks() - self.prevTick >= self.rollingTimer):
            self.prevTick = pg.time.get_ticks()
            self.roll = True
            self.rollCount = 0

    def collision(self, direction):                        
        
        if direction == "horizontal":
            for npc in self.npcs:
                if npc.hitbox.colliderect(self.hitbox) and npc != self:

                        
                    if self.direction.x > 0:
                        self.hitbox.right = npc.hitbox.left
                        
                    if self.direction.x < 0:
                        self.hitbox.left = npc.hitbox.right
                        
                        

        if direction == "vertical":
            for npc in self.npcs:
                if npc.hitbox.colliderect(self.hitbox) and npc != self:

                    if self.direction.y > 0:
                        self.hitbox.bottom = npc.hitbox.top
                        
                    if self.direction.y < 0:
                        self.hitbox.top = npc.hitbox.bottom


class Weapon(pg.sprite.Sprite):
    def __init__(self, groups, player, weapon):
        super().__init__(groups)
        
        self.weapon = weapon
        self.player = player

        self.image = pg.image.load(f'Assets/Weapons/{weapon}.png')
        self.rect = self.image.get_rect(topleft = (self.player.rect.topleft))
        self.interactionHitbox = self.rect