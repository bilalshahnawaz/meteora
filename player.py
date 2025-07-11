import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, updatables, drawables, *groups):
        super().__init__(x, y, PLAYER_RADIUS, updatables, drawables, *groups)
        self.updatables = updatables
        self.drawables = drawables
        self.rotation = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        actions = {
            pygame.K_a: lambda: self.rotate(-dt),
            pygame.K_d: lambda: self.rotate(dt),
            pygame.K_w: lambda: self.move(dt),
            pygame.K_s: lambda: self.move(-dt),
            pygame.K_SPACE: self.shoot
        }
        for key, action in actions.items():
            if keys[key]:
                action()
                
        if self.shoot_timer:
            self.shoot_timer = max(0, self.shoot_timer - dt)


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer == 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.updatables, self.drawables)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN



