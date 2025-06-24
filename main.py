import pygame
from database import connect_database, database_version
from constants import *
from player import Player
from meteorfield import MeteorField, Meteor


def main():
    pygame.init()

    print("Starting Meteora!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, updatables, drawables)

    MeteorField(updatables, drawables, updatables)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000 # Returns the amount of time since the last frame
        updatables.update(dt)

        for obj in drawables:
            obj.draw(screen)
            # Check collision only if obj is a Meteor
            if isinstance(obj, Meteor):
                if player.checkCollision(obj):
                    print("Game over!")
                    exit()


        pygame.display.flip()

if __name__ == "__main__":
    main()


