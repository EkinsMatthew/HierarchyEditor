# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:09:25 2023

@author: Matt
"""
from __future__ import annotations
import typing

import tkinter
import tkinter.filedialog
import pygame
import Colors
from Window import Window
from ToolButton import ToolButton


class CCHEditor(Window):
    """
    Test doc.
    """

    # Version number
    VERSION = "0.0.1"

    def __init__(
        self,
        aspect_ratio: tuple[int, int] = (16, 9),
        scale_factor: int = 80,
        font_name: str = "consolas",
        theme: str = "light",
        FPS: int = 60,
        debug_mode: bool = False,
    ):
        """
        Parameters
        ----------
        aspect_ratio : tuple, optional
            The aspect ratio of the window expressed as a tuple. i.e. 4:3 ->
            (4,3), etc. The default is (16,9).
        scale_factor : int, optional
            Multiply the values in apspect ratio by this factor to get our F
            screen resolution. e.g. if aspect_ratio = (4,3) and scale_factor =
            200, the final screen resolution will be 800x600. The default is 80
            which combined with the default aspect_ratio of (16,9) gives us a
            screen resolution of 1280x700.
        FPS : int, optional
            The frame rate cap on the program window. The default is 60.
        debug_mode : bool, optional
            If the program should be run in debug mode. Will show various
            diagnostics in the console on tick. The default is False.
        theme : str, optional
            The theme of the color pallete. Follows the Solarized standard.
            Currently supported values are "light" and "dark". The default is
            light.

        Returns
        -------
        None.

        """

        # Initialize pygame
        pygame.init()

        # Construct the window with the superclass constructor
        super(CCHEditor, self).__init__(
            aspect_ratio, scale_factor, font_name, theme=theme
        )

        # FPS cap
        self.FPS = FPS
        # Debugg flag *NOT CURRENTLY USED*
        self.debug_mode = debug_mode

        # Initialize the window
        self._initialize_window()

        # Start the clock
        self._start_clock()

        # Create our first test button
        self.button = ToolButton("File", (0, 0), print, self)

        self.button.draw(self.screen)

    def _initialize_window(self):
        """
        Create the window for the game to take place in. Here we determine the
        size of the window.

        Parameters
        ----------
        None.

        Returns
        -------
        pygame Screen that was constructed with the parameters defined above.

        """
        # Set the screen as a new display with the dimensions stated
        self.screen = pygame.display.set_mode(self.window_size)

        # Set the original background color
        self.screen.fill(self.background_color)

    def get_screen(self) -> pygame.Surface:
        return self.screen

    def _start_clock(self):
        # Out clock for frame rate and update
        self.clock = pygame.time.Clock()

    def get_clock(self) -> pygame.time.Clock:
        return self.clock

    def get_font(self) -> pygame.font.Font:
        return self.font

    def tick(self):
        # Process user inputs.
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            # Check for various key-presses
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    f_name = self._prompt_for_file()

        # The current location of the mouse
        mouse_loc = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed(num_buttons=5)[0]:
            if self.button.get_rect().collidepoint(mouse_loc):
                self.button.press()

        # Logical updates
        self.screen.set_at(mouse_loc, Colors.get_color("Magenta"))

        pygame.display.set_caption(
            f"CCH Editor {self.VERSION} Mouse position: {mouse_loc}"
        )

        # Update the display
        pygame.display.flip()

        self.clock.tick(self.FPS)

    def _prompt_for_file(self):
        # Create a Tk window
        tk_wind = tkinter.Tk()
        # Remove from view since we don't want it for graphics
        tk_wind.withdraw()
        # Get the file chosen by the user
        file_name = tkinter.filedialog.askopenfilename(parent=tk_wind)
        # Kill the window since we don't need it anymore
        tk_wind.destroy()

        return file_name


def main():
    # Create the editor
    editor = CCHEditor(scale_factor=120, theme="dark")

    # Create the main game window
    screen = editor.get_screen()

    # game loop
    while True:
        editor.tick()


# Execute the main function if the interpreter gets here
if __name__ == "__main__":
    main()
