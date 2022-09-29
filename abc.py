
import pygame
import random
import sys

pygame.init()

wood_bg = pygame.image.load('./shooting range assets/Wood_BG.png')
land_bg = pygame.image.load('./shooting range assets/Land_BG.png')
water_bg = pygame.image.load('./shooting range assets/Water_BG.png')
cloud_1 = pygame.image.load('./shooting range assets/Cloud1.png')
cloud_2 = pygame.image.load('./shooting range assets/Cloud2.png')
second_cloud_1 = pygame.image.load('./shooting range assets/Cloud1.png')
second_cloud_2 = pygame.image.load('./shooting range assets/Cloud2.png')
crosshair = pygame.image.load('./shooting range assets/crosshair.png')
duck = pygame.image.load('./shooting range assets/duck.png')

game_font = pygame.font.Font(None, 60)
font = game_font.render('GAME OVER', True, (255, 255, 255))
end_rect = font.get_rect(center=(640, 360))

land_position_y = 540
land_speed = 1

water_position_y = 640
water_speed = 2

cloud_1_position_x = 200
cloud_1_speed = 1

cloud_2_position_x = 700
cloud_2_speed = 0.5

second_cloud_2_x = 50
second_cloud_2_speed = 1.5

second_cloud_1_x = 1000
second_cloud_1_speed = 1


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
crosshair_rect = (640, 360)
duck_list = []
arr = []
for i in range(10):
    random_x = random.randrange(50, 1200)
    random_y = random.randrange(120, 600)
    duck_rect = duck.get_rect(center=(random_x, random_y))
    duck_list.append(duck_rect)

while True:
    for event in pygame.event.get():
        # this allows pygame to listen for all the events happening on the window
        if (event.type == pygame.QUIT):
            pygame.quit()  # this will listen for the event for you to quit the window
            sys.exit()

        if (event.type == pygame.MOUSEMOTION):
            crosshair_rect = crosshair.get_rect(center=event.pos)
            # event.pos gives us the current position of the event on the screen
            # get_rect() makes the rectangle around the image on which it is called

        if (event.type == pygame.MOUSEBUTTONDOWN):
            # enumerate gives you the index of the item that you are looping in the list
            for index, i in enumerate(duck_list):
                # crosshair_rect.colliderect(duck_rect) takes in two rectangle and returns a bool
                result = crosshair_rect.colliderect(i)
                if (result):
                    # this delets the ducks that overlasp the crosshair rectangle
                    del duck_list[index]


# object movement
    water_position_y = water_position_y + water_speed
    cloud_1_position_x = cloud_1_position_x + cloud_1_speed
    cloud_2_position_x = cloud_2_position_x - cloud_2_speed
    land_position_y = land_position_y - land_speed

    if (water_position_y <= 530 or water_position_y >= 650):
        water_speed = water_speed * -1

    if (cloud_1_position_x <= 190 or cloud_1_position_x >= 400):
        cloud_1_speed = cloud_1_speed * -1

    if (cloud_2_position_x <= 600 or cloud_2_position_x >= 750):
        cloud_2_speed = cloud_2_speed * -1

    if (land_position_y <= 510 or land_position_y >= 560):
        land_speed = land_speed * -1
# displaying the objects on the screen
    screen.blit(crosshair, crosshair_rect)
    screen.blit(wood_bg, (0, 0))

    for i in duck_list:
        screen.blit(duck, i)

    if (len(duck_list) == 0):
        screen.blit(font, end_rect)

    screen.blit(land_bg, (0, land_position_y))
    screen.blit(water_bg, (0, water_position_y))
    screen.blit(cloud_1, (cloud_1_position_x, 0))
    screen.blit(cloud_2, (cloud_2_position_x, 25))
    screen.blit(second_cloud_1, (second_cloud_1_x, 50))
    screen.blit(second_cloud_2, (second_cloud_2_x, 100))
    screen.blit(crosshair, crosshair_rect)

    pygame.display.update()
    # setting up the frame rate of the game, this will also let help you animate
    clock.tick(120)
