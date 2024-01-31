import sys

import pygame

class AlienInvasion:
    """General class for managing the game resources and behaviour."""
    def __init__(self):
        """Initialize the game and create de resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Initialize the game main loop."""
        while True:
            # Search key and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    # Make visible the last painting screen
    pygame.display.flip()
