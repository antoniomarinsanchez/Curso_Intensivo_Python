class GameStats:
    """Manage the stats of the game"""

    def __init__(self, ai_game):
        """Initialize the statistics"""
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize the stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
