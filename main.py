import pygame, sys
from Settings import *
from Debug import *
from World import World

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Dead by Sunrise')
        self.clock = pygame.time.Clock()

        self.world = World()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black') # Fills background with the colour 'black'
            self.world.run() # Creates the world
            pygame.display.update() # Continously updates screen
            self.clock.tick(fps) # Controls frame rate

if __name__ == '__main__':
    game = Game()
    game.run()