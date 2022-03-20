## This is going to be hard

import pygame as pg
import sys

from player import Player
from npc import NPC

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((1280,720))
        pg.display.set_caption('2D Monster Hunter')
        pg.init()
        self.clock = pg.time.Clock()

        self.sprites = CameraGroup()

        self.player = Player(self.sprites, 'Player', 0,0)
        NPC(self.sprites, 'Player', 4, 5)
        NPC(self.sprites, 'Player', 2, 1)
        NPC(self.sprites, 'Player', 7, 6)
        
    def main(self):
        while True:
            for event in pg.event.get():
    
                if event.type == pg.QUIT:
                    pg.QUIT
                    sys.exit()

            self.screen.fill('#9edb64')

            self.sprites.custom_draw(self.player)
            self.sprites.update()
            
            pg.display.update()
            self.clock.tick(60)

class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.placement):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

if __name__ == '__main__':
    game = Game()
    game.main()