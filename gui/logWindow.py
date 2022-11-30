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

def headTitle(master, title, FONT, rowNum=0, columnNum=0):
    """Function to create head title"""
    title = Label(master= master,
                  text  = title,
                  font  = FONT
                  )
    title.grid(row=rowNum, column=columnNum, pady=10, padx=10, sticky='nswe')
    return

###################################################################
					        # CLASS #
###################################################################


class LogWindow(Frame):
    """Log window instance"""
    FONT = "Roboto 11"
    HEADFONT = "Roboto 12 bold"

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
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Set left frame
        self.frameLeft = Frame(master=self, borderwidth=1)
        self.frameLeft.grid(row=0, column=0, sticky="nswe")

        # Set right frame
        self.frameRight = Frame(master=self)
        self.frameRight.grid(row=0, column=1, sticky="nswe")

        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # LEFT FRAME TOP - INPUT
    def createLeftFrame(self):
        """Create the input frame"""
        self.leftFrameInitialGridConfiguration()
        self.frameLeft.configure(bg='red')
        headTitle(self.frameLeft, 'LOG GEGEVENS', self.HEADFONT)

        # Create subframes for user input
        self.createLogInputFrame()
        self.createItemInputFrame()

        return

    def leftFrameInitialGridConfiguration(self):
        """Initial configuration of the left frame"""
        self.frameLeft.grid_columnconfigure(0, weight=1)
        self.frameLeft.grid_rowconfigure(0, weight=0)
        self.frameLeft.grid_rowconfigure(1, weight=0)
        self.frameLeft.grid_rowconfigure(2, weight=1)
        return
    def createLogInputFrame(self):
        """Frame to get the log input from user"""
        self.frameLogInput = Frame(master=self.frameLeft, height=400, borderwidth=1, relief=RAISED)
        self.frameLogInput.grid(row=1, column=0, padx=5, sticky='nswe')
        self.frameLogInput.configure(bg='blue')
        return
    def createItemInputFrame(self):
        """Frame to get the item input from user"""
        self.frameItemInput = Frame(master=self.frameLeft, borderwidth=1, relief=RAISED)
        self.frameItemInput.grid(row=2, column=0, padx=5, pady=5, sticky='nswe')
        self.frameItemInput.configure(bg='grey')
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # RIGHT FRAME - SETTINGS
    def createRightFrame(self):
        """Overview of the current log"""
        self.rightFrameInitialGridConfiguration()
        self.frameRight.configure(bg='green')
        headTitle(self.frameRight, 'LOG OVERZICHT', self.HEADFONT)
        self.createLogPreviewFrame()
        return

    def rightFrameInitialGridConfiguration(self):
        """Initial configuration of the right frame"""
        self.frameRight.grid_columnconfigure(0, weight=1)
        self.frameRight.grid_rowconfigure(0, weight=0)
        self.frameRight.grid_rowconfigure(1, weight=1)
        return

    def createLogPreviewFrame(self):
        """Frame to display the log data"""
        self.frameLogPreview = Frame(master=self.frameRight, borderwidth=1, relief=RAISED)
        self.frameLogPreview.grid(row=1, column=0, padx=5, pady=(0,5), sticky='nswe')
        self.frameLogPreview.configure(bg='yellow')
        return