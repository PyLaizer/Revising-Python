import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage alien a single alien"""

    def __init__(self,ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        #Load the alien image and set it's rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if aliens is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True    

    def update(self):
        """Move the alien to the right"""    
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x

