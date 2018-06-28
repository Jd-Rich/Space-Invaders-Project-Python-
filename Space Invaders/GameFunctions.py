import sys

import pygame
###Holds methods for Space Invaders###

def checkEvents(ship):
    "Responds to keyclicks and keyboard input"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, ship)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, ship)

def checkKeydownEvents(event, ship):
    """Responds to key presses"""
    if event.key == pygame.K_d:
        ship.movingRight = True
    elif event.key == pygame.K_a:
        ship.movingLeft = True

def checkKeyupEvents(event, ship):
    """Responds to key releases"""
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
