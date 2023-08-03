import pygame
import pymunk

PIX_W = 640
PIX_H = 480
FPS = 60

pygame.init()
display = pygame.display.set_mode((PIX_W, PIX_H))
clock = pygame.time.Clock()
space = pymunk.Space()

body = pymunk.Body()
body.position = int(PIX_W/10), int(PIX_H/10)
shape = pymunk.Circle(body, 10)
shape.density = 1
space.add(body, shape)

def coor2pygame(point):
    return point[0], PIX_H-point[1]
def simulate():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((255, 255, 255))
        x, y = coor2pygame(body.position)
        pygame.draw.circle(display,
                           (255, 0, 0),
                           (int(x), int(y)),
                           10)
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

simulate()
pygame.quit()
