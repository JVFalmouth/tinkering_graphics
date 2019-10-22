"""Contract #4 - Platformer Entity Reskinning
To enable better re-use of assets, a tool which reskins in-game items and
monsters devised by the dugeon entity. You will have to remove a colour
and then add a new colours. There are four types (representing qualities)
represented by a set of colours. For example: red, green, blue and yellow.
Each unit of these teams will have to be saved in a new png file."""


# Colours is a custom import containing a number of colours, as RGB tuples.
import pygame
import colours


def find_colours(image: pygame.Surface) -> list:
    """This function is used to find all of the different colours in an image.
    It will output a list of colours."""
    list_of_colours = []
    for x in range (image.get_size()[0]):
        for y in range(image.get_size()[1]):
            pos = (x, y)
            pixel = image.get_at(pos)
            if pixel not in list_of_colours:
                list_of_colours.append(pixel)
            image.set_at(pos, pixel)
    return list_of_colours


def change_colours(image: pygame.Surface, colour_to_change: pygame.Color, target_colour: pygame.Color) -> pygame.Surface:
    """Function will convert a colour in an image into a different colour.
    It will save the edited image to file as "reskin.png" in the asset folder, and return the image.
    THIS FUNCTION IS BROKEN and I don't know why."""
    for x in range(image.get_size()[0]):
        for y in range(image.get_size()[1]):
            pos = (x, y)
            pixel_col = image.get_at(pos)
            if pixel_col == colour_to_change:
                pixel_col = target_colour
            image.set_at(pos, pixel_col)
    pygame.image.save(image, "assets/reskin.png")
    return image


def tool(image: str):
    """This function is a tool for the re-skinning of simple images.
    It will not work well for images with many different colours."""
    image = pygame.image.load(image)
    colour_list = find_colours(image)
    print(colour_list)
    colour_to_replace = colour_list[int(input("Select one of the colours to replace: "))-1]
    image = change_colours(image, colour_to_replace, colours.yellow)  # currently just using yellow for development.


tool("assets/sans.png")  # Pre-made simple sprite, included in the /assets folder. Simply for testing purposes.
