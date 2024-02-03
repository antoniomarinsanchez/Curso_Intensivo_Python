import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represent an alien in a fleet"""

    def __init__(self, ai_game):
        """Initialize an alien and its position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the image of the alien
        self.image = pygame.image.load('images/Alien_alienInvasion.bmp')
        self.rect = self.image.get_rect()

        # Starts an alien close to up-left position on screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save x-location as a float
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true if the alien is touching the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the left or right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
