#Exercise 12.2 & 12.4
import pygame

class RocketShip:
    """A class to manage Rocket Ship"""

    def __init__(self,rocket_game):
        """Initializing the rocket ship"""
        self.screen = rocket_game.screen
        self.setting = rocket_game.setting
        self.screen_rect = rocket_game.screen.get_rect()

        #Load ship image and get its rect
        self.image = pygame.image.load('images/rocketship.bmp')
        self.rect = self.image.get_rect()

        #Start each ship at the center of the screen
        self.rect.center = self.screen_rect.center

        #Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.rocket_ship_speed_x
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.setting.rocket_ship_speed_x
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.setting.rocket_ship_speed_y
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.rocket_ship_speed_y            

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draws the ship at its current location"""
        self.screen.blit(self.image,self.rect)    

        