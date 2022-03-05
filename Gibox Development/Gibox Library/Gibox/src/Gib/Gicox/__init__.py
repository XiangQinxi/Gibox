class GAciton(object):
    def __init__(self, Enabled: bool = True, Name: str = "Gib.Gicox.GAction"):
        from gi.repository import Gio
        self.Widget = Gio.Action(enabled=Enabled, name=Name)

    def SetEnabled(self, Enabled: bool):
        self.Widget.set_enabled(Enabled)

    def SetName(self, Name: str):
        self.Widget.set_name(Name)

    def Get(self):
        return self.Widget


class GApplication(object):
    def __init__(self, ApplicationId: str = "Gib.Gicox.GApplication"):
        from gi import require_version
        require_version("Gtk", "3.0")
        from gi.repository import Gio
        self.Widget = Gio.Application(application_id=ApplicationId)

    def Connect(self, ConnectName, ConnectFuction):
        self.Widget.connect(ConnectName, ConnectFuction)

    def SetApplicationId(self, ApplicationId: str):
        self.Widget.set_application_id(ApplicationId)

    def SetDefault(self):
        self.Widget.set_default()

    def SetInactivityTimeout(self, InactivityTimeout: int):
        self.Widget.set_inactivity_timeout(InactivityTimeout)

    def GetApplicationId(self):
        return self.Widget.get_application_id()

    def GetDefault(self):
        return self.Widget.get_default()

    def GetInactivityTimeout(self):
        return self.Widget.get_inactivity_timeout()

    def Activate(self):
        self.Widget.activate()

    def Quit(self):
        self.Widget.quit()

    def Run(self, Argv=None):
        self.Widget.run(Argv)

    def Hold(self):
        self.Widget.hold()

    def Release(self):
        self.Widget.release()

    def Get(self):
        return self.Widget


class GNotification(object):
    def __init__(self):
        from gi import require_version
        require_version("Gio", "2.0")
        from gi.repository import Gio
        self.Widget = Gio.Notification()

    def AddButton(self, Label: str, DetailedAction: str):
        self.Widget.add_button(label=Label, detailed_action=DetailedAction)

    def SetTitle(self, Title: str = "Title"):
        self.Widget.set_title(Title)

    def Get(self):
        return self.Widget


class GSimpleAction(GAciton):
    def __init__(self, Enabled: bool = True, Name: str = "Gib.Gicox.GAction"):
        super().__init__()
        from gi.repository import Gio
        self.Widget = Gio.SimpleAction(enabled=Enabled, name=Name)
