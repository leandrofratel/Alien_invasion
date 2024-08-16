class Settings():
    """Uma classe para armanezar todas as funções do jogo."""

    def __init__(self):
        """Inicializa as configurações estáticas do jogo."""

        """Configurações e opções de tamanho de tela, basta remover o "#" do...
        conjunto de tamanho que deseja utilizar e adiocionar no conjunto em...
        que não está sendo utilizado."""
        # Configurações da tela.
        self.screen_width = 1000
        self.screen_hight = 800
       
        # Configurações de cor da tela
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave.
        self.ship_limit = 3

        # Configurações dos alienígenas.
        self.fleet_drop_speed = 2

        # Configurações dos projéteis.
        self.bullet_widht = 3
        self.bullet_hight = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Taxa com que a velocidade aumenta.
        self.speedup_scale = 0.2

        # Taxa com que os pontos para cada alienígena aumentam.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam no decorrer do jogo."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

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