from __future__ import annotations
import typing

import pygame
import Colors


class Window:
    """
    Generic window class. This can be defined as the window of the entire app,
    or a sub-window within one.
    """

    def __init__(
        self,
        aspect_ratio: tuple[int, int],
        scale_factor: int,
        font_name: str,
        theme: str,
        background_color: typing.Optional[str] = None,
        text_color: typing.Optional[str] = None,
    ):

        # Store the aspect ratio
        self.aspect_ratio = aspect_ratio

        # Calculate the resulting window size
        self.window_size = tuple([x * scale_factor for x in self.aspect_ratio])

        # Define the default font using the font_name provided
        self.font = self._create_default_font(font_name)
        # Standard buffer size as the width of a space
        self.string_spacer = self.font.metrics(" ")[0][4]

        # Define default colors if they did not provide ones
        if background_color is None:
            self.background_color = Colors.get_color("background_light", theme)
        else:
            self.background_color = background_color
        if text_color is None:
            self.text_color = Colors.get_color("content_0")
        else:
            self.text_color = text_color

    def _create_default_font(self, font_name: str) -> pygame.font.Font:
        # Define the font that we will be using to write to the screen
        pygame.font.init()
        # Get the place on this machine where the font is stored
        font_loc = pygame.font.match_font(font_name)
        # Create our font
        self.font = pygame.font.Font(font_loc, 16)

        return self.font
