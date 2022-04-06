import pygame as pg
from gameManager import GameManager

class NPC(pg.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)

        self.image = pg.Surface((64,64))
        self.rect = self.image.get_rect(topleft = (x*64, y*64))
        self.hitbox = self.rect