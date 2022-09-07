#Exercise 12.6

class Setting():
    """A class to manage the setting"""

    def __init__(self) -> None:
        self.bg_color = (240,255,255)
        self.caption = "Sideways Shooter"
        self.screen_height = 600
        self.screen_width = 800
        self.ship_speed = 1.2

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = (220,20,60)
        