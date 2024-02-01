
import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """General class for managing the game resources and behaviour."""
    def __init__(self):
        """Initialize the game and create de resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Configure the background color
        self.bg_color = self.settings.bg_color

        # Create a ship
        self.ship = Ship(self)

    def run_game(self):
        """Initialize the game main loop."""
        while True:
            # Search key and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Paint the screen in each step
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            # Make visible the last painting screen
            pygame.display.flip()


if __name__ == '__main__':
    # Do an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()
