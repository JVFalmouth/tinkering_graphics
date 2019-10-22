"""Contract #4 - Platformer Entity Reskinning
To enable better re-use of assets, a tool which reskins in-game items and
monsters devised by the dugeon entity. You will have to remove a colour
and then add a new colours. There are four types (representing qualities)
represented by a set of colours. For example: red, green, blue and yellow.
Each unit of these teams will have to be saved in a new png file."""

import sys, pygame, colours
from pygame.locals import *


def change_colour(image: pygame.Surface, colour):
    image_array = pygame.PixelArray(image)
    print(image_array.shape)
    image_array.replace(colours.blue, colours.green, 0, 0)
    pygame.image.save(image_array, "sprite.jpg")


def tool(image: str):
    image = pygame.image.load(image)
    change_colour(image, colours.blue)


tool("assets/sans.png")