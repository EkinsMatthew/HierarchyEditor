from __future__ import annotations
import typing

import pygame
import Colors
from Window import Window


class Button:
    """
    Generic class of pressable button for windows. This button exists within a
    window and inherits most of its default behavior from that window.
    """

    def __init__(
        self,
        label: str,
        location: tuple[int, int],
        press_function: typing.Callable,
        owner: Window,
        face_color: typing.Optional[str] = None,
        text_color: typing.Optional[str] = None,
    ):
        """Create a Button.

        Parameters
        ----------
        label : str
            Text to appear on the face of the button
        location : tuple[int, int]
            Location of the top left corner. Where should this button be drawn?
        press_function : typing.Callable
            The function to call when the Button is pressed
        owner : Window
            The window that this button sits within.
        """

        print("Button Constructor")

        # Store the visual aspects of the Button
        self.label = label
        if face_color is None:
            self.face_color = owner.background_color
        else:
            self.face_color = face_color
        if text_color is None:
            self.text_color = Colors.get_color("content_0")
        else:
            self.text_color = text_color

        # Our font is the font of the editor
        self.font = owner.font

        # Store the editor
        self.owner = owner

        # Render our text
        self.label_surface = self._render_label(self.text_color)

        # Store the location of the top left corner
        self.x = location[0]
        self.y = location[1]

        self.rect = self._build_rect()

        # What function will we use when we press the button?
        self.press_function = press_function

    def _render_label(self, color: str) -> pygame.Surface:
        return self.owner.font.render(self.label, True, color)

    def _build_rect(self) -> pygame.rect.Rect:
        """Build the rectangle that will surround the text. This is the main
        body of the button.

        Returns
        -------
        pygame.rect.Rect
            The rectangle of the button.
        """

        # The rectangle that bounds the text as rendered
        text_rect = self.label_surface.get_rect()

        # Last value is the height of the text
        text_height = text_rect[3]
        # Length of the entire string
        text_width = text_rect[2]

        # How far we want to scoot the text to be in the middle of rect
        self.text_x_offset = self.owner.string_spacer
        self.text_y_offset = int(text_height / 2)

        # Define rect coords in reference to the text_coords

        return pygame.rect.Rect(
            self.x,
            self.y,
            text_width + 2 * self.owner.string_spacer,
            text_height * 2,
        )

    def get_rect(self) -> pygame.rect.Rect:
        """Returns the rectangle bounding box of the Button.

        Returns
        -------
        pygame.rect.Rect
            The rectangle of the button.
        """
        return self.rect

    def draw(self, screen: pygame.Surface, offset: tuple[int, int] = (0, 0)):
        """Draw the button on the screen where specified.

        Parameters
        ----------
        screen : pygame.Surface
            The surface on which to draw the button
        offset : tuple[int, int], optional
            _description_, by default (0, 0)
        """

        pygame.draw.rect(screen, color=self.face_color, rect=self.rect)
        screen.blit(
            self.label_surface,
            (self.x + self.text_x_offset, self.y + self.text_y_offset),
        )

    def press(self):
        """Activate the function of the button."""
        self.press_function()
