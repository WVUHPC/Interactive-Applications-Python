import math
import numpy as np
import pygame
import pymunk

PIX_W = 640
PIX_H = 480
FPS = 60

pygame.init()
display = pygame.display.set_mode((PIX_W, PIX_H))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 0, -100


def coor2pygame(point):
    return point[0], PIX_H - point[1]


class Ball:
    def __init__(self, x, y, radius=10):
        self.radius = radius
        self.body = pymunk.Body()
        self.body.position = int(x * PIX_W), int(y * PIX_H)
        self.shape = pymunk.Circle(self.body,
                                   self.radius)
        self.shape.density = 1
        self.shape.elasticity = 0.9
        space.add(self.body, self.shape)

    def draw(self):
        x, y = coor2pygame(self.body.position)
        pygame.draw.circle(display,
                           (255, 0, 0),
                           (int(x), int(y)),
                           self.radius)


class Floor:

    def __init__(self, angle=0, shift=0):

        self.body = pymunk.Body(mass=0,
                                moment=0,
                                body_type=pymunk.Body.STATIC)
        if angle >= 0:
            self.xleft = 0
            self.yleft = int(PIX_W * math.tan(angle * math.pi / 180)) + shift
            self.xright = PIX_W
            self.yright = shift
        else:
            self.xleft = 0
            self.yleft = shift
            self.xright = PIX_W
            self.yright = int(PIX_W * math.tan(-angle * math.pi / 180)) + shift

        self.shape = pymunk.Segment(self.body,
                                    (self.xleft, self.yleft),
                                    (self.xright, self.yright),
                                    5)
        self.shape.elasticity = 0.9
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.line(display,
                         (0, 0, 0),
                         coor2pygame((self.xleft, self.yleft)),
                         coor2pygame((self.xright, self.yright)),
                         10)


balls = []
for i in range(400):
    ball = Ball(np.random.rand(), 0.5 + 0.5 * np.random.rand())
    balls.append(ball)

floor1 = Floor(30, -100)
floor2 = Floor(-30, -100)


def simulate():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))

        for iball in balls:
            iball.draw()

        for ifloor in [floor1, floor2]:
            ifloor.draw()

        pygame.display.update()
        clock.tick(FPS)
        space.step(1 / FPS)


simulate()
pygame.quit()
