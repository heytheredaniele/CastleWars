from sys import exit
from swordsman import *
from worker import *
from archer import *
from random import randint as r
from building import *
from army_functions import *
import pygame

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
menu_screen = pygame.transform.scale(pygame.image.load('images/background/aquila.jpg'), (1000, 250))
pygame.display.set_caption('CastleWars')

# font
title_font = pygame.font.Font('images/font/Pixeltype.ttf', 75)
screen_font = pygame.font.Font('images/font/Pixeltype.ttf', 40)
small_test_font = pygame.font.Font('images/font/Pixeltype.ttf', 25)

clock = pygame.time.Clock()

# background and ground
background = pygame.transform.scale(pygame.image.load('images/background/aquila.jpg'), (1000, 250))
ground = pygame.transform.scale(pygame.image.load('images/background/good_ground.png'), (1000, 250))
ground_below = pygame.image.load('images/background/good_ground.png')

# Groups
red_swordsmen_army = pygame.sprite.Group()
blue_swordsmen_army = pygame.sprite.Group()
red_archers_army = pygame.sprite.Group()
blue_archers_army = pygame.sprite.Group()
red_workers_army = pygame.sprite.Group()
blue_workers_army = pygame.sprite.Group()

red_archer_arrows = pygame.sprite.Group()
blue_archers_arrow = pygame.sprite.Group()
red_tower_arrows = pygame.sprite.Group()
blue_tower_arrows = pygame.sprite.Group()

# Adding buildings
red_mine = Building(pygame.image.load('images/player1/building/mine.png'), MINE_POS, SCREEN_HEIGHT - GROUND_HEIGHT)
blue_mine = Building(pygame.image.load('images/player2/building/mine.png'), 1000 - MINE_POS,
                     SCREEN_HEIGHT - GROUND_HEIGHT)
red_barracks = Building(pygame.image.load('images/player1/building/barracks.png'), BARRACKS_POS,
                        SCREEN_HEIGHT - GROUND_HEIGHT)
blue_barracks = Building(pygame.image.load('images/player2/building/barracks.png'), 1000 - BARRACKS_POS,
                         SCREEN_HEIGHT - GROUND_HEIGHT)
red_tower = Building(pygame.image.load('images/player1/building/tower.png'), WALL_POS, SCREEN_HEIGHT - GROUND_HEIGHT)
red_wall = Building(pygame.image.load('images/player1/building/wall.png'), WALL_POS, SCREEN_HEIGHT - GROUND_HEIGHT)

blue_tower = Building(pygame.image.load('images/player2/building/tower.png'), 1000 - WALL_POS,
                      SCREEN_HEIGHT - GROUND_HEIGHT)
blue_wall = Building(pygame.image.load('images/player2/building/wall.png'), 1000 - WALL_POS,
                     SCREEN_HEIGHT - GROUND_HEIGHT)

blue_mines_group = pygame.sprite.Group(red_mine)
red_mines_group = pygame.sprite.Group(blue_mine)
blue_barracks_group = pygame.sprite.Group(red_barracks)
red_barracks_group = pygame.sprite.Group(blue_barracks)
blue_wall_group = pygame.sprite.Group(red_wall)
red_walls_group = pygame.sprite.Group(blue_wall)
blue_tower_group = pygame.sprite.Group(blue_tower)
red_towers_group = pygame.sprite.Group(red_tower)


def menu_display():
    game_title_surf = title_font.render('CastleWars', False, 'Black')
    game_title_rect = game_title_surf.get_rect(center=(500, 50))
    screen.blit(game_title_surf, game_title_rect)

    start_surf = screen_font.render('To start the game press "enter" ...', False, 'Black')
    start_rect = start_surf.get_rect(center=(500, 200))
    screen.blit(start_surf, start_rect)


def group_display_update():
    # display the buildings for player 2
    blue_tower_group.update()
    blue_tower_group.draw(screen)
    blue_wall_group.update()
    blue_wall_group.draw(screen)
    blue_barracks_group.update()
    blue_barracks_group.draw(screen)
    blue_mines_group.update()
    blue_mines_group.draw(screen)

    # display the arrows for player 2
    red_archer_arrows.update()
    red_archer_arrows.draw(screen)
    red_tower_arrows.update()
    red_tower_arrows.draw(screen)

    # display the armies for player 2
    red_swordsmen_army.update()
    red_swordsmen_army.draw(screen)
    red_archers_army.update()
    red_archers_army.draw(screen)
    red_workers_army.update()
    red_workers_army.draw(screen)

    # display the buildings for player 1
    red_towers_group.update()
    red_towers_group.draw(screen)
    red_walls_group.update()
    red_walls_group.draw(screen)
    red_barracks_group.update()
    red_barracks_group.draw(screen)
    red_mines_group.update()
    red_mines_group.draw(screen)

    # display the armies for player 1
    blue_swordsmen_army.update()
    blue_swordsmen_army.draw(screen)
    blue_archers_army.update()
    blue_archers_army.draw(screen)
    blue_workers_army.update()
    blue_workers_army.draw(screen)

    # display the arrows for player 1
    blue_archers_arrow.update()
    blue_archers_arrow.draw(screen)
    blue_tower_arrows.update()
    blue_tower_arrows.draw(screen)


def text(data, swordsmen1_army, swordsman2_text, worker1_army, worker2_army, archer1_army, archer2_army):
    swordsman1_text = small_test_font.render('Swordsmen: ' + str(len(swordsmen1_army)), False, 'WHITE')
    swordsman1_rect = swordsman1_text.get_rect(topleft=(10, 10))

    swordsman2_text = small_test_font.render('Swordsmen: ' + str(len(blue_swordsmen_army)), False, 'WHITE')
    swordsman2_rect = swordsman1_text.get_rect(topright=(960, 10))

    archer1_text = small_test_font.render('Archers: ' + str(len(archer1_army)), False, 'WHITE')
    archer1_rect = archer1_text.get_rect(topleft=(10, 25))

    archer2_text = small_test_font.render('Archers: ' + str(len(archer2_army)), False, 'WHITE')
    archer2_rect = archer2_text.get_rect(topright=(960, 25))

    worker1_text = small_test_font.render('Workers: ' + str(len(worker1_army)), False, 'WHITE')
    worker1_rect = worker1_text.get_rect(topleft=(10, 40))

    worker2_text = small_test_font.render('Workers: ' + str(len(worker2_army)), False, 'WHITE')
    worker2_rect = worker2_text.get_rect(topright=(960, 40))

    wall1_text = small_test_font.render(f'WALL HEALTH: {data["p1_wallhealth"]}', False, 'WHITE')
    wall1_rect = wall1_text.get_rect(topleft=(10, 55))

    wall2_text = small_test_font.render(f'WALL HEALTH: {data["p2_wallhealth"]}', False, 'WHITE')
    wall2_rect = wall2_text.get_rect(topright=(960, 55))

    p1_rescource_text = small_test_font.render(f'RESOURCES: {int(data["p1_resources"])}', False, 'Pink')
    p1_rescource_rect = p1_rescource_text.get_rect(topleft=(10, 70))

    p2_rescource_text = small_test_font.render(f'RESOURCES: {int(data["p2_resources"])}', False, 'Pink')
    p2_rescource_rect = p2_rescource_text.get_rect(topright=(960, 70))

    screen.blit(swordsman1_text, swordsman1_rect)
    screen.blit(swordsman2_text, swordsman2_rect)

    screen.blit(archer1_text, archer1_rect)
    screen.blit(archer2_text, archer2_rect)

    screen.blit(worker1_text, worker1_rect)
    screen.blit(worker2_text, worker2_rect)

    screen.blit(wall1_text, wall1_rect)
    screen.blit(wall2_text, wall2_rect)

    screen.blit(p1_rescource_text, p1_rescource_rect)
    screen.blit(p2_rescource_text, p2_rescource_rect)


def resume():
    playagain_surf = screen_font.render('To resume the game press "space" ...', False, 'Black')
    playagain_rect = playagain_surf.get_rect(center=(500, 125))
    screen.blit(playagain_surf, playagain_rect)
    pygame.display.update()

    resume = True
    while resume:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resume = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


# data
data = {'p1_resources': INIT_RESOURCES, 'p2_resources': INIT_RESOURCES, 'p1_wallhealth': WALL_HEALTH,
        'p2_wallhealth': WALL_HEALTH}


# worker collision
def workers_collision(workers, mine, wall, player):
    global data
    player_health_counter = 0
    for worker in workers:
        # worker collision to mine
        if pygame.sprite.spritecollideany(worker, mine):
            worker.dig = True
            
            if player == 1:
                data['p1_resources'] += WORKER_PROD/100
                return data['p1_resources']
            else:
                data['p2_resources'] += WORKER_PROD/100
                return data['p2_resources']
            
                

        # worker collision to wall
        if pygame.sprite.spritecollideany(worker, wall):
            worker.repair = True
            player_health_counter += 1
            if player_health_counter == 100:
                player_health_counter = 0
                if player == 1:
                    data['p1_wallhealth'] += WORKER_REPAIR
                    if data['p1_wallhealth'] >= 1000:
                        data['p1_wallhealth'] = 1000
                        return data['p1_wallhealth']
                else:
                    data['p2_wallhealth'] += WORKER_REPAIR
                    if data['p2_wallhealth'] >= 1000:
                        data['p2_wallhealth'] = 1000
                        return data['p2_wallhealth']


# Main loop
game_active = False

while True:
    if game_active == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # Stop and resume
                if event.key == pygame.K_SPACE:
                    resume()
                # Spawning P1 Units
                if event.key == pygame.K_w and data['p1_resources'] >= SWORD_COST and len(red_swordsmen_army) < 30:
                    red_swordsman = Swordsman(swordsman1_ready, swordsman1_run, swordsman1_attack, swordsmasn1_dead,
                                              r(55, 157), 1)
                    red_swordsmen_army.add(red_swordsman)
                    data['p1_resources'] -= SWORD_COST
                if event.key == pygame.K_q and data['p1_resources'] >= WORKER_COST:
                    red_worker = Worker(worker1_ready, worker1_run_left, worker1_run_right, worker1_dig, worker1_repair,
                                        r(75, 147))
                    red_workers_army.add(red_worker)
                    data['p1_resources'] -= WORKER_COST
                if event.key == pygame.K_e and data['p1_resources'] >= ARCHER_COST and len(red_archers_army) < 30:
                    red_archer = Archer(archer1_ready, archer1_run, archer1_shoot, archer1_dead, r(65, 167))
                    red_archers_army.add(red_archer)
                    data['p1_resources'] -= ARCHER_COST
                # Unleash P1 Units separately
                if event.key == pygame.K_d:
                    for swordsman in red_swordsmen_army:
                        swordsman.unleash = True
                if event.key == pygame.K_f:
                    for archer in red_archers_army:
                        archer.unleash = True
                # Unleash P1 Units together
                if event.key == pygame.K_z:
                    for swordsman in red_swordsmen_army:
                        swordsman.unleash = True
                    for archer in red_archers_army:
                        archer.unleash = True
                # Worker movement
                if event.key == pygame.K_a:
                    for red_worker in red_workers_army:
                        if red_worker.run_right == False:
                            red_worker.run_left = True

                if event.key == pygame.K_s:
                    for red_worker in red_workers_army:
                        if red_worker.run_left == False:
                            red_worker.run_right = True
                # Spawning P2 Units
                if event.key == pygame.K_o and data['p2_resources'] >= SWORD_COST and len(blue_swordsmen_army) < 30:
                    blue_sowrdsman = Swordsman(swordsman2_ready, swordsman2_run, swordsman2_attack, swordsman2_dead,
                                               1000 - r(55, 157), 2)
                    blue_swordsmen_army.add(blue_sowrdsman)
                    data['p2_resources'] -= SWORD_COST
                if event.key == pygame.K_p and data['p2_resources'] >= WORKER_COST:
                    blue_worker = Worker(worker2_ready, worker2_run_left, worker2_run_right, worker2_dig,
                                         worker2_repair,
                                         1000 - randint(75, 137))
                    blue_workers_army.add(blue_worker)
                    data['p2_resources'] -= WORKER_COST
                if event.key == pygame.K_i and data['p2_resources'] >= ARCHER_COST and len(blue_archers_army) < 30:
                    blue_archer = Archer(archer2_ready, archer2_run, archer2_shoot, archer2_dead,
                                         1000 - randint(65, 167))
                    blue_archers_army.add(blue_archer)
                    data['p2_resources'] -= ARCHER_COST
                # Unleash P1 Units separately
                if event.key == pygame.K_j:
                    for swordsman in blue_swordsmen_army:
                        swordsman.unleash = True
                if event.key == pygame.K_h:
                    for archer in blue_archers_army:
                        archer.unleash = True
                # Unleash P1 Units together
                if event.key == pygame.K_m:
                    for swordsman in blue_swordsmen_army:
                        swordsman.unleash = True
                    for archer in blue_archers_army:
                        archer.unleash = True
                # Worker movement
                if event.key == pygame.K_k:
                    for blue_worker in blue_workers_army:
                        if blue_worker.run_right == False:
                            blue_worker.run_left = True
                if event.key == pygame.K_l:
                    for blue_worker in blue_workers_army:
                        if blue_worker.run_left == False:
                            blue_worker.run_right = True

        if data['p1_wallhealth'] <= 0 or data['p2_wallhealth'] <= 0:
            game_active = False

        swordsmen_collision(red_swordsmen_army, blue_swordsmen_army, red_walls_group, blue_archers_army,
                            data['p2_wallhealth'])
        swordsmen_collision(blue_swordsmen_army, red_swordsmen_army, blue_wall_group, red_archers_army,
                            data['p1_wallhealth'])

        # archer_collision(archers1_army, archers2_army, swordsmen2_army, archer_arrows1, Arrow(a_arrow1, archer1.rect.x, "archer", 0, 0), walls2_building, data['p2_wallhealth'])
        # archer_collision(archers2_army, archers1_army, swordsmen1_army, archer_arrows2, Arrow(a_arrow1, archer2.rect.x, "archer", 0, 0), walls1_building, data['p1_wallhealth'])

        workers_collision(red_workers_army, blue_mines_group, blue_wall_group, 1)
        workers_collision(blue_workers_army, red_mines_group, red_walls_group, 2)

        # Background
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 250 - GROUND_HEIGHT))
        screen.blit(ground_below, (0, 250 - GROUND_HEIGHT))
        text(data, red_swordsmen_army, blue_swordsmen_army, red_workers_army, blue_workers_army, red_archers_army,
             blue_archers_army)
        # Groups draw and update
        group_display_update()


    elif game_active == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True
                    data = {'p1_resources': INIT_RESOURCES, 'p2_resources': INIT_RESOURCES,
                            'p1_wallhealth': WALL_HEALTH, 'p2_wallhealth': WALL_HEALTH}
                    red_workers_army.empty()
                    blue_workers_army.empty()
                    red_archers_army.empty()
                    blue_archers_army.empty()
                    red_swordsmen_army.empty()
                    blue_swordsmen_army.empty()
                    red_archer_arrows.empty()
                    blue_archers_arrow.empty()
                    red_tower_arrows.empty()
                    blue_tower_arrows.empty()
        screen.blit(menu_screen, (0, 0))
        menu_display()
        if data["p1_wallhealth"] <= 0:
            blue_surf = screen_font.render("BLUE WINS!!!", False, "Blue")
            blue_rect = blue_surf.get_rect(center=(500, 125))
            screen.blit(blue_surf, blue_rect)
        if data["p2_wallhealth"] <= 0:
            red_surf = screen_font.render("RED WINS!!!", False, "Red")
            red_rect = red_surf.get_rect(center=(500, 125))
            screen.blit(red_surf, red_rect)
    pygame.display.update()
    clock.tick(60)
