"""
-- DESCRIPTION --
GUI of the logWindow


-- SCRIPT OVERVIEW --


-- ASSUMPTIONS --

"""

##### Imports #####
from tkinter import *
from tkinter import ttk

###################################################################
					       # FUNCTIONS #
###################################################################


###################################################################
					        # CLASS #
###################################################################


class LogWindow(Frame):
    """Log window instance"""
    FONT = "Roboto 11"

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        # Create the main two frames - grid layout(2x1)
        self.initialFrameAndGridConfiguration()

        # Left frame - Data input
        self.createLeftFrame()

        # Right frame - Log overview
        self.createRightFrame()

    def initialFrameAndGridConfiguration(self):
        """Function to set the initial grid configuration of the left and right frame"""
        # Row and column configuration
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Set left frame
        self.frameLeft = Frame(master=self, width=200, borderwidth=1, relief=RAISED)
        self.frameLeft.grid(row=0, column=0, sticky="nswe")

        # Set right frame
        self.frameRight = Frame(master=self)
        self.frameRight.grid(row=0, column=1, sticky="nswe")

        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # LEFT FRAME TOP - INPUT
    def createLeftFrame(self):
        """Create the input frame"""
        self.frameLeft.configure(bg='red')
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # RIGHT FRAME - SETTINGS
    def createRightFrame(self):
        """Overview of the current log"""
        self.frameRight.configure(bg='green')
        return