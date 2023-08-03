import pygame

PIX_W = 640
PIX_H = 480
FPS = 30

pygame.init()

display = pygame.display.set_mode((PIX_W, PIX_H))
clock = pygame.time.Clock()


def simula():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
        clock.tick(FPS)


simula()
pygame.quit()
