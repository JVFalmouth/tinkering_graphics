"""Contract #4 - Platformer Entity Reskinning
To enable better re-use of assets, a tool which reskins in-game items and
monsters devised by the dugeon entity. You will have to remove a colour
and then add a new colours. There are four types (representing qualities)
represented by a set of colours. For example: red, green, blue and yellow.
Each unit of these teams will have to be saved in a new png file."""


# Colours is a custom import containing a number of colours, as RGB tuples.
import pygame
import sys
import colours


__author__ = "James Vanstone"
__licence__ = "MIT"
__version__ = 1.0
__url__ = "github.com/JVFalmouth/tinkering_graphics"


def find_colours(image: pygame.Surface) -> list:
    """This function is used to find all of the different colours in an image.
    It will output a list of colours."""

    list_of_colours = []
    for x in range(image.get_size()[0]):
        for y in range(image.get_size()[1]):
            pos = (x, y)
            pixel = image.get_at(pos)
            if pixel not in list_of_colours:
                list_of_colours.append(pixel)
            image.set_at(pos, pixel)
    return list_of_colours


def change_colours(image: pygame.Surface, colour_to_change: pygame.Color,
                   target_colour: pygame.Color, new_file_name: str) -> pygame.Surface:
    """Function will convert a colour in an image into a different colour.
    It will save the edited image to file in the asset folder, and return the image."""

    for x in range(image.get_size()[0]):
        for y in range(image.get_size()[1]):
            pos = (x, y)
            pixel_col = image.get_at(pos)
            if pixel_col == colour_to_change:
                pixel_col = target_colour
            image.set_at(pos, pixel_col)
    pygame.image.save(image, f"assets/{new_file_name}_re-skin.png")
    return image


def cmd_line_options(image: pygame.Surface, window) -> pygame.Surface:
    colour_list = find_colours(image)
    for item in colour_list:
        print(item, end=", ")
    print("")
    colour_to_replace = colour_list[int(input("Select one of the colours to replace: ")) - 1]

    colour_options = {"Blue": colours.blue,
                      "Grey": colours.grey,
                      "Green": colours.green,
                      "Yellow": colours.yellow,
                      "Red": colours.red}

    for item in colour_options:
        print(item, end=" ")
    print("")
    colour_choice = ""
    while colour_choice not in colour_options:
        colour_choice = input("What colour would you like to replace it with?: ")
    image = change_colours(image, colour_to_replace, colour_options[colour_choice], colour_choice)
    window.blit(pygame.transform.scale(image, (300, 300)), (300, 0))  # Draw re-skinned image to screen.
    pygame.display.flip()
    return image


def tool(image: str):
    """This procedure is a tool for the re-skinning of simple images.
    It will not work well for images with many different colours.
    Procedure includes a pygame window, displaying the images."""

    pygame.init()
    window = pygame.display.set_mode((600, 300))

    image = pygame.image.load(image).convert()  # Load the image from file.

    window.fill(colours.black)
    window.blit(pygame.transform.scale(image, (300, 300)), (0, 0))  # Draw start image to screen.
    pygame.display.flip()

    cmd_line_options(image, window)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    while True:
        try:
            tool(input("File path: "))
        except pygame.error:
            print("That's not a valid file.")