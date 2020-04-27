import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    # Inicia o jogo e cria um objeto na tela.
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hight))
    pygame.display.set_caption("Alien Invasion")

    # Musica.
    pygame.mixer.music.load('songs/star_wars_theme.mp3')
    pygame.mixer.music.play()

    # Cria uma nave, um grupo de projéteis e um grupo de alienígenas.
    aliens = Group()
    ship = Ship(ai_settings, screen)
    bullets = Group()

    # Cria uma frota de alienígenas.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Define a cor de fundo.
    bg_color = (230, 230, 230)

    # Cria um objeto para armazenar os dados estatísticos.
    stats = GameStats(ai_settings)

    # Cria o botão Play.
    play_button = Button(ai_settings, screen, "Iniciar")

    # Incia o laço principal do jogo.
    while True:
        # Observa eventos de teclado e de mouse.
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
        
        if not stats.game_active:
            play_button.draw_button()
        
        # Deixa a tela mais recente visível.
        pygame.display.flip()
 
run_game()