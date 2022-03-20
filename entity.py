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

        self.rect = self.image.get_rect(topleft = (x*32, y*32))