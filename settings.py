class Settings():
    """Uma classe para armanezar todas as funções do jogo."""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da Tela.
        #self.screen_width = 1520
        #self.screen_hight = 900

        self.screen_width = 800
        self.screen_hight = 600

        #self.screen_width = 1200
        #self.screen_hight = 900
        
        # Configurações de cor da tela
        self.bg_color = (100, 100, 100)

        # Configurações da espaçonave.
        self.ship_speed_factor = 1.5

        # Configurações dos projéteis.
        self.bullet_speed_factor = 3
        self.bullet_widht = 3
        self.bullet_hight = 15
        self.bullet_color = 0, 220, 0
        self.bullet_allowed = 3