class GToplevel(object):
    def __init__(self):
        from gi.repository import Gdk
        self.Widget = Gdk.Toplevel()