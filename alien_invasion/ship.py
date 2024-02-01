import pygame

class Ship:
    """Class for managing the ship"""
    def __init__(self, ai_game):
        """Initialize and configure the ship"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image of the ship and get its rect
        self.image = pygame.image.load('images/NaveEspacial_alienInvasion.png')
        self.rect = self.image.get_rect()

        # Put the ship in the center at the begining
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Paint the ship in its location"""
        self.screen.blit(self.image, self.rect)