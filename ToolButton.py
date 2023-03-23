# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:44:04 2023

@author: Matt
"""
from __future__ import annotations
import typing

import pygame

from Button import Button
from Window import Window


class ToolButton(Button):

    # TODO Fix class constructor for the toolbutton. As it stands, no code after the super() call is executed.
    def __init__(
        self,
        label: str,
        location: tuple[int, int],
        press_function: typing.Callable,
        owner: Window,
        parent: typing.Optional[ToolButton] = None,
        children: list[ToolButton] = [],
        shortcut: typing.Optional[str] = None,
    ):
        # Initialize the parent class constructor
        super(ToolButton, self).__init__(
            label=label,
            location=location,
            press_function=press_function,
            owner=owner,
            face_color=owner.background_color,
            text_color=owner.text_color,
        )

        print("ToolButton Constructor")

        # Store the hierarchical information
        self.parent = parent
        self.children = children
        # Measure all children
        self._measure_children()

        # Store the shortcut string
        self.shortcut = shortcut
        self.shortcut_surface = self._render_shortcut(self.text_color)

        # Instantiate hover flag
        self.cursor_hovered = False

    def add_child(self, button: ToolButton):
        self.children.append(button)
        # Optimized code for checking label length
        self._measure_child(button)

    def _measure_children(self):
        # We are remeasuring, so reset
        self.max_child_label_width = 0
        self.max_child_shortcut_width = 0

        for child in self.children:
            self._measure_child(child)

    def _measure_child(self, button: ToolButton):

        # Find max width for labels
        label_width = button.label_surface.get_rect()[2]
        if label_width > self.max_child_label_width:
            self.max_child_label_width = label_width

        # Find max width for shortcuts
        if button.shortcut is not None:
            shorcut_width = button.shortcut_surface.get_rect()[2]
            if shorcut_width > self.max_child_shortcut_width:
                self.max_child_shortcut_width = shorcut_width

    def _get_child_label_x_offset(self):
        return self.owner.string_spacer

    def _get_child_shortcut_x_offset(self):
        return self.max_child_label_width + self.owner.string_spacer * 2

    def _get_child_y_offset(self):
        return self.text_y_offset

    def _render_shortcut(self, color: str) -> pygame.Surface:
        return self.owner.font.render(self.shortcut, True, color)

    def _build_rect(self) -> pygame.rect.Rect:
        if self.parent is None:
            if self.shortcut is None:
                return super()._build_rect()
            else:
                self.label = self.label + " " + self.shortcut
                self._render_label(self.text_color)
                return super()._build_rect()

        else:
            # Default to the max width of the labels
            total_width = self.parent.max_child_label_width
            # If at least one child has a shortcut
            if self.parent.max_child_shortcut_width > 0:
                total_width += (
                    self.owner.string_spacer * 2 + self.parent.max_child_shortcut_width
                )

            text_height = max(
                # Max vertical size between the label and the shortcut
                self.label_surface.get_rect()[3],
                self.shortcut_surface.get_rect()[3],
            )

            return pygame.rect.Rect(
                self.x,
                self.y,
                total_width + 2 * self.owner.string_spacer,
                text_height * 2,
            )

    def draw(self, screen: pygame.Surface):
        if self.parent is None:
            super().draw(screen)
