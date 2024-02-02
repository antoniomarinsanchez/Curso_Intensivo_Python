import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represent an alien in a fleet"""

    def __init__(self, ai_game):
        """Initialize an alien and its position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the image of the alien
        self.image = pygame.image.load('images/Alien_alienInvasion.png')
        self.rect = self.image.get_rect()

        # Starts an alien close to up-left position on screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save x-location as a float
        self.x = float(self.rect.x)
