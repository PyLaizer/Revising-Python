import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, side_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = side_game.screen
        self.setting = side_game.setting
        self.color = self.setting.bullet_color

        #Create a bullet rect at () and then set correct position
        self.rect = pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)
        self.rect.midleft = side_game.ship.rect.midleft

        #Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet right the screen"""  
        #Update the decimal position of the bullet
        self.x += self.setting.bullet_speed
        #Update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)     