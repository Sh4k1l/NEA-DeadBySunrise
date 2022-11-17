import pygame
from Settings import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(r'C:\Users\shaka\source\repos\NEA-DeadBySunrise\rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
