import pygame
import sys
import os
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

score = 0

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    plr = Player(x, y)
    field = AsteroidField() 

    while True:
        font = pygame.font.Font(None, 36)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if plr.is_collide(asteroid):
                sys.exit("Game over!")

            for bullet in shots:
                global score
                if asteroid.is_collide(bullet):
                    bullet.kill()
                    asteroid.split()
                    score += SCORE_INCREMENT


        screen.fill('black')

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
            
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
