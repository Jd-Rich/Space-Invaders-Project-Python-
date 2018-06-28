import pygame
from pygame.sprite import Sprite

class Bullet(object, Sprite):
    """Manages bullets fired from the ship"""
    def __init__(self, aiSettings, screen, ship):
        """Create bullet object at ships current location"""
        super().__init__()
        self.screen = screen

        #Create bullet rect at (0,0) then correct pos
        self.rect = pygame.Rect(0,0, aiSettings.bulletWidth, aiSettings.bulletWidth)
        self.rect.centerx = ship.centerx
        self.rect.top = ship.top

        #store bullets pos as decimal
        self.y = float(self.rect.y)

        self.color = aiSettings.bulletColor
        self.speedFactor = aiSettings.bulletSpeedFactor

    def update(self):
        """Moves the bullet up the screen"""
        #update the decimal pos of bullet
        self.y -= self.speedFactor
        #update the rect pos
        self.rect.y = self.y

    def drawBullet(self):
        """Draws the bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)



