"""
-- DESCRIPTION --
GUI of the mainWindow


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

class MainWindow(Frame):
    """Main window instance"""
    FONT = "Roboto 11"

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

        # Create the main frames - grid layout([2],[1])
        self.initialFrameAndGridConfiguration()

        # Left frame top - Table
        self.createLeftFrameTop()

        # Left frame bottom - Point preview
        self.createLeftFrameBottom()

        # Right frame - Selection options
        self.createRightFrame()

    def initialFrameAndGridConfiguration(self):
        """Function to set the initial grid configuration of the left and right frames"""
        # Row and column configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        # Set left frame - Top
        self.frameLeftTop = Frame(master=self)
        self.frameLeftTop.grid(row=0, column=0, sticky="nswe")
        self.frameLeftTop.grid_columnconfigure(0, weight=1)
        self.frameLeftTop.grid_rowconfigure(0, weight=0)
        self.frameLeftTop.grid_rowconfigure(1, weight=1)

        # Set left frame - Bottom
        self.frameLeftBottom = Frame(master=self, height=200, borderwidth=1, relief=RAISED)
        self.frameLeftBottom.grid(row=1, column=0, sticky="nswe")
        self.frameLeftBottom.grid_columnconfigure(0, weight=1)
        self.frameLeftBottom.grid_rowconfigure(0, weight=0)
        self.frameLeftBottom.grid_rowconfigure(1, weight=1)

        # Set right frame
        self.frameRight = Frame(master=self, width=200, borderwidth=1, relief=RAISED)
        self.frameRight.grid(row=0, column=1, rowspan=2, sticky="nswe")

        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # LEFT FRAME TOP - TABLE
    def createLeftFrameTop(self):
        """Create the table frame"""
        self.frameLeftTop.configure(bg='red')
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # LEFT FRAME BOTTOM - PREVIEW
    def createLeftFrameBottom(self):
        """Create the point preview frame"""
        self.frameLeftBottom.configure(bg='blue')
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # RIGHT FRAME - SETTINGS
    def createRightFrame(self):
        """Setting options to update the table"""
        self.frameRight.configure(bg='green')
        return