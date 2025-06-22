from circleshape import CircleShape
import pygame

class Meteor(CircleShape):
    def __init__(self, x, y, radius, *groups):
        super().__init__(x, y, radius, *groups)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

