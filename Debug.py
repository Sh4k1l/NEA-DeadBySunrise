import pygame
from Players import *

pygame.init()
font = pygame.font.Font(None, 30)

class debug:
    def __init__(self, x, y):
        self.x = x 
        self.y = y     

    def debugging(self, info):
        self.display_surface = pygame.display.get_surface()
        self.debug_surf = font.render(str(info), True, 'White')
        self.debug_rect = self.debug_surf.get_rect(topleft = (self.x, self.y))
        pygame.draw.rect(self.display_surface, 'black', self.debug_rect)
        self.display_surface.blit(self.debug_surf, self.debug_rect)



def debug1 (info, x = 10, y = 10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, 'black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)

def debug2 (info, x = 10, y = 40):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface, 'black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)

# Helps with speed and direction
# Used for normalisation of player speed when moving diagonally
# Doesn't affect the game