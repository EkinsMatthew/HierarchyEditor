# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:44:04 2023

@author: Matt
"""

import pygame


class ContextItem(pygame.sprite.Sprite):
    
    def __init__(self, label, parent=None, children=None, shortcut=None):
        """
        Creates a sprite for a context menu item. These sprites are clickable 
        and offer specfic functions on each execution.

        Parameters
        ----------
        label : str
            String that appears as the text on the context menu item. All 
            ContextItems must have a label
        shortcut : str, optional
            The string expression of the shortcut for this function. The 
            default is None.
        parent : ContextItem, optional
            The higher level context item that this nests under. e.g. Open... 
            might sit under File. The default is None. If None, this 
            ContextItem belongs at the top of the menu and is always visible.
        children : list, optional
            An ordered list of the ContextItems that are below this. These will 
            be rendered when this item is clicked on. The default is None.

        Returns
        -------
        ContextItem object as constructed.

        """
        # Initialize the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Store the items that will appear on its face
        self.label = label
        self.shortcut = shortcut
        
        # Store the hierarchical information
        self.parent = parent
        
        # Keep children if provided
        if children is not None:
            self.children = children
        else:
            self.children = []
            
        # Also place the children in a group for functionality
        self.children_group = pygame.sprite.Group()
        # Fill the group
        for child in children:
            self.children_group.add(child)
        
        
    def add_child(self, sprite):
        """
        Add a sprite to the end of this one's child list.

        Parameters
        ----------
        sprite : ContextItem
            The child to be added to this children list.

        Returns
        -------
        None.

        """
        
        self.children.add(sprite)
        self.children_group.add(sprite)
        
    