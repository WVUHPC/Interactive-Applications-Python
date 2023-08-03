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

    def __init__(self):
        self.body = pymunk.Body(mass=0,
                                moment=0,
                                body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body,
                                    (0, 20),
                                    (PIX_W, 0), 5)
        self.shape.elasticity = 0.9
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.line(display,
                         (0, 0, 0),
                         coor2pygame((0, 20)),
                         coor2pygame((PIX_W, 0)),
                         10)


ball = Ball(0.2, 0.5)
floor = Floor()


def simulate():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))

        ball.draw()
        floor.draw()

        pygame.display.update()
        clock.tick(FPS)
        space.step(1 / FPS)


simulate()
pygame.quit()
