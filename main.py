"""
-- DESCRIPTION --
This is the main script for the NotuleRegistratie project


-- SCRIPT OVERVIEW --


-- ASSUMPTIONS --

"""

##### Imports #####
from tkinter import *
import gui.menuBar    as guiMenuBar
import gui.mainWindow as guiMainWindow
import gui.logWindow  as guiLogWindow

###################################################################
					       # CLASSES #
###################################################################
class App(Tk):
    """Main application class"""

    def __init__(self):
        super().__init__()

        # Initialize root window
        self.title("Notule Registratie")
        self.state('zoomed')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create Menu Bar
        guiMenuBar.createMenuBar(self)

        # Get window options
        self.windowNames = self.getWindowNames()

        # Set current window
        self.currentWindow = None
        # self.switchWindow('mainWindow')
        self.switchWindow('logWindow')

    @staticmethod
    def getWindowNames():
        """Return dictionary with window class names"""
        windowNames = {
                       'mainWindow': guiMainWindow.MainWindow,
                       'logWindow':  guiLogWindow.LogWindow
                       }
        return windowNames

    def switchWindow(self, windowClassName):
        """Switch between windows based on the given className"""
        windowClass = self.windowNames[windowClassName]
        newWindow = windowClass(self)

        if self.currentWindow is not None:
            self.currentWindow.destroy()
        self.currentWindow = newWindow
        self.currentWindow.grid(row=0, column=0, sticky="nswe")

        return

###################################################################
					        # MAIN #
###################################################################
if __name__ == "__main__":
    app = App()
    app.mainloop()