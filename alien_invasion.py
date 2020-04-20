import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    # Inicia o jogo e cria um objeto na tela.
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hight))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave.
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis.
    bullets = Group()

    # Define a cor de fundo.
    bg_color = (230, 230, 230)

    # Incia o laço principal do jogo.
    while True:
        # Observa eventos de teclado e de mouse.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
        # Deixa a tela mais recente visível.
        pygame.display.flip()
 
run_game()