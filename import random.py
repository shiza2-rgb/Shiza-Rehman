# Game 1
import random
import pygame
# import time
# import random 

def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit()
    
if __name__ == "__main__":
    main()
