from object import *
import utils


# pygame setup
pygame.init()
resolution = (1280, 720)

screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


running = True
deltaTime = 0
timer = 0

firingRate = 3



player = Object(20, "red", pygame.math.Vector2(screen.get_width()/2, screen.get_height()/2),[0,0],
                       [move_player_obj, velocity_movement])
objectList = [player]


def update_objects(object_list):

    # deletes bullets that are out of bounds of the window
    for i in range(len(objectList) - 1, -1, -1):
        if 0 > object_list[i][0] or object_list[i][0] > 1280 or 0 > object_list[i][1] or object_list[i][1] > 720:
            del object_list[i]

    return object_list



def spawn_bullet(ky, t ,object_list):


    initial_bullet_spd = 0.70

    if ky[pygame.K_LEFT]:
        new_vel = [player.vel[0] - initial_bullet_spd, player.vel[1]]
        new_bullet = Object(10, "white", (player.pos[0], player.pos[1]),new_vel,[velocity_movement])
        object_list.append(new_bullet)
        t = 0  # reset timer on key press so timer still runs above firing rate limit
    elif ky[pygame.K_RIGHT]:
        new_vel = [player.vel[0] + initial_bullet_spd, player.vel[1]]
        new_bullet = Object(10, "white", (player.pos[0], player.pos[1]), new_vel, [velocity_movement])
        object_list.append(new_bullet)
        t = 0
    elif ky[pygame.K_UP]:
        new_vel = [player.vel[0] , player.vel[1] - initial_bullet_spd]
        new_bullet = Object(10, "white", (player.pos[0], player.pos[1]), new_vel, [velocity_movement])
        object_list.append(new_bullet)
        t = 0
    elif ky[pygame.K_DOWN]:
        new_vel = [player.vel[0], player.vel[1] + initial_bullet_spd]
        new_bullet = Object(10, "white", (player.pos[0], player.pos[1]),new_vel, [velocity_movement])
        object_list.append(new_bullet)
        t = 0

    return objectList, t




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.display.set_caption(str(clock.get_fps()))

    # limit player position to bound of the window
    player.pos = utils.clamp_vector(player.pos, (0,0), resolution)

    keys = pygame.key.get_pressed()

    if keys and timer >= 1/firingRate:
       objectList, timer = spawn_bullet(keys,timer ,objectList)



    # iterates through each object and applies each function in the func_list to it
    for obj in objectList:
        for function in obj.func_list:
            function(obj, deltaTime, keys)
        obj.draw_obj(screen)





    pygame.display.flip()
    deltaTime = clock.tick() / 1000
    deltaTime = max(min(deltaTime, 0.1), 0.001)

    timer += deltaTime

pygame.quit()