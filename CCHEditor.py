# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:09:25 2023

@author: Matt
"""
import tkinter
import tkinter.filedialog
import pygame


class CCHEditor:
    # Colors of solarized
    colors = {
        "Content": [
            "#586e75",
            "#657b83",
            "#839496",
            "#93a1a1",
        ],
        "Background": {
            "Light": ["#eee8d5", "#fdf6e3"],
            "Dark": ["#002b36", "#073642"],
        },
        "Accent": [
            "#b58900",
            "#cb4b16",
            "#dc322f",
            "#d33682",
            "#6c71c4",
            "#268bd2",
            "#2aa198",
            "#859900",
        ],
    }

    # Version number
    VERSION = "0.0.1"

    def __init__(
        self,
        aspect_ratio=(16, 9),
        scale_factor=80,
        FPS=60,
        debug_mode=False,
        light_theme=True,
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

        Returns
        -------
        None.

        """

        # Initialize pygame
        pygame.init()

        # Store our passed vars

        # Screen sizes
        self.aspect_ratio = aspect_ratio
        self.scale_factor = scale_factor

        # FPS cap
        self.FPS = FPS
        # Debugg flag *NOT CURRENTLY USED*
        self.debug_mode = debug_mode

        if light_theme:
            # Light background color
            background_color = CCHEditor.colors["Background"]["Light"][0]
        else:
            # Dark background color
            background_color = CCHEditor.colors["Background"]["Dark"][0]

        # Initialize the window
        self.initiate_window(background_color=background_color)

        # Start the clock
        self.start_clock()

        # Define our default font
        self.create_default_font()

    def initiate_window(self, background_color):
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
        # Calculate the dimensions as the multiplication of the aspect ration
        # by the scale factor.
        self.dimensions = tuple([x * self.scale_factor for x in self.aspect_ratio])
        # Set the screen as a new display with the dimensions stated
        self.screen = pygame.display.set_mode(self.dimensions)

        # Set the original background color
        self.screen.fill(background_color)

    def get_screen(self):
        return self.screen

    def start_clock(self):
        # Out clock for frame rate and update
        self.clock = pygame.time.Clock()

    def create_default_font(self, font_name="consolas"):
        # Define the font that we will be using to write to the screen
        pygame.font.init()
        # Get the place on this machine where the font is stored
        font_loc = pygame.font.match_font(font_name)
        # Create our font
        self.font = pygame.font.Font(font_loc, 14)

    def tick(self):
        f_name = ""

        # Process user inputs.
        for event in pygame.event.get():
            # Check for QUIT event
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            # Check for various key-presses
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    f_name = self.prompt_for_file()

        # The current location of the mouse
        mouse_loc = pygame.mouse.get_pos()

        # Logical updates
        self.screen.set_at(mouse_loc, CCHEditor.colors["Accent"][4])

        pygame.display.set_caption(
            f"CCH Editor {self.VERSION} Open file: {f_name} Mouse position: {mouse_loc}"
        )

        # Update the display
        pygame.display.flip()

        self.clock.tick(self.FPS)

    def prompt_for_file(self):
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
    editor = CCHEditor(scale_factor=120, light_theme=False)

    # Create the main game window
    screen = editor.get_screen()

    # Create a test sprite and draw it on the screen
    test_sprite = pygame.sprite.Sprite()

    # game loop
    while True:
        editor.tick()


# Execute the main function if the interpreter gets here
if __name__ == "__main__":
    main()
