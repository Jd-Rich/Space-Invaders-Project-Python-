import sys

import pygame

from Bullet import Bullet
from Alien import Alien
###Holds methods for Space Invaders###

def checkEvents(aiSettings, screen, ship, bullets):
    "Responds to keyclicks and keyboard input"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event, aiSettings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyupEvents(event, ship)

def checkKeydownEvents(event, aiSettings, screen, ship, bullets):
    """Responds to key presses"""
    if event.key == pygame.K_d:
        ship.movingRight = True
    elif event.key == pygame.K_a:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        fireBullets(aiSettings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def checkKeyupEvents(event, ship):
    """Responds to key releases"""
    if event.key == pygame.K_d:
        ship.movingRight = False
    elif event.key == pygame.K_a:
        ship.movingLeft = False

def updateScreen(aiSettings, screen, ship, alien, bullets):
    """Update images on the screen and print to knew screen"""
    screen.fill(aiSettings.bgColor)
    
    #Redraw all bullets behind ships and aliens
    for bullet in bullets.sprites():
        bullet.drawBullet()
        bullet.update()
    ship.blitme()
    alien.draw(screen)
    alien.blitme()
    #make the most recently drawn screen visible
    pygame.display.flip()

def updateBullets(bullets):
    #gets rid of bullets that go off screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def fireBullets(aiSettings, screen, ship, bullets):
    """Fire bullet if limit isn't reached"""
    #create new bullet and add it to the bullet group
    if len(bullets) < aiSettings.bulletsAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)

def createFleet(aiSettings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    #Create an alien and find the numer of aliens in a row
    alien = Alien(aiSettings, screen)
    numberAliensX = getNumberAliensX(aiSettings, alien.rect.width)
    numberRows = getNumberOfRows(aiSettings, ship.rect.height, alien.rect.height)
    
    #create the first row of aliens
    for rowNumber in range(numberRows):
        for alienNumber in range(numberAliensX):
            createAlien(aiSettings, screen, aliens, alienNumber, rowNumber)
       

def getNumberAliensX(aiSettings, alienWidth):
    """Determine the number of aliens that fit in a row"""
    availableSpaceX = aiSettings.screenWidth - (2*alienWidth)
    numberAliensX = int(availableSpaceX / (2*alienWidth))
    return numberAliensX

def createAlien(aiSettings, screen, aliens, alienNumber, rowNumber):
    """Create an alien and place it in a row"""
    alien = Alien(aiSettings, screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2*alienWidth * alienNumber
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
    aliens.add(alien)

def getNumberOfRows(aiSettings, shipHeight, alienHeight):
    """Determine the number of rows of aliens that fit on the screen"""
    availableSpaceY = (aiSettings.screenHeight - (3*alienHeight) - shipHeight)
    numberRows = int(availableSpaceY / (2*alienHeight))
    return numberRows