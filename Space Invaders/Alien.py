import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    """Represents the aliens in the game"""
    def __init__(self, aiSettings, screen):
        """Initialize the alienand set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.aiSettings = aiSettings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
   

    
        

