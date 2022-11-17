import pygame
from Settings import *
from Obstacle import *

class Survivor(pygame.sprite.Sprite): # Inherits from sprite group
    def __init__(self, pos, group, obstacle_sprite):
        super().__init__(group)
        self.image = pygame.image.load(r'C:\Users\shaka\source\repos\NEA-DeadBySunrise\New Piskel-20221117-191638.piskel').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #Vector, x:0 y:0 
        self.direction = pygame.math.Vector2()
        self.speed = 3 # Survivor moves 3 pixels per frame

        self.obstacle_sprite = obstacle_sprite

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1 
        else:
           self.direction.x = 0
           
        if keys[pygame.K_w]:
            self.direction.y = -1 
        elif keys[pygame.K_s]:
            self.direction.y = 1 
        else:
            self.direction.y = 0

    #def collision(self, direction):
    #    if direction == 'horizontal':
    #        for sprite in self.obstacle_sprite: # Checks all sprites in obstacle sprites group
    #            if sprite.rect.colliderect(self.rect): # Checks rectangle of sprite with rectangle of player
    #                if self.direction.x > 0: # Move right
    #                    self.rect.right = self.rect.left
    #                if self.direction.x < 0: # Move left
    #                    self.rect.left = self.rect.right

    #    if direction == 'vertical':
    #        for sprite in self.obstacle_sprite:
    #            if sprite.rect.colliderect(self.rect):
    #                if self.direction.y > 0: # Move down
    #                    self.rect.bottom = self.rect.top
    #                if self.direction.y < 0: # Move up
    #                    self.rect.top = self.rect.bottom

    def move(self, speed):
        # When travelling diagonally, speed is much faster then normal. 
        # Checking if vector has length
        if self.direction.magnitude() != 0:
            # When it does have a length, vector = 1
            self.direction = self.direction.normalize()
            # Doesn't matter which direction travelled

        self.rect.x += self.direction.x * speed
        #self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        #self.collision('vertical')
        self.rect.center += self.direction * speed # Results in same speed in all directions 

    def update(self):
        self.input()
        self.move(self.speed)


class Killer(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacle_sprite):
        super().__init__(group)
        self.image = pygame.image.load(r'C:\Users\shaka\source\repos\NEA-DeadBySunrise\player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprite = obstacle_sprite

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1 
        else:
           self.direction.x = 0
        
        if keys[pygame.K_w]:
            self.direction.y = -1 
        elif keys[pygame.K_s]:
            self.direction.y = 1 
        else:
            self.direction.y = 0

    #def collision(self, direction):
    #    if direction == 'horizontal':
    #        for sprite in self.obstacle_sprite:
    #            if sprite.rect.colliderect(self.rect):
    #                if self.direction.x > 0:
    #                    self.rect.right = self.rect.left
    #                if self.direction.x < 0:
    #                    self.rect.left = self.rect.right

    #    if direction == 'vertical':
    #        for sprite in self.obstacle_sprite:
    #            if sprite.rect.colliderect(self.rect):
    #                if self.direction.y > 0:
    #                    self.rect.bottom = self.rect.top
    #                if self.direction.y < 0:
    #                    self.rect.top = self.rect.bottom

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.rect.x += self.direction.x * speed
        #self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        #self.collision('vertical')
        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)
