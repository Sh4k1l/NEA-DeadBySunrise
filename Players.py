import pygame
from Settings import *
from Obstacle import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprite):
        super().__init__(groups)
        self.image = pygame.image.load(r'C:\Users\shaka\source\repos\NEA-DeadBySunrise\player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #Vector, x:0 y:0 
        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprite = obstacle_sprite

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1 
        else:
           self.direction.x = 0
        
        if keys[pygame.K_UP]:
            self.direction.y = -1 
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1 
        else:
            self.direction.y = 0


    def move(self, speed):
        # when travelling diagonally, speed is much faster then normal. 
        # checking if vector has length
        if self.direction.magnitude() != 0:
            # when it does have a length, vector = 1
            self.direction = self.direction.normalize()
            # doesn't matter which direction travelled

        self.rect.x += self.direction.x * speed
        #self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        #self.collision('vertical')
        self.rect.center += self.direction * speed # results in same speed in all directions 

    def update(self):
        self.input()
        self.move(self.speed)


class Killer(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(r'C:\Users\shaka\source\repos\NEA-DeadBySunrise\tile000.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

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

    def move(self, speed):
        self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)


