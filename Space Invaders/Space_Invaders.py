import pygame

from Settings import Settings
from Ship import Ship
import GameFunctions as gf

def runGame():
    #initialize pygame, screen and screen object
    pygame.init()
    aiSettings = Settings() #store the settings variables in the aiSettings to access them through this variable
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption(aiSettings.caption)

    #make a ship
    ship = Ship(aiSettings, screen)

    #start the main loop for the game
    while True:
        #Watch for keyboard/mouse events
        gf.checkEvents(ship)
        ship.update()
        gf.updateScreen(aiSettings, screen, ship)

runGame()
