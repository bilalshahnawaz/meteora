import pygame
import random
from meteor import Meteor
from constants import *


class MeteorField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-METEOR_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + METEOR_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -METEOR_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + METEOR_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self, updatables, drawables, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.updatables = updatables
        self.drawables = drawables
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        print(f"Spawning meteor at {position} with velocity {velocity}")
        meteor = Meteor(position.x, position.y, radius, self.updatables, self.drawables)
        meteor.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > METEOR_SPAWN_RATE:
            self.spawn_timer = 0
            # Choose a random edge and spawn a meteor
            edge = random.choice(self.edges)
            kind = random.randint(1, METEOR_KINDS)
            radius = METEOR_MIN_RADIUS * kind
            t = random.random()
            direction = edge[0]
            position = edge[1](t)
            velocity = direction * (100 + random.random() * 100)
            self.spawn(radius, position, velocity)