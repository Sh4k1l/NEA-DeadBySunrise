import pygame
from Settings import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, group): # Pos = position, Groups = Sprite group obstacles will be part of
        super().__init__(group)
        self.image = pygame.image.load(r'C:\Users\shaka\source\repos\NEA-DeadBySunrise\rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        #C:\Users\shaka\source\repos\NEA-DeadBySunrise\rock.png
        #C:\Users\shaka\source\repos\NEA-DeadBySunrise\sprites\objects
        #C:\Users\shaka\source\repos\NEA-DeadBySunrise\objects.png