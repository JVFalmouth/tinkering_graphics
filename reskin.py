"""Contract #4 - Platformer Entity Reskinning
To enable better re-use of assets, a tool which reskins in-game items and
monsters devised by the dugeon entity. You will have to remove a colour
and then add a new colours. There are four types (representing qualities)
represented by a set of colours. For example: red, green, blue and yellow.
Each unit of these teams will have to be saved in a new png file."""

import sys, pygame, colours
from pygame.locals import *


def find_colours(image: pygame.Surface):
    list_of_colours = []
    for x in range (image.get_size()[0]):
        for y in range(image.get_size()[1]):
            pos = (x, y)
            pixel = image.get_at(pos)
            if pixel not in list_of_colours:
                list_of_colours.append(pixel)
            image.set_at(pos, pixel)
    return list_of_colours


def change_colours(image: pygame.Surface, colour):
    for x in range (image.get_size()[0]):
        for y in range(image.get_size()[1]):
            pos = (x, y)
            pixel_col = image.get_at(pos)
            if pixel_col == colour:
                pixel_col.b = 30
            image.set_at(pos, pixel_col)
    pygame.image.save(image, "reskin.png")


def tool(image: str):
    image = pygame.image.load(image)
    colour_list = find_colours(image)
    print(colour_list)
    colour_to_replace = colour_list[int(input("Select one of the colours to replace: "))-1]
    change_colours(image, colour_to_replace)



tool("assets/sans.png")