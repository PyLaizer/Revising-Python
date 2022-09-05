#Exercise 12.1 & 12.4

import sys
import pygame

from alien_test_settings import Setting
from rocket_ship import RocketShip

class Game:
    """A class to manage a test game"""

    def __init__(self):
        """Initializes the game"""
        pygame.init()
        self.setting = Setting()

        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption(self.setting.caption)

        self.rocket_ship = RocketShip(self)

    def run_game(self):
        while True:
            self._check_event()
            self.rocket_ship.update()
            self._update_screen()
       
    def _check_event(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.rocket_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket_ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket_ship.moving_up = True                         
        elif event.key == pygame.K_DOWN:
            self.rocket_ship.moving_down = True
              
    def _check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.rocket_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket_ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket_ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket_ship.moving_down = False                            




    def _update_screen(self):
        """Update images of the screen and flip to the new screen"""
        self.screen.fill(self.setting.bg_color)
        self.rocket_ship.blitme()        
        #Make the most recently drawn screen visible.
        pygame.display.flip()        
                                  


if __name__ == '__main__':
    at = Game()
    at.run_game()
