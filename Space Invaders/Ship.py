import pygame

class Ship(object):
    """Initializes the ship and set its starting position"""
    def __init__(self, screen):
        self.screen = screen
        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #movement flag
        self.movingRight = False
        self.movingLeft = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ships position based on the movement flag"""
        if self.movingRight:
            self.rect.centerx += 1
        if self.movingLeft:
            self.rect.centerx -= 1




