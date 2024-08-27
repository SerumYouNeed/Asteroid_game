import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    plr = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for plr in updatable:
            plr.update(dt)
        
        screen.fill('black')

        for plr in drawable:
            plr.draw(screen)

        pygame.display.flip()
            
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
