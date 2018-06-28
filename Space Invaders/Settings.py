class Settings(object):
    """A class to store all of the setting for Alien Invasion"""
    def __init__(self):
        """initialize the games settings"""
        #Screen settings
        self.screenWidth = 1400
        self.screenHeight = 700
        self.bgColor = (0,0,0)
        self.caption = "Alien Invasion"

        #Ship settings
        self.shipSpeedFactor = 1.5

        #Bullet settings
        self.bulletSpeedFactor = 1
        self.bulletHeight = 15
        self.bullerWidth = 3
        self.bulletColor = (5,5,5)



        




