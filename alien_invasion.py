import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Inicia o jogo e cria um objeto na tela.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hight))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave.
    ship = Ship(screen)

    # Define a cor de fundo.
    bg_color = (230, 230, 230)

    # Incia o laço principal do jogo.
    while True:
        # Observa eventos de teclado e de mouse.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
        # Deixa a tela mais recente visível.
        pygame.display.flip()

run_game()