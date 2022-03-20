import pygame as pg
from entity import Entity

class NPC(Entity):
    def __init__(self, groups, imageRepo, x, y):
        super().__init__(groups, imageRepo, x, y)