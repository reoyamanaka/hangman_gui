import wx, sys

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt = True)
        frame = MyFrame()
        frame.Show()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent = None, title = "Hangman Game", size = (600, 600))
        self.OnInit()
        
    def OnInit(self):
        self.panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
    def onQuit(self, event):
        sys.exit()

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
