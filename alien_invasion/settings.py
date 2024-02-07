class Settings:
    """Class for the settings of the game"""

    def __init__(self):
        """Initialize the static settings"""
        # Game settings
        self.game_delay = 0
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 5

        # Change of the game speed between levels
        self.speedup_scale = 1.1

        # Change the score of the aliens between levels
        self.score_scale = 1.5

        # Initialize dynamic settings in each game
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the dynamic settings"""
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1.0

        # Score
        self.alien_points = 50

        # fleet direction 1 to right, -1 to left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the speed and score settings"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


