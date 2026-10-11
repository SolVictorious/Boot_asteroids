import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        

    def draw(self, screen: pygame.Surface) -> None:
       pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
                
        
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            vect1 = self.velocity.rotate(angle)
            vect2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            s_asteriod1 = Asteroid(self.position.x,self.position.y,new_radius)
            s_asteriod1.velocity = vect1 * 1.2
            s_asteriod2 = Asteroid(self.position.x,self.position.y,new_radius)
            s_asteriod2.velocity = vect2 * 1.2