import pygame

class Ship(object):
    """Initializes the ship and set its starting position"""
    def __init__(self, aiSettings, screen):
        self.screen = screen
        self.aiSettings = aiSettings

        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #store a decimal value for the ships center
        self.center = float(self.rect.centerx)

        #movement flag
        self.movingRight = False
        self.movingLeft = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ships position based on the movement flag"""
        #update the ships center value, not the rect + make sure doesn't go off screen
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.center += self.aiSettings.shipSpeedFactor
        if self.movingLeft and self.rect.left > 0:
            self.center -= self.aiSettings.shipSpeedFactor

        #update the rect object from self.center
        self.rect.centerx = self.center





