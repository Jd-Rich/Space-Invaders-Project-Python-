class Settings(object):
    """A class to store all of the setting for Alien Invasion"""
    def __init__(self):
        """initialize the games settings"""
        #Screen settings
        self.screenWidth = 1200
        self.screenHeight = 700
        self.bgColor = (0,0,0)
        self.caption = "Alien Invasion"

        #Ship settings
        self.shipSpeedFactor = 1.5

        #Bullet settings
        self.bulletSpeedFactor = 2
        self.bulletHeight = 15
        self.bulletWidth = 3
        self.bulletColor = (0,250,0)
        self.bulletsAllowed = 3



        




