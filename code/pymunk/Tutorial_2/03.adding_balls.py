import pygame
import pymunk

PIX_W = 640
PIX_H = 480
FPS = 60

pygame.init()

display = pygame.display.set_mode((PIX_W, PIX_H))
clock = pygame.time.Clock()
space = pymunk.Space()


def coor2pygame(point):
    return int(point[0]), int(PIX_H - point[1])


class Ball:
    def __init__(self, x, y):
        self.body = pymunk.Body()
        self.body.position = int(x * PIX_W), int(y * PIX_H)
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.density = 1

    def draw(self):
        pygame.draw.circle(display,
                           (255, 0, 0),
                           coor2pygame(self.body.position),
                           10)


def simula():
    ball_1 = Ball(0.3, 0.6)
    ball_2 = Ball(0.4, 0.3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        ball_1.draw()
        ball_2.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.step(1 / FPS)


simula()
pygame.quit()
