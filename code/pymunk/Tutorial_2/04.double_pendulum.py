import pygame
import pymunk

PIX_W = 640
PIX_H = 480
FPS = 60

pygame.init()

display = pygame.display.set_mode((PIX_W, PIX_H))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, -200)

def coor2pygame(point):
    return int(point[0]), int(PIX_H - point[1])


class Ball:
    def __init__(self, x, y):
        self.body = pymunk.Body()
        self.body.position = int(x * PIX_W), int(y * PIX_H)
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.density = 1
        space.add(self.body, self.shape)

    def draw(self):
        pygame.draw.circle(display,
                           (255, 0, 0),
                           coor2pygame(self.body.position),
                           10)


class String():
    def __init__(self, body, attachment, id="body"):
        self.body1 = body
        if id == "body":
            self.body2 = attachment
        elif id == "position":
            self.body2 = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.body2.position = attachment
        joint = pymunk.PinJoint(self.body1, self.body2)
        space.add(joint)

    def draw(self):
        pos1 = coor2pygame(self.body1.position)
        pos2 = coor2pygame(self.body2.position)
        pygame.draw.line(display,
                         (0, 0, 0),
                         pos1,
                         pos2,
                         2)


def simula():
    ball_1 = Ball(0.2, 0.99)
    ball_2 = Ball(0.5, 0.99)

    string_1 = String(ball_1.body,
                      (int(0.5 * PIX_W), int(0.9 * PIX_H)),
                      "position")
    string_2 = String(ball_1.body, ball_2.body)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        ball_1.draw()
        ball_2.draw()
        string_1.draw()
        string_2.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.step(1 / FPS)


simula()
pygame.quit()
