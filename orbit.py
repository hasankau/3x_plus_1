import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 1024, 600
YELLOW = (180,150,0)
BLUE = (0,150,180)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 32)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3X+1")

class Star:
    def __init__(self, x, y, radius, mass, color):
        self.x = x
        self.y = y
        self.color = color
        self.mass = mass
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

class Planet:
    def __init__(self, x, y, radius, mass, color):
        self.x = x
        self.y = y
        self.color = color
        self.mass = mass
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


sun = Star(500, 300, 20, 565, YELLOW)
earth = Planet(420, 300, 5, 565, BLUE)


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        sun.draw(WIN)
        earth.draw(WIN)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
main()