"""
-- DESCRIPTION --
This scripts adds a menuBar to the root window


-- SCRIPT OVERVIEW --


-- ASSUMPTIONS --

"""

##### Imports #####
import os, re
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as msgBox

###################################################################
					       # FUNCTIONS #
###################################################################

def bestandMenu(root, menuBar, FONT):
    """Add the Bestand button to the menubar"""
    bestandMenu = Menu(menuBar, font= FONT, tearoff=0)
    menuBar.add_cascade(label='Bestand', menu=bestandMenu)
    bestandMenu.add_separator()
    bestandMenu.add_command(label='Afsluiten', command= root.quit)
    return


###################################################################
					         # MAIN #
###################################################################
def createMenuBar(root):
    """Main function to create the menu bar buttons"""

    # Add menu bar to window
    menuBar = Menu(root)
    root.config(menu = menuBar)

    # Set general layout
    FONT = "Roboto 11"

    # Create buttons
    # Bestand...
    bestandMenu(root, menuBar, FONT)

    return