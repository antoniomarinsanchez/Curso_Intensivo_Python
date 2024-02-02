
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for managing the bullets of the ship"""

    def __init__(self, ai_game):
        """Create an object of the bullet in the ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create the rect of the bullet in (0, 0), position depends on the ship
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Save the bullet position in a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up"""
        # Update the float position
        self.y -= self.settings.bullet_speed
        # Update position in rect.y
        self.rect.y = self.y

    def draw_bullet(self):
        """Paint the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
