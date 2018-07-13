import pygame
from pygame.sprite import Group

from Settings import Settings
from Ship import Ship
from Alien import Alien

import GameFunctions as gf

def runGame():
    #initialize pygame, screen and screen object
    pygame.init()
    aiSettings = Settings() #store the settings variables in the aiSettings to access them through this variable
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption(aiSettings.caption)

    #make a ship
    ship = Ship(aiSettings, screen)
    #make an alien
    alien = Alien(aiSettings, screen)

    #make a group to store bullets in & a group of aliens
    bullets = Group()
    aliens = Group()

    #create the fleat of aliens
    gf.createFleet(aiSettings, screen, ship, aliens)

    #start the main loop for the game
    while True:
        #Watch for keyboard/mouse events
        gf.checkEvents(aiSettings, screen, ship, bullets)
        ship.update()
        gf.updateBullets(bullets)
        gf.updateScreen(aiSettings, screen, ship, aliens, bullets)

runGame()
