import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""

    def __init__(self, ai_settings, screen):
        """Inicializa o alienígena e define sua posição inicial."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do alienígena e define seu atributo rect.
        self.image = pygame.image.load('images/TIE_48x44.bmp').convert_alpha()
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena.
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alienígena em sua posição inicial."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move o alien para a direia."""
        self.x += (self.ai_settings.alien_speed_factor *
                self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Devolve True se o alien estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True