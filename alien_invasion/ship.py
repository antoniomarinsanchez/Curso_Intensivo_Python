import pygame

class Ship:
    """Class for managing the ship"""
    def __init__(self, ai_game):
        """Initialize and configure the ship"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image of the ship and get its rect
        self.image = pygame.image.load('images/NaveEspacial_alienInvasion.bmp')
        self.rect = self.image.get_rect()

        # Put the ship in the center at the begining
        self.rect.midbottom = self.screen_rect.midbottom

        # Float X-position of the ship
        self.x = float(self.rect.x)

        # Moving flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the location of the ship depends on the moving flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect.x
        self.rect.x = self.x

    def blitme(self):
        """Paint the ship in its location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship to the start position"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
