## This is going to be hard

import pygame as pg
import sys

from player import Player
from npc import NPC
from gameManager import GameManager

class MainLoop():
    
    def __init__(self):
        self.screen = pg.display.set_mode((1280,720))
        pg.display.set_caption('2D Monster Hunter')
        pg.init()
        self.clock = pg.time.Clock()

        GameManager.obstacleSprites = YSortCameraGroup()
        GameManager.npcSprites = pg.sprite.Group()
        GameManager.folliageSprties = pg.sprite.Group()
        self.player = Player([GameManager.obstacleSprites], 0,0)
        NPC(GameManager.obstacleSprites, 3, 3)
        
        
    def main(self):
        while True:
            for event in pg.event.get():
    
                if event.type == pg.QUIT:
                    pg.QUIT
                    sys.exit()

            self.screen.fill('#9edb64')

            GameManager.obstacleSprites.custom_draw(self.player)
            GameManager.obstacleSprites.update()
            
            pg.display.update()
            self.clock.tick(60)

class YSortCameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()

    def custom_draw(self, player):

        

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.y):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

            pg.draw.rect(pg.display.get_surface(), 'red', sprite.hitbox, 2)
            # pg.draw.rect(pg.display.get_surface(), 'blue', sprite.interactionHitbox, 2)
            self.display_surface.blit(sprite.image, sprite.rect)


if __name__ == '__main__':
    mainLoop = MainLoop()
    mainLoop.main()