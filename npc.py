from email.headerregistry import SingleAddressHeader
from dialogDatabase import dialog
import pygame as pg
from entity import Entity

class NPC(Entity):
    def __init__(self, groups, imageRepo, x, y, npcID):
        super().__init__(groups, imageRepo, x, y)

        self.npcID = npcID

    def talk(self):
        for dialogText in dialog[self.npcID]:
            print(dialogText)
            input('>')

        