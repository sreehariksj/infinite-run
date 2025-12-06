import random
import pygame

pygame.init()

# Game contences
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
WIDTH = 450
HIGHT = 300

# Player variables
player_x = 50
player_y = 200
y_change = 0
x_change = 0
gravity = 1
obstacle = [300, 450, 600]
obstacle_speed = 2
active = True
score = 0

screen = pygame.display.set_mode([WIDTH, HIGHT])
pygame.display.set_caption('Infinite Runner')
background = black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

running = True
while running:
    timer.tick(fps)
    screen.fill(background)
    if not active:
        instruction_text = font.render(
            f'Space button to restart', True, white, black)
        screen.blit(instruction_text, (160, 50))

    score_text = font.render(f'Score: {score}', True, white, black)
    screen.blit(score_text, (160, 250))
    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, green, [player_x, player_y, 20, 20])

    for i in obstacle:
        obstacle0 = pygame.draw.rect(screen, red, [obstacle[0], 200, 20, 20])

        obstacle1 = pygame.draw.rect(screen, blue, [obstacle[1], 200, 20, 20])

        obstacle2 = pygame.draw.rect(
            screen, yellow, [obstacle[2], 200, 20, 20])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not active:
            obstacle = [300, 450, 600]
            player_x = 50
            score = 0
            active = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18
            if event.key == pygame.K_RIGHT:
                x_change = 2
            if event.key == pygame.K_LEFT:
                x_change = -2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0

    for i in range(len(obstacle)):
        if active:
            obstacle[i] -= obstacle_speed
            if obstacle[i] < -20:
                obstacle[i] = random.randint(430, 570)
                score += 1
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                active = False

    if 0 < player_x <= 430:
        player_x += x_change
    if player_x <= 0:
        player_x = 1
    if player_x >= 430:
        player_x = 430

    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    pygame.display.flip()
pygame.quit()
