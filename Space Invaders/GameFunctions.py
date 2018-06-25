import sys

import pygame
###Holds methods for Space Invaders###

def checkEvents():
    "Responds to keyclicks and keyboard input"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def updateScreen(aiSettings, screen, ship):
    """Update images on the screen and print to knew screen"""
    screen.fill(aiSettings.bgColor)
    ship.blitme()
    #make the most recently drawn screen visible
    pygame.display.flip()
