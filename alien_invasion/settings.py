class Settings:
    """Class for the settings of the game"""

    def __init__(self):
        """Initialize the settings"""
        # Game settings
        self.game_delay = 0
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        # fleet direction 1 to right, -1 to left
        self.fleet_direction = 1

