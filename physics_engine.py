import sys, pygame, math, gc, colours
from pygame.locals import *
from window_options import *


class GameObject:
    def __init__(self, x: int, y: int):
        self.sprite = None
        self.x = x
        self.y = y
        self.velocity = (0, 0)
        self.mass = 100
        self.drag_coefficient = 1
        self.has_gravity = False

    def trail(self, surface):
        surface.set_at((int(self.x), int(self.y)), (255, 255, 255))

    def set_sprite(self, image: str, scale: int):
        self.sprite = pygame.transform.scale(pygame.image.load(image), (scale, scale))

    def phys_update(self, dt):
        self.add_force(self.drag())
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def drag(self):
        x = (-self.drag_coefficient * self.velocity[0])
        y = (-self.drag_coefficient * self.velocity[1])
        return (x, y)

    def add_force(self, force: tuple) -> tuple:
        x = (self.velocity[0] + force[0] / self.mass)
        y = (self.velocity[1] + force[1] / self.mass)
        resultant_velocity = (x, y)
        self.velocity = resultant_velocity


def update_physics(objects: list, gravity: tuple, dt):
    for game_object in objects:
        if game_object.has_gravity:
            game_object.add_force(gravity)
        game_object.phys_update(dt)


def render_frame(objects: list, surface):
    for game_object in objects:
        if type(game_object) == GameObject:
            if type(game_object.sprite) == pygame.Surface:
                game_object.render(surface)
            else:
                game_object.trail(surface)
        else:
            game_object.render(surface)


def key_movement(event, movement_force: tuple) -> tuple:
    if event.type == pygame.KEYDOWN:
        if event.key == K_w:  # up
            movement_force = movement_force[0], movement_force[1] - 2
        if event.key == K_s:  # down
            movement_force = movement_force[0], movement_force[1] + 2
        if event.key == K_a:  # left
            movement_force = movement_force[0] - 2, movement_force[1]
        if event.key == K_d:  # right
            movement_force = movement_force[0] + 2, movement_force[1]

    if event.type == pygame.KEYUP:
        if event.key == K_w:  # up
            movement_force = movement_force[0], movement_force[1] + 2
        if event.key == K_s:  # down
            movement_force = movement_force[0], movement_force[1] - 2
        if event.key == K_a:  # left
            movement_force = movement_force[0] + 2, movement_force[1]
        if event.key == K_d:  # right
            movement_force = movement_force[0] - 2, movement_force[1]
    return movement_force


def game():
    pygame.init()

    monitor = pygame.display.Info()
    monitor_res = (monitor.current_w, monitor.current_h)
    default_res = (1000,1000)
    res = [default_res, monitor_res]

    screen = pygame.display.set_mode(res[1], flags=FULLSCREEN)
    is_fullscreen = True
    ball = GameObject(50, 50)

    ball.set_sprite("assets/sprite.png", 30)
    ball.render(screen)
    game_objects = []
    for obj in gc.get_objects():
        if isinstance(obj, GameObject):
            game_objects.append(obj)

    clock = pygame.time.Clock()
    screen.fill(colours.black)

    movement_force = (0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_F12:
                    is_fullscreen, screen = toggle_fullscreen(is_fullscreen, screen, res)
                # movement
            movement_force = key_movement(event, movement_force)

        delta_time = clock.tick()
        ball.add_force(movement_force)
        update_physics(game_objects, 0, delta_time)
        render_frame(game_objects, screen)
        pygame.display.flip()


if __name__ == "__main__":
    game()