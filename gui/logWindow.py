"""
-- DESCRIPTION --
GUI of the logWindow


-- SCRIPT OVERVIEW --


-- ASSUMPTIONS --

"""

##### Imports #####
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

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

def textBox(master, FONT, rowNum, columnNum=0, columnSpan=1, height=None):
    """Create textbox with vertical scrollbar"""
    textBox = Text(master,
                   font=FONT,
                   wrap=WORD
                   )
    scrollbar = Scrollbar(master, command=textBox.yview)
    textBox['yscrollcommand'] = scrollbar.set

    # Include height
    if height:
        textBox['height'] = height
        sticky = 'we'
    else:
        sticky = 'nswe'

    # Add items to grid
    textBox.grid(row=rowNum, column=columnNum, columnspan=columnSpan ,padx=(10,0), pady=5, sticky=sticky)
    scrollbar.grid(row=rowNum, column=columnNum+columnSpan, padx=(0,10), pady=5, sticky='nswe')

    return textBox

def entryBox(master, labelText, FONT, rowNum, columnNum=0):
    """Add entryBox to master"""
    label = Label(master=master, text=labelText, font=FONT, anchor=N)
    label.grid(row=rowNum, column=columnNum, padx=(10, 0), pady=2, sticky='w')
    entryBox = Entry(master,
                     font=FONT
                     )
    entryBox.grid(row=rowNum, column=columnNum+1, padx=(0,3), pady=2, sticky='we')
    return

def dropdownBox(master, labelText, inputList, FONT, rowNum, columnNum=0):
    """Create dropdownBox including label"""
    label = Label(master=master, text=labelText, font=FONT, anchor=N)
    label.grid(row=rowNum, column=columnNum, padx=(10, 0), pady=2, sticky='w')
    drop = ttk.Combobox(master, value=inputList)
    drop.current(0)
    drop.grid(row=rowNum, column=columnNum+1, pady=2, sticky='w')
    return

def plusButton(master, rowNum, command, columnNum=2):
    """Add a plus button to the master frame"""
    iconOpenFolder = ImageTk.PhotoImage(Image.open('icons\icon_plus.png'))
    openButton = Button(master, image=iconOpenFolder, command=command)
    openButton.image = iconOpenFolder
    openButton.grid(row=rowNum, column=columnNum, padx=(0, 3), pady=3)
    openButton.configure(state="normal")
    return

###################################################################
					        # CLASS #
###################################################################

class LogWindow(Frame):
    """Log window instance"""
    FONT = "Roboto 10"
    TEXTBOXFONT = "Roboto 10"
    HEADER_1_FONT = "Roboto 12 bold"
    HEADER_3_FONT = "Roboto 10 bold"

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
        headTitle(self.frameLeft, 'LOG GEGEVENS', self.HEADER_1_FONT)

        # Create subframes for user input
        self.createLogInputFrame()
        self.createItemInputFrame()
        self.createButtonFrame()

        return

    def leftFrameInitialGridConfiguration(self):
        """Initial configuration of the left frame"""
        self.frameLeft.grid_columnconfigure(0, weight=1)
        self.frameLeft.grid_rowconfigure(0, weight=0)
        self.frameLeft.grid_rowconfigure(1, weight=0)
        self.frameLeft.grid_rowconfigure(2, weight=1)
        self.frameLeft.grid_rowconfigure(3, weight=0)
        return

    def createLogInputFrame(self):
        """Frame to get the log input from user"""
        self.frameLogInput = Frame(master=self.frameLeft, borderwidth=1, relief=RAISED)
        self.frameLogInput.grid(row=1, column=0, padx=5, sticky='nswe')
        self.logInputFrameInitialGridConfiguration()
        logRowNum = 0

        # Add Title
        label = Label(master=self.frameLogInput, text='Nieuw log', font=self.HEADER_3_FONT)
        label.grid(row=logRowNum, column=0, columnspan=2, pady=(6, 2), padx=10, sticky='w')
        logRowNum += 1

        entryBox(self.frameLogInput, 'Log titel:', self.TEXTBOXFONT, logRowNum)

        plusButton(self.frameLogInput, logRowNum, command=lambda: print('test'))
        logRowNum += 1
        entryBox(self.frameLogInput, 'Datum:', self.TEXTBOXFONT, logRowNum)
        logRowNum += 1
        Label(master=self.frameLogInput, text='Aanwezig', font=self.TEXTBOXFONT).grid(row=logRowNum, column=0, pady=2, padx=10)
        logRowNum += 1
        textBox(self.frameLogInput, self.TEXTBOXFONT, logRowNum, height=5, columnSpan=2)
        return

    def logInputFrameInitialGridConfiguration(self):
        """Initial configuration of the log input frame"""
        self.frameLogInput.grid_columnconfigure(0, weight=0)
        self.frameLogInput.grid_columnconfigure(1, weight=1)
        self.frameLogInput.grid_rowconfigure(0, weight=1)
        self.frameLogInput.grid_rowconfigure(5, weight=1)
        return

    def createItemInputFrame(self):
        """Frame to get the item input from user"""
        self.frameItemInput = Frame(master=self.frameLeft, borderwidth=1, relief=RAISED)
        self.frameItemInput.grid(row=2, column=0, padx=5, pady=5, sticky='nswe')
        self.itemInputFrameInitialGridConfiguration()
        inputRowNum = 0

        # Add Title
        label = Label(master=self.frameItemInput, text='Onderwerp', font=self.HEADER_3_FONT)
        label.grid(row=inputRowNum, column=0, columnspan=2, pady=(6, 2), padx=10, sticky='w')
        inputRowNum += 1

        # Add buttons
        self.frameItemButtons = Frame(master=self.frameItemInput)
        self.frameItemButtons.grid(row=inputRowNum, column=0, padx=5, pady=(0, 5), sticky='nswe')
        Button(self.frameItemButtons, text='Save').grid(row=0, column=0, padx=(10,0))
        Button(self.frameItemButtons, text='Delete').grid(row=0, column=1, padx=10)
        inputRowNum += 1

        # Add type option
        itemTypes = ['Informatie', 'Definitie', 'Datum']
        dropdownBox(self.frameItemInput, 'Type:', itemTypes, self.TEXTBOXFONT, inputRowNum)
        inputRowNum += 1

        # Add title and keyword input
        entryBox(self.frameItemInput, 'Titel:', self.TEXTBOXFONT, inputRowNum)
        plusButton(self.frameItemInput, inputRowNum, command=lambda: print('test'))
        inputRowNum += 1
        entryBox(self.frameItemInput, 'Trefwoorden:', self.TEXTBOXFONT, inputRowNum)
        plusButton(self.frameItemInput, inputRowNum, command=lambda: print('test'))
        inputRowNum += 1

        # Issue description
        label = Label(master=self.frameItemInput, text='Omschrijving', font=self.HEADER_3_FONT)
        label.grid(row=inputRowNum, column=0, columnspan=2, pady=(6, 2), padx=10, sticky='w')
        inputRowNum += 1
        textBox(self.frameItemInput, self.TEXTBOXFONT, inputRowNum,columnSpan=2)

        return

    def itemInputFrameInitialGridConfiguration(self):
        """Initial configuration of the right frame"""
        self.frameItemInput.grid_columnconfigure(0, weight=0)
        self.frameItemInput.grid_columnconfigure(1, weight=1)
        self.frameItemInput.grid_rowconfigure(0, weight=0)
        self.frameItemInput.grid_rowconfigure(6, weight=1)
        return

    def createButtonFrame(self):
        """Create the bottom frame to hold the general buttons"""
        self.frameButtons = Frame(master=self.frameLeft)
        self.frameButtons.grid(row=3, column=0, padx=5, pady=(0,5), sticky='nswe')
        Button(self.frameButtons, text='Save log').grid(row=0, column=0, padx=(10,0))
        Button(self.frameButtons, text='Delete log').grid(row=0, column=1, padx=10)
        Button(self.frameButtons, text='Cancel').grid(row=0, column=2)
        return

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # RIGHT FRAME - SETTINGS
    def createRightFrame(self):
        """Overview of the current log"""
        self.rightFrameInitialGridConfiguration()
        headTitle(self.frameRight, 'LOG OVERZICHT', self.HEADER_1_FONT)
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
        self.logPreviewFrameInitialGridConfiguration()
        self.preview = textBox(self.frameLogPreview, self.TEXTBOXFONT, 0)
        self.preview.config(state=DISABLED)
        return

    def logPreviewFrameInitialGridConfiguration(self):
        """Initial configuration of the right frame"""
        self.frameLogPreview.grid_columnconfigure(0, weight=1)
        self.frameLogPreview.grid_rowconfigure(0, weight=1)
        return