import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        old_radius = self.radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_vel = random.uniform(20, 50)
            vel_a = self.velocity.rotate(new_vel)
            vel_b = self.velocity.rotate(-new_vel)
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            self.new_a = Asteroid(self.position.x, self.position.y, new_radius)
            self.new_b = Asteroid(self.position.x, self.position.y, new_radius)
            self.new_a.velocity = vel_a * 1.2
            self.new_b.velocity = vel_b * 1.2
            
            
            


