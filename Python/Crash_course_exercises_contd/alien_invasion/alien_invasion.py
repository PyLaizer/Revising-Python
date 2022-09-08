import sys
import pygame


from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            #Get rid of bullets that have disappeared
            # for bullet in self.bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         self.bullets.remove(bullet)
            # print(len(self.bullets))        


                         
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()    

    def _check_keyup_events(self,event):
        """Respond to keypress"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)   

    def _create_fleet(self):
        """Create the fleet of aliens"""
        #Make an alien and find the number of aliens in a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.setting.screen_width - (2 * alien_width)
        num_of_alien_x = available_space_x // (2 * alien_width)

        #Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.setting.screen_heigth - (3 * alien_height) - ship_height)
        num_rows = available_space_y // (2 * alien_height)

        #Create the first row of aliens
        for row_num in range(num_rows):
            for alien_number in range(num_of_alien_x):
                self._create_alien(alien_number, row_num)
               

    def _create_alien(self, alien_number, row_num):
        """Create an alien and place it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number 
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_num
        self.aliens.add(alien)                    

    def _update_screen(self):
        """Update images of the screen and flip to the new screen"""
        self.screen.fill(self.setting.bg_color)          
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)    
        #Make the most recently drawn screen visible.
        pygame.display.flip()
        #Redraw the screen during each pass through the loop 
                            

if __name__ == '__main__':
    #Makes an instance, and runs the game by calling the run_game method
    ai = AlienInvasion()
    ai.run_game()          
    