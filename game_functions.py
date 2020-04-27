import sys
import pygame
from time import sleep
from alien import Alien
from bullet import Bullet

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Identifica se um alien atingil a borda da tela."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Responde da mesma forma quando a nave é atingida.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Responde quando a nave é atingida."""
    if stats.ships_left > 0:
        # Decrementa ships_left.
        stats.ships_left -= 1

        # Esvazia a lista de aliens e balas.
        aliens.empty()
        bullets.empty()

        # Recria a frota e centraliza a nave.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Faz uma leve pausa.
        sleep(0.5)
        
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_fleet_edges(ai_settings, aliens):
    """Responde se um alien alcançou a borda da tela."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Faz a frota mudar de direcção e desce na tela."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamento de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
                
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)   

    elif event.key == pygame.K_q:
        sys.exit()     
                
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship,
                aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """O jogo é iniciado quando o jogado clicar no botão."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reinicia os dados estatisticos do jogo.
        stats.reset_stats()
        stats.game_active = True

        # Esvazia a lista de balas e projeteis.
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a nave.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Oculta o cursor do mouse.
        pygame.mouse.set_visible(False)

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem de laço.
    screen.fill(ai_settings.bg_color)
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

def update_bullets(ai_settings, screen, ship, bullets, aliens):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis.
    bullets.update()

    # Livra-se dos projéteis que desapareceram.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # Verifica se algum projétil atingiu os aliens e apaga o projetil e o alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings,screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    # Cria um projétil e o adiciona ao grupo de projéteis.
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o número de linhas com alienígenas que cabem na tela."""
    available_space_y = (ai_settings.screen_hight - 
                        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_alien_x(ai_settings, alien_width):
    """Determina o número de alienígenas que cabem na tela."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Cria um alienígena e o posiciona na linha.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota completa de alienígenas."""
    # Cria um alienígina e calcula o número de alienígenas em uma linha.
    # O espaçamento entre os alienígenas é igaul à largura de um alienígena.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Cria a frota de alienígenas.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Verifica se a frota está em uma das bordas e 
    então atualiza as posições de todos os aliens da frota"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Indica se houve colisão entre um alien e a nave.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Verifica se um alien chegou até o fim da dela.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)