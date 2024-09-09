import pygame
import os

from constants import *
from player import Player

def main():
    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(player_x, player_y)
    
    # Start game loop
    while True:
        screen.fill("#000000")
        player.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        delta = clock.tick(60)
        dt = delta / 1000 # milliseconds to seconds


if __name__ == "__main__":
    main()
