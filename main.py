import pygame
import os
import time
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Text and messages
    event_text = pygame.font.Font(None, 74)
    game_over_msg = event_text.render("Game Over", True, "#FFFFFF")

    # Create groups
    bullets = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add game objects to groups
    # This ensures that new instances of these classes will be automatically
    # added to the correct sprite groups.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, bullets)

    # Initiate game objects
    middle_x = SCREEN_WIDTH / 2     # starting position
    middle_y = SCREEN_HEIGHT / 2    # starting position
    player = Player(middle_x, middle_y)
   
    asteroid_field = AsteroidField()

    # Start game loop
    while True:
        # Catch events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update positions accordingly
        for obj in updatable:
            obj.update(dt)
        
        # Check if any asteroids have collided with the player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                # screen.fill("#FF0000")
                # screen.blit(game_over_msg, (middle_x, middle_y))
                # pygame.display.flip()
                # time.sleep(5)
                sys.exit(0)

            for bullet in bullets:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()

        # Fill the screen with black backdrop
        screen.fill("#000000")

        # Draw all objects at their new positions
        for obj in drawable:
            obj.draw(screen)

        # Render the drawing
        pygame.display.flip()


        delta = clock.tick(60)
        dt = delta / 1000 # milliseconds to seconds


if __name__ == "__main__":
    main()
