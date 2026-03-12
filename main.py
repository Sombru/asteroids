import pygame
from constants import *
from logger import log_state

def main():
    print(f"Starting Asteroids...\n\
Screen width: {SCREEN_WIDTH}\n\
Screen height: {SCREEN_HEIGHT}\n\
with pygame version: {pygame.version.ver}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    for event in pygame.event.get():
    # while True:
        log_state()
        if event.type == pygame.QUIT:
            return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
