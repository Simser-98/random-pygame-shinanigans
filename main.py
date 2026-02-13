import pygame
import player
import utils

# pygame setup
pygame.init()
resolution = (1280, 720)

screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
running = True
deltaTime = 0


player = player.Player(20, "red", pygame.math.Vector2(screen.get_width()/2, screen.get_height()/2))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    player.pos = utils.clamp_vector(player.pos, (0,0), resolution)

    player.draw(screen)
    player.move(deltaTime)





    pygame.display.flip()

    deltaTime = clock.tick(240) / 1000

pygame.quit()