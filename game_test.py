import pygame

WIDTH_SCREEN = 800
HEIGHT_SCREEN = 600

screen = pygame.display.set_mode(WIDTH_SCREEN, HEIGHT_SCREEN)

pygame.display.set_caption("pygame")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
