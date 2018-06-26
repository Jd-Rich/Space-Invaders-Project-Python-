import sys

import pygame
###Holds methods for Space Invaders###

def checkEvents(ship):
    "Responds to keyclicks and keyboard input"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                #move the ship to the right
                ship.movingRight = True
            elif event.key == pygame.K_a:
                ship.movingLeft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.movingRight = False
            elif event.key == pygame.K_a:
                ship.movingLeft = False

def updateScreen(aiSettings, screen, ship):
    """Update images on the screen and print to knew screen"""
    screen.fill(aiSettings.bgColor)
    ship.blitme()
    #make the most recently drawn screen visible
    pygame.display.flip()
