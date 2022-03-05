from Gib.Gibox import *
from Gib.Ginet import *


class GiFile(GWindow):
    def __init__(self):
        super().__init__()
        self.HeaderBar = GHeaderBar(Title="Chooser file")
        self.SetHeaderBar(self.HeaderBar)
        self.FileDialog = GFileChooser()


class GiPad(GWindow):
    def __init__(self):
        super().__init__()
        self.SetBounds(1200, 600)

        self.HeaderBar = GHeaderBar(Title="GiPad")
        self.SetHeaderBar(self.HeaderBar)

        self.Editor_Layout = GBox(Spacing=1)
        self.Editor_Layout.SetOrientation(1)
        self.Add(self.Editor_Layout)

        self.Editor_Menu()
        self.Editor_Design()

    def NewFile(self, Widget=None):
        self.HeaderBar.SetTitle("*GiPad")
        self.HeaderBar.SetSubTitle("New file")

    def HideInfoBar(self):
        self.InfoBar.Hide()
        print("Hello")

    def Editor_Info(self):
        self.InfoBar = GInfoBar(ShowCloseButton=True)
        self.InfoBar.Event("close", self.HideInfoBar)
        self.Editor_Layout.PackStart(self.InfoBar)

    def Editor_Menu(self):
        self.Editor_MenuBar = GMenuBar()

        self.FileMenu = GMenu()
        self.FileMenuItem = GMenuItem("文件")
        self.FileMenuItem.SetSubMenu(self.FileMenu)

        self.New = GMenuItem("新建")
        self.New.Event("activate", self.NewFile)

        self.Quit = GMenuItem("退出")
        self.Quit.Event("activate", self.MainQuit)

        self.FileMenu.AddMenu(self.New)
        self.FileMenu.AddMenu(self.Quit)

        self.Editor_MenuBar.AddMenu(self.FileMenuItem)

        self.Editor_Layout.PackStart(self.Editor_MenuBar)

    def Editor_Design(self):
        self.Editor_Window = GScrolledWindow()

        self.Editor_Text = GTextView()
        self.Editor_Text.SetWrapMode(1)

        self.Editor_Window.Add(self.Editor_Text)
        self.Editor_Layout.PackEnd(self.Editor_Window, True, True)


if __name__ == "__main__":
    Ui = GiPad()
    Ui.Run()