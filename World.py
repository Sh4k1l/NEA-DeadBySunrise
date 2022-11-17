import pygame
from Settings import *
from Obstacle import *
from Players import *
from Debug import *

class World:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.visable_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_world()

    def create_world(self):
        for row_index, row in enumerate(world_map):
            for col_index, col in enumerate(row):
                x = col_index * tilesize
                y = row_index * tilesize
                if col == 'x':
                    Obstacle((x, y), [self.visable_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.Player = Player((x, y), [self.visable_sprites], [self.obstacle_sprites])     
                if col == 'k':
                    self.Killer = Killer((x,y), [self.visable_sprites])

    def run(self):
        self.visable_sprites.draw(self.display_surface)
        self.visable_sprites.update()
        debug1(self.Player.direction)       
        debug2(self.Killer.direction)