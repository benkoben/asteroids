import pygame
import os

from constants import *
from player import Player

def main():
    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create game objects
    player_x = SCREEN_WIDTH / 2     # starting position
    player_y = SCREEN_HEIGHT / 2    # starting position
    player = Player(player_x, player_y)

    # Create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    # Add game objects to groups
    updatables.add(player)
    drawables.add(player)
    
    # Start game loop
    while True:
        # Events that happend each iteration before rendering
        screen.fill("#000000")
        
        for obj in updatables:
            obj.update(dt)

        for obj in drawables:
            obj.draw(screen)

        # Render
        pygame.display.flip()

        # Catch events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        delta = clock.tick(60)
        dt = delta / 1000 # milliseconds to seconds


if __name__ == "__main__":
    main()
