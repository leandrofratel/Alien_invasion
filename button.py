import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Atributos do botão."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Dimensões do botão e propriedades.
        self.widht, self.height = 200, 50
        self.button_color = (25, 25, 55)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Constrói o objeto rect do botão e o centraliza.
        self.rect = pygame.Rect(0, 0, self.widht, self.height)
        self.rect.center = self.screen_rect.center

        # Mensagem do botão.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Converte msg em imagem renderizada e centraliza o texto no botão."""
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Desenha um botão em branco, e desenha a mensagem.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)