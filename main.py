"""
-- DESCRIPTION --
This is the main script for the NotuleRegistratie project


-- SCRIPT OVERVIEW --


-- ASSUMPTIONS --

"""

##### Imports #####
from tkinter import *
import gui.menuBar as guiMenuBar

###################################################################
					       # CLASSES #
###################################################################
class App(Tk):
    """Main application class"""

    def __init__(self):
        super().__init__()

        # Initialize root window
        self.title("Notule registratie")
        self.state('zoomed')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create Menu Bar
        guiMenuBar.createMenuBar(self)

###################################################################
					        # MAIN #
###################################################################
if __name__ == "__main__":
    app = App()
    app.mainloop()