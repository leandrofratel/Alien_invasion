class Settings():
    """Uma classe para armazenar todas as configurações do jogo."""

    def __init__(self):
        """Inicializa as configurações estáticas do jogo."""
        # Configurações da tela.
        self.screen_width = 800
        self.screen_height = 600

        # Configurações de cor da tela
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave.
        self.ship_limit = 3

        # Configurações dos alienígenas.
        self.fleet_drop_speed = 2

        # Configurações dos projéteis.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Taxa com que a velocidade aumenta.
        self.speedup_scale = 1.1

        # Taxa com que os pontos para cada alienígena aumentam.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam no decorrer do jogo."""
        self.ship_speed_factor = 0.2
        self.bullet_speed_factor = 0.3
        self.alien_speed_factor = 0.2

        # fleet_direction igual a 1 ==> direita;
        # fleet_direction igual a -1 ==> "esquerda"
        self.fleet_direction = 1

        # Pontuação.
        self.alien_points = 50

    def increase_speed(self):
        """Aumenta as configurações de velocidade."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)