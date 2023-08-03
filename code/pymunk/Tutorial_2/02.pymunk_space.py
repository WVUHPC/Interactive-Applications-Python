import pygame
import pymunk

PIX_W = 640
PIX_H = 480
FPS = 60

pygame.init()

display = pygame.display.set_mode((PIX_W, PIX_H))
clock = pygame.time.Clock()
space = pymunk.Space()


def simula():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
        clock.tick(FPS)
        space.step(1 / FPS)


simula()
pygame.quit()
