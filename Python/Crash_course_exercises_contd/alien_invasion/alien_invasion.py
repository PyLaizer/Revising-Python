import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.setting = Settings()
        
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_heigth))
        pygame.display.set_caption(self.setting.caption)

        self.ship = Ship(self)
        # #Set the background color
        # self.bg_color = self.setting.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
                         
    def _check_events(self):
       """Respond to keypresses and mouse events."""
       for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

                    

    def _check_keydown_events(self,event):
        """Respond to keypress"""
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()    

    def _check_keyup_events(self,event):
        """Respond to keypress"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 


    def _update_screen(self):
        """Update images of the screen and flip to the new screen"""
        self.screen.fill(self.setting.bg_color)          
        self.ship.blitme()
        #Make the most recently drawn screen visible.
        pygame.display.flip()
        #Redraw the screen during each pass through the loop 
                            

if __name__ == '__main__':
    #Makes an instance, and runs the game by calling the run_game method
    ai = AlienInvasion()
    ai.run_game()          
    