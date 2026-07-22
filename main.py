import pygame
import configs
import assets
from objects.background import Background
from objects.floor import Floor
from objects.column import Column

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True

assets.load_sprites()

sprite = pygame.sprite.LayeredUpdates()

Background(0, sprite)
Background(1, sprite)
Floor(0, sprite)
Floor(1, sprite)

Column(sprite)

pygame.time.set_timer(column_create_event, millis=1500)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            Column(sprite)

    screen.fill("pink")

    sprite.draw(screen)
    sprite.update()

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()