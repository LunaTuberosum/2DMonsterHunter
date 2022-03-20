import pygame as pg

from imageRepos import humanSprites

class Entity(pg.sprite.Sprite):
    def __init__(self, groups, imageRepo, x, y):
        super().__init__(groups)

        self.idleDown = pg.image.load(humanSprites[imageRepo]['Down']).convert_alpha()
        self.idleLeft = pg.image.load(humanSprites[imageRepo]['Left']).convert_alpha()
        self.idleRight = pg.image.load(humanSprites[imageRepo]['Right']).convert_alpha()
        self.idleUp = pg.image.load(humanSprites[imageRepo]['Up']).convert_alpha()

        self.image = self.idleDown
    
        self.direction = pg.math.Vector2()

        self.rect = self.image.get_rect(topleft = (x*32, y*32))
        self.hitbox = self.rect.inflate(-28, -20)
        self.interactionHitbox = pg.Rect(self.rect.x, self.rect.y, 32, 32)

    def update(self):
        self.interactionHitboxPlacement()

    def interactionHitboxPlacement(self):
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