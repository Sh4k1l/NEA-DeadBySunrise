import pygame
from Settings import *
from Obstacle import *
from Players import *
from Debug import *

class World:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.game_paused = False

        # Sprite group setup
        self.visable_sprites = YSortCameraGroup() # Sprites that will be drawn on the screen
        self.obstacle_sprites = pygame.sprite.Group() # Will be able to collide with the player

        self.create_world()

    # Goes through world map in Settings.py
    def create_world(self):
        for row_index, row in enumerate(world_map): # Index of y 
            for col_index, col in enumerate(row): # Index of x
                x = col_index * tilesize
                y = row_index * tilesize
                if col == 'x':
                    Obstacle((x, y), [self.visable_sprites, self.obstacle_sprites]) # Obstacles will be in both groups of sprites
                    # Can check the obstacle sprites and player to see if collisions have occured
                    # If there is any collision player will be affected
                if col == 's':
                    self.Survivor = Survivor((x, y), [self.visable_sprites], [self.obstacle_sprites])     
                if col == 'k': 
                    self.Killer = Killer((x, y,) , [self.visable_sprites], [self.obstacle_sprites])
            # Loops through list finding any values of 'x', 's' or 'k' and creates instances of them
    def toggle_Menu(self):
        self.game_paused = not self.game_paused          


    def run(self): # Upades and draws the game
        self.visable_sprites.custom_draw(self.Survivor)
        if self.game_paused:
            pass         
        else:       
            self.visable_sprites.update()
        
        debug1(self.Survivor.direction)
      

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.halfWidth = width / 2 
        self.halfHeight = height / 2
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2() 


    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.halfWidth
        self.offset.y = player.rect.centery - self.halfHeight

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
