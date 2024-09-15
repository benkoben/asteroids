import pygame
import random

from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, width=2)

    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        asteroid1_velocity = self.velocity.rotate(random_angle)
        asteroid1_radius = self.radius - ASTEROID_MIN_RADIUS 

        asteroid2_velocity = self.velocity.rotate(-random_angle)
        asteroid2_radius = self.radius - ASTEROID_MIN_RADIUS 

        asteroid1 = Asteroid(
            self.position.x, 
            self.position.y, 
            asteroid1_radius
        ).velocity = asteroid1_velocity

        asteroid2 = Asteroid(
            self.position.x, 
            self.position.y, 
            asteroid2_radius
        ).velocity = asteroid2_velocity

