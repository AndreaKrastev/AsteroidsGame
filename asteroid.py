from circleshape import *
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            baby1 = Asteroid(self.position.x ,self.position.y , radius = new_radius)
            baby2 = Asteroid(self.position.x, self.position.y , radius = new_radius)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            baby1.velocity = vector1 * 1.2
            baby2.velocity = vector2 * 1.2
