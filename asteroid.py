import circleshape
import pygame

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)