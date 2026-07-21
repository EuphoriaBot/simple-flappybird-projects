import pygame
import configs
import assets
from objects.background import Background
from objects.floor import Floor

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

assets.load_sprites()

sprite = pygame.sprite.LayeredUpdates()

Background(0, sprite)
Background(1, sprite)

Floor(0, sprite)
Floor(1, sprite)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("pink")

    sprite.draw(screen)
    sprite.update()

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()