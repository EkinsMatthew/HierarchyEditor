import pygame

class Button:

    def __init__(self, label, pressed_function, color=pygame.Color("#eee8d5")):

        # Store the visual aspects of the Button
        self.label = label
        self.color = color

        # What function will we use when we press the button?
        self.pressed_function = pressed_function

    def press(self):
        