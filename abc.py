import pygame, sys

pygame.init()

wood_bg = pygame.image.load('./shooting range assets/Wood_BG.png')
land_bg = pygame.image.load('./shooting range assets/Land_BG.png')
water_bg = pygame.image.load('./shooting range assets/Water_BG.png')
cloud_1 = pygame.image.load('./shooting range assets/Cloud1.png')
cloud_2 = pygame.image.load('./shooting range assets/Cloud2.png')
land_position_y = 560
land_speed = 1

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): # this allows pygame to listen for all the events happening on the window
            pygame.quit() # this will listen for the event for you to quit the window
            sys.exit()
    land_position_y -= 1

    screen.blit(wood_bg,(0,0))
    screen.blit(land_bg,(0,land_position_y))
    screen.blit(water_bg,(0,640))
    screen.blit(cloud_1, (200,0))
    screen.blit(cloud_2,(700,100))
    screen.blit(cloud_1, (1000,50))
    screen.blit(cloud_2,(50,100))
    
    pygame.display.update()
    clock.tick(120) # setting up the frame rate of the game, this will also let help you animate

