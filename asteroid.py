import pygame # type: ignore[import]
import random
from logger import log_event
from circleshape import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        radius = self.radius
        velocity = self.velocity
        self.kill()
        if radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_vel = velocity
        angle = random.uniform(20, 50)
        vel1 = split_vel.rotate(angle)
        vel2 = split_vel.rotate(-angle)
        new_radius = radius - ASTEROID_MIN_RADIUS
        troid1 = Asteroid(self.position,self.position,new_radius)
        troid1.velocity = vel1 * 1.2
        troid2 = Asteroid(self.position,self.position,new_radius)
        troid2.velocity = vel2 * 1.2



    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)