class GameStats():
    """Armazena dados estatísticos do jogo."""

    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

        # Inicia o jogo em um estado inativo.
        self.game_active = False

    def reset_stats(self):
        """Dados estatísticos que podem mudar ao decorrer do jogo."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0