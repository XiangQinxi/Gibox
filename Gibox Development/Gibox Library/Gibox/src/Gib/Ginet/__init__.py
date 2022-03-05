class GWebs(object):
    def OpenWebSite(self, Mode: int = 0, WebSite: str = "",
                    Browser: str = "C://Program Files//Internet Explorer//iexplore.exe"):
        if Mode == 0:
            from webbrowser import open
            open(WebSite)
        elif Mode == 1:
            from os import system
            system(f'"{Browser}" {WebSite}')

class GFiles(object):
    def __init__(self, FileName: str, Mod: str ,Encoding: str = "utf-8", ):
        self.File = open(file=FileName, encoding=Encoding)
        self.Name = self.File.name

    def Seek(self, OffSet: int = 0, Whence: int = 0):
        self.File.seek(OffSet, Whence)

    def WriteTxt(self, String: str):
        self.File.write(String)

    def WriteTxtLine(self, String: str):
        self.File.writelines(String)

    def WriteableTxt(self):
        return self.File.writable()

    def ReadTxt(self, Size: int):
        return self.File.read(n=Size)

    def ReadTxtLine(self):
        return self.File.readline()

    def ReadTxtLines(self):
        return self.File.readlines()

    def ReadableTxt(self):
        return self.File.readable()

    def Save(self):
        self.Close()

    def Close(self):
        self.File.close()
