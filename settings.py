class Settings():
    """Uma classe para armanezar todas as funções do jogo."""

    def __init__(self):
        """Inicializa as configurações do jogo."""

        """Configurações e opções de tamanho de tela, basta remover o "#" do...
        conjunto de tamanho que deseja utilizar e adiocionar no conjunto que não está sendo utilizado."""

        self.screen_width = 1520
        self.screen_hight = 900

        #self.screen_width = 800
        #self.screen_hight = 600

        #self.screen_width = 1200
        #self.screen_hight = 800
        
        # Configurações de cor da tela
        self.bg_color = (25, 25, 55)

        # Configurações da espaçonave.
        self.ship_speed_factor = 3

        # Configurações dos projéteis.
        self.bullet_speed_factor = 2
        self.bullet_widht = 3
        self.bullet_hight = 15
        self.bullet_color = 0, 220, 0
        self.bullet_allowed = 20

        # Configurações dos aliens.
        self.alien_speed_factor = 1.5
        self.fleet_drop_speed = 10
        # fleet_direction igual a 1 ==> direita;
        # fleet_direction igual a -1 ==> "esquerda"
        self.fleet_direction = 1