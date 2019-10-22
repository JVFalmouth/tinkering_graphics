import sys, pygame
from pygame.locals import *


def toggle_fullscreen(is_fullscreen: bool, screen: pygame.display, res: list) -> (bool, pygame.display):

    if is_fullscreen:
        pygame.display.quit()
        pygame.display.init()
        screen = pygame.display.set_mode(res[0], flags=RESIZABLE)
        is_fullscreen = False
    else:
        pygame.display.quit()
        pygame.display.init()
        screen = pygame.display.set_mode(res[1], flags=FULLSCREEN)
        is_fullscreen = True

    return is_fullscreen, screen