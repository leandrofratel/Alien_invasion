class GameStats():
    """Armazena dados estatísticos do jogo."""

    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_acrtive = True

    def reset_stats(self):
        """Dados estatísticos que podem mudar ao decorrer do jogo."""
        self.ships_left = self.ai_settings.ship_limit