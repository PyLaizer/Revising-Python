#Exercise 12.6

import sys
import pygame

from setting import Setting
from sideway_ship import Ship
from bullet import Bullet

class Shooter:
    """A class to manage the sideways-shooter game"""

    def __init__(self):
        """Initializing the pygame """
        pygame.init()
        self.setting = Setting()

        #Sets the windows display and the caption for our game
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption(self.setting.caption)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            self._check_event()
            self.ship.update()
            self.bullets.update()

            #Get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.left >= self.ship.screen_rect.right:
                    self.bullets.remove(bullet)
            print(len(self.bullets)) 
                   
            self._update_screen()
   

    def _check_event(self):
    #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_down_event(event)
            elif event.type == pygame.KEYUP:
                self._check_up_event(event)
                
    def _check_down_event(self,event):
        if event.key == pygame.K_UP:
            #Move the ship up
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            #Move the ship down
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()    

    def _check_up_event(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False 
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)        

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    ss = Shooter()
    ss.run_game()                   



