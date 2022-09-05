#Exercise 12.5

import pygame
import sys

class Test:
    """A class that shows an empty screen"""

    def __init__(self):
        """Initializes the test app"""
        pygame.init()

        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Empty screen")

    def run_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    #Convert the ascii codes (the defaulf format of event.key) to char
                    char = chr(event.key)
                    print(char)  



if __name__ == '__main__':
    test_instance = Test() 
    test_instance.run_screen()                         