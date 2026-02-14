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
timer = 0



player = player.Player(20, "red", pygame.math.Vector2(screen.get_width()/2, screen.get_height()/2))
firingRate = 3
initialBulletSpd = 0.75
bulletLst = []
bulletVel = []

def bullet_update(bullet_lst, bullet_vel):

    for i in range(len(bullet_lst)):
        bullet_lst[i] = (bullet_lst[i][0] + bullet_vel[i][0], bullet_lst[i][1] + bullet_vel[i][1])

    return bullet_lst



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.display.set_caption(str(clock.get_fps()))

    player.pos = utils.clamp_vector(player.pos, (0,0), resolution)

    keys = pygame.key.get_pressed()

    if keys and timer >= 1/firingRate:

        if keys[pygame.K_LEFT]:
            bulletLst.append((player.pos[0], player.pos[1]))
            bulletVel.append((-initialBulletSpd + player.vel[0], player.vel[1]))
        elif keys[pygame.K_RIGHT]:
            bulletLst.append((player.pos[0], player.pos[1]))
            bulletVel.append(((initialBulletSpd + player.vel[0]), player.vel[1]))
        elif keys[pygame.K_UP]:
            bulletLst.append((player.pos[0], player.pos[1]))
            bulletVel.append((player.vel[0], (-initialBulletSpd + player.vel[1])))
        elif keys[pygame.K_DOWN]:
            bulletLst.append((player.pos[0], player.pos[1]))
            bulletVel.append((player.vel[0], (+initialBulletSpd + player.vel[1])))
        timer = 0

    bulletLst = bullet_update(bulletLst, bulletVel, deltaTime)

    for bullet in bulletLst:
        pygame.draw.circle(screen, "white", (bullet[0], bullet[1]), 10)

    player.draw(screen)
    player.move(deltaTime, keys)










    pygame.display.flip()

    deltaTime = clock.tick() / 1000
    deltaTime = max(min(deltaTime, 0.1), 0.001)

    timer += deltaTime

pygame.quit()