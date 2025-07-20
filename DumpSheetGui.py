from tkinter import *
from tkinter import ttk
import Helpers
import clipboard as cb
import CMTS_STATS_MODEL as modelFile

class CMTS_Dump_Sheet:
    
    def __init__(self, root):

        mainframe = ttk.Frame(root, padding="30 30 120 120")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        self.outputText = StringVar()
        ttk.Button(mainframe, text="Huawei Statistics", command = self.parseStats).grid(column = 0, row = 0, sticky=W)

        statframe = ttk.Frame(mainframe)
        statframe.grid(column=0, row = 1, sticky=(N, W, E, S))
        statframe['width'] = 100
        statframe['height'] = 100
        statframe['borderwidth'] = 1
        statframe['relief'] = 'sunken'

        self.res = ttk.Entry(statframe,  textvariable=self.outputText).grid(column = 0, row = 0, sticky=(N,W,S,E))

    def parseStats(self, *args):
        self.md = modelFile.CMTS_STATS_MODEL()
        #Parse the contents of the clipboard into a dictionary format format, then construct the statframe widget from that.
        self.md.parse_from_clipboard(cb.paste())
        self.constructGui()

    def constructGui(self):
        ii = 0
        for key, value in self.md.model.items():
            keyLbl = ttk.Label(self.res, text=(key)).grid(column = 0, row = ii)
            valueLbl = ttk.Label(self.res, text=(value)).grid(column = 1, row = ii)
            ii = ii + 1



root = Tk()
CMTS_Dump_Sheet(root)
root.mainloop()
