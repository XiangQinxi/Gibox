# Gicox
# -------------------------------------------------------------
from Gib import Gicox


class GObject(object):
    def __init__(self):
        self.EventId = None
        from gi.repository import GObject
        self.Widget = GObject.Object()

    def Event(self, BindName: str, BindFunc):
        self.EventId = self.Widget.connect(BindName, BindFunc)


class GAttribute(object):
    def __init__(self):
        pass


class GOrientable(object):
    def __init__(self):
        from gi.repository import Gtk
        self.Widget = None

    def SetOrientation(self, Orientation: int = 0):
        self.Widget.set_orientation(orientation=Orientation)

    def GetOrientation(self):
        return self.Widget.get_orientation()


class GWidget(GObject, GOrientable):
    def __init__(self):
        super().__init__()
        self.Init()

        self.Widget = None

    def Init(self):
        import gi
        gi.require_version("Gtk", "3.0")

    def Remove(self, Widget: GObject):
        self.Widget.remove(widget=Widget.Get())

    def Add(self, Widget: GObject):
        self.Widget.add(widget=Widget.Get())

    def SetVersion(self, Version: float = 3.0):
        from gi import require_version
        require_version("Gtk", str(Version))

    def GetChildren(self):
        return self.Widget.get_children()

    def DoRemove(self):
        self.Widget.do_remove()

    def DoAdd(self):
        self.Widget.do_add(widget)

    def Activated(self):
        self.Widget.activate()

    def Destroy(self):
        self.Widget.destroy()

    def DoDestroy(self):
        self.Widget.do_destroy()

    def DoDestroyEvent(self, event):
        self.Widget.do_destroy_event(event=event)

    def DeleteWindow(self, Window):
        self.Widget.unregister_window(window=Window.Get())

    def DoPressButton(self):
        self.Widget.do_button_press_event()

    def DoReleaseButton(self):
        self.Widget.do_button_release_event()

    def GetMarginLeft(self):
        self.Widget.get_margin_start()

    def GetMarginRight(self):
        self.Widget.get_margin_end()

    def GetMarginTop(self):
        self.Widget.get_margin_top()

    def GetMarginBottom(self):
        self.Widget.get_margin_bottom()

    def Show(self):
        self.Widget.show()

    def ShowAll(self):
        self.Widget.show_all()

    def ShowNow(self):
        self.Widget.show_now()

    def DoShow(self):
        self.Widget.do_show()

    def DoShowAll(self):
        self.Widget.do_show_all()

    def Hide(self):
        self.Widget.hide()

    def DoHide(self):
        self.Widget.do_hide()

    def SetID(self, ID: int or None):
        self.Widget.set_id(id=ID)

    def SetWigdet(self, Widget: GObject):
        self.Widget = Widget.Get()

    def SetStateFlags(self, Flags, Clear: bool = False):
        self.Widget.set_state_flags(flags=Flags, clear=Clear)

    def SetStateNORMAL(self):
        self.SetStateFlags("NORMAL")

    def SetStateACTIVE(self):
        self.SetStateFlags("ACTIVE")

    def SetRilief(self, Rilief: int):
        self.Widget.set_relief(Rilief)

    def SetParent(self, Parent):
        self.Widget.set_parent(parent=Parent.Get())

    def SetParentWindow(self, ParentWindow):
        self.Widget.set_parent_window(parent_window=ParentWindow.Get())

    def SetResizable(self, Resizable: bool):
        self.Widget.set_resizable(Resizable)

    def SetDefaultSize(self, Width: int, Height: int):
        self.Widget.set_default_size(Width, Height)

    def SetDefaultWidth(self, Width: int):
        self.SetDefaultSize(Width=Width, Height=self.GetDefaultSize()[1])

    def SetDefaultHeight(self, Height: int):
        self.SetDefaultSize(Width=self.GetDefaultSize()[0], Height=Height)

    def SetAngle(self, Angle: int):
        self.Widget.set_angle(Angle)

    def SetAlpha(self, Alpha: float):
        self.Widget.set_opacity(opacity=Alpha)

    def SetMiniSize(self, Width: int, Height: int):
        self.Widget.set_size_request(width=Width, height=Height)

    def SetToolTip(self, Text: str):
        self.Widget.set_tooltip_text(text=Text)

    def SetToolMarkup(self, IconPos: int = 0, ToolTip: str = ""):
        self.Widget.set_icon_tooltip_markup(icon_pos=IconPos, tooltip=ToolTip)

    def SetToolTipWindow(self, Window):
        self.Widget.set_tooltip_window(custom_window=Window.Get())

    def SetName(self, Name: str):
        self.Widget.set_name(name=Name)

    def GetName(self):
        """
        :return: int
        """
        self.Widget.get_name()

    def GetAlpha(self):
        return self.Widget.get_opacity()

    def GetResizable(self):
        return self.Widget.get_resizable()

    def GetDefaultSize(self):
        return self.Widget.get_default_size()

    def GetRelief(self):
        return self.Widget.get_relief()

    def AddEvent(self, Func):
        self.Widget.connect("add", Func)

    def Get(self):
        return self.Widget


class GAppChooser(GObject):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.AppChooser()

    def Init(self):
        from gi import require_version
        require_version("Gtk", "3.0")

    def SetVersion(self, Version: float = 3.0):
        from gi import require_version
        require_version("Gtk", str(Version))

    def GetAppInfo(self):
        return self.Widget.get_app_info()

    def GetContentType(self):
        return self.Widget.get_content_type()

    def Refresh(self):
        self.Widget.refresh()


# GCore
# -------------------------------------------------------------
class GApplication(Gicox.GApplication):
    def __init__(self, ApplicationId: str = "Gib.GContainer.GApplication"):
        super().__init__()
        self.Init()

        from gi.repository import Gtk

        self.Widget = Gtk.Application(application_id=ApplicationId)

    def SetVersion(self, Version: float = 3.0):
        from gi import require_version
        require_version("Gtk", str(Version))

    def Init(self):
        self.SetVersion(3.0)

    def Get(self):
        return self.Widget

    def MainLoop(self, MainFunc):
        self.Widget.connect('activate', MainFunc)

    def AddWindow(self, Window: GWidget):
        self.Widget.add_window(window=Window)


class GWindowPos(GAttribute):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.WindowPosition()
        self.NONE = self.Widget.NONE
        self.CENTER = self.Widget.CENTER
        self.MOUSE = self.Widget.MOUSE
        self.CENTER_ALWAYS = self.Widget.CENTER_ALWAYS
        self.CENTER_ON_PARENT = self.Widget.CENTER_ON_PARENT


class GWindowType(GAttribute):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.WindowType()
        self.TOPLEVEL = 0
        self.POPUP = 1


class GAppChooserWidget(GAppChooser):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.AppChooserWidget()

    def GetDefaultText(self):
        return self.Widget.get_default_text()

    def GetShowDefault(self):
        return self.Widget.get_show_default()

    def GetShowAll(self):
        return self.Widget.get_show_all()

    def GetShowFallback(self):
        return self.Widget.get_show_fallback()

    def GetShowOther(self):
        return self.Widget.get_show_other()

    def GetShowRecommended(self):
        return self.Widget.get_show_recommended()

    def SetDefaultText(self):
        return self.Widget.set_default_text()

    def SetShowDefault(self):
        return self.Widget.set_show_default()

    def SetShowAll(self):
        return self.Widget.set_show_all()

    def SetShowFallback(self):
        return self.Widget.set_show_fallback()

    def SetShowOther(self):
        return self.Widget.set_show_other()

    def SetShowRecommended(self):
        return self.Widget.set_show_recommended()


class GFileChooser(GObject):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.FileChooser()

    def AddChoice(self, Id, Label, Option, OptionLabel):
        pass

    def Init(self):
        from gi import require_version
        require_version("Gtk", "3.0")


class GIcon(GObject):
    def __init__(self, Icon):
        super().__init__()
        self.Init()
        from gi.repository import Gio
        self.Widget = Gio.Icon(Icon)

    def Init(self):
        from gi import require_version
        require_version("Gtk", "3.0")


class GImage(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Image()

    def SetIcon(self, IconName: str or None, Size: int):
        self.Widget.set_from_icon_name(icon_name=IconName, size=Size)

    def SetIconFile(self, IconFile: str or None):
        self.Widget.set_from_resource(resource_path=IconFile)

    def Get(self):
        return self.Widget


class GBind(GObject):
    def __init__(self):
        super().__init__()
        self.Clicked = "clicked"
        self.Activate = "activate"
        self.Enter = "enter"
        self.Leave = "leave"
        self.Pressed = "pressed"
        self.Released = "released"
        self.Swich_Acitvate = "activate"
        self.Swich_State = "state-set"


class GColor(GObject):
    def __init__(self, Red: float = 1.0, Green: float = 1.0, Blue: float = 1.0, Alpha: float = 1.0):
        super().__init__()
        from gi.repository import Gdk

        self.Widget = Gdk.RGBA(red=Red, green=Green, blue=Blue, alpha=Alpha)


class GButtonBoxLayout(GAttribute):
    def __init__(self):
        super().__init__()
        self.SPREAD = 1
        self.EDGE = 2
        self.START = 3
        self.END = 4
        self.CENTER = 5
        self.EXPAND = 6


class GPosition(GAttribute):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.LEFT = 0
        self.RIGHT = 1
        self.TOP = 2
        self.BOTTOM = 3

    def Init(self):
        from gi import require_version
        require_version("Gtk", "3.0")


class GEditable(GObject):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = None

    def Init(self):
        from gi import require_version
        require_version("Gtk", "3.0")

    def Copy(self):
        self.Widget.copy_clipboard()

    def Cut(self):
        self.Widget.cut_clipboard()

    def DeleteSelectionText(self):
        self.Widget.delete_selection()

    def DeleteText(self, Start: int, End: int):
        self.Widget.delete_text(start_pos=Start, end_pos=End)

    def GetChars(self, Start: int, End: int):
        return self.Widget.get_chars(start_pos=Start, end_pos=End)

    def GetEditable(self):
        return self.Widget.get_editable()

    def GetPosition(self):
        return self.Widget.get_position()

    def GetSelectPosition(self):
        return self.Widget.get_selection_bounds()

    def Get(self):
        return self.Widget

    def InsertText(self, Text: str, Pos: int):
        self.Widget.insert_text(text=Text, position=Pos)


class GEllipsizeMode(GAttribute):
    def __init__(self):
        super().__init__()
        self.NONE = 0
        self.START = 1
        self.MIDDLE = 2
        self.END = 3


class GShadowType(GAttribute):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.ShadowType()
        self.NONE = self.Widget.NONE
        self.IN = self.Widget.IN
        self.OUT = self.Widget.OUT
        self.ETCHED_IN = self.Widget.ETCHED_IN
        self.ETCHED_OUT = self.Widget.ETCHED_OUT


# GContainers
# -------------------------------------------------------------
class GWindow(GWidget):
    def __init__(self, Title: str = "Gib.GContainer.GWindow", Application: GApplication = None,
                 Type: GWindowType or int = 0):
        super().__init__()
        self.Init()

        from gi.repository import Gtk

        self.Widget = Gtk.Window(title=Title, application=Application, type=Type)
        self.SetDefaultBounds(450, 200)

    def Init(self):
        from gi import require_version
        require_version("Gtk", "3.0")

    def Move(self, X: int, Y: int):
        self.Widget.move(x=X, y=Y)

    def Maximize(self):
        self.Widget.maximize()

    def IfMaximize(self):
        return self.Widget.is_maximized()

    def Present(self):
        self.Widget.present()

    def SetTitle(self, Title: str):
        self.Widget.set_title(Title)

    def SetSize(self, X: int, Y: int):
        self.Widget.move(x=X, y=Y)

    def SetDecorated(self, Setting: bool):
        self.Widget.set_decorated(setting=Setting)

    def SetBounds(self, Width: int, Height: int):
        self.Widget.resize(width=Width, height=Height)

    def SetHeaderBar(self, TitleBar: GWidget):
        self.Widget.set_titlebar(titlebar=TitleBar.Get())

    def SetStartupID(self, StartID: str):
        self.Widget.set_startup_id(startup_id=StartID)

    def SetWindowPos(self, Pos: GWindowPos or int):
        self.Widget.set_position(position=Pos)

    def SetIcon(self, IconName: str):
        self.Widget.set_icon_name(name=IconName)

    def SetApplication(self, Application: GApplication or None):
        self.Widget.set_application(Application)

    def SetDeleteWindowButton(self, Setting: bool):
        self.Widget.set_deletable(Setting)

    def SetIconFile(self, IconFile: str):
        self.Widget.set_icon_from_file(filename=IconFile)

    def SetDefaultBounds(self, Width: int, Height: int):
        self.Widget.set_default_size(Width, Height)

    def SetDefaultWidget(self, DefaultWidget=None):
        self.Widget.set_default_widget(DefaultWidget)

    def SetDeleltButton(self, DeleltButton: bool):
        self.Widget.set_deletable(DeleltButton)

    def SetDestroyWithParent(self, DestroyWithParent: bool):
        self.Widget.set_destroy_with_parent(setting=DestroyWithParent)

    def SetUnMaximize(self):
        self.Widget.unmaximize()

    def SetStartID(self, StartId):
        self.Widget.set_startup_id(startup_id=StartId)

    def SetSkipTaskbarHint(self, SkipTaskbarHint: bool):
        self.Widget.set_skip_taskbar_hint(setting=SkipTaskbarHint)

    def GetHeaderBar(self):
        return self.Widget.get_titlebar()

    def GetDefaultBounds(self):
        return self.Widget.get_default_size()

    def GetDeleteButton(self):
        return self.Widget.get_deletable()

    def GetPosition(self):
        return self.Widget.get_position()

    def GetBounds(self):
        return self.Widget.get_size()

    def Close(self):
        self.Widget.close()

    def MainLoop(self, Widget=None):
        from gi.repository import Gtk
        Gtk.main()

    def MainQuit(self, Widget=None):
        from gi.repository import Gtk
        Gtk.main_quit()

    def Run(self):
        from gi.repository import Gtk

        self.Event("delete-event", Gtk.main_quit)
        self.ShowAll()
        Gtk.main()


class OffscreenWindow(GWindow):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.OffscreenWindow()

    def GetPixbuf(self):
        return self.Widget.get_pixbuf()

    def GetSurface(self):
        return self.Widget.get_surface()


class GDialog(GWindow):
    def __init__(self, Title: str = "Gib.GContainer.GWindow", Application: GApplication = None):
        super().__init__()
        self.Init()

        from gi.repository import Gtk

        self.Widget = Gtk.Dialog(title=Title, application=Application)
        self.SetBounds(450, 200)

    def Response(self, ID: int):
        self.Widget.response(response_id=ID)

    def AddActionWidget(self, Widget: GWidget, ID: int):
        self.Widget.add_action_widget(child=Widget.Get(), response_id=ID)

    def AddButton(self, Text: str, ID: int):
        self.Widget.add_button(button_text=Text, response_id=ID)


class GAboutDialog(GDialog):
    def __init__(self):
        super().__init__(self)
        self.Init()

        from gi.repository import Gtk
        self.Widget = Gtk.AboutDialog()

    def SetAuthors(self, Authors: str or None):
        self.Widget.set_authors(authors=Authors)

    def SetNotes(self, Notes: str or None):
        self.Widget.set_comments(comments=Notes)

    def SetCopyright(self, Copyright: str or None):
        self.Widget.set_copyright(copyright=Copyright)

    def SetDocumenters(self, Documenters: str or None):
        self.Widget.set_documenters(documenters=Documenters)

    def SetLicense(self, License: str or None):
        self.Widget.set_license(license=License)

    def SetLicenseType(self, LicenseType: str or None):
        self.Widget.set_license_type(license_type=LicenseType)

    def SetProgramName(self, Name: str):
        self.Widget.set_program_name(name=Name)

    def SetWebsite(self, Website: str or None):
        self.Widget.set_website(website=Website)

    def SetWebsiteLabel(self, WebsiteLabel: str or None):
        self.Widget.set_website_label(website_label=WebsiteLabel)


class GAppChooserDialog(GAppChooser):
    def __init__(self):
        super().__init__(self)
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.AppChooserDialog()

    def GetHeading(self):
        return self.Widget.get_heading

    def GetWidget(self):
        return self.Widget.get_widget()

    def SetHeading(self, Title):
        self.Widget.set_heading(heading=Title)


class GFileChooserDialog(GDialog):
    def __init__(self, Title: str = "Gib.Gibox.GAppChooserDialog", Application: GApplication = None):
        super().__init__(self)
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.FileChooserDialog(Title, self,
                                            Gtk.FileChooserAction.OPEN,
                                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))


class GApplicationWindow(GWindow):
    def __init__(self, Title: str = "Gib.GContainer.GWindow", Size=(450, 200), Application=None):
        super().__init__(self)
        self.Init()

        from gi.repository import Gtk

        self.Widget = Gtk.Application(application=Application)

    def Run(self):
        self.Widget.run(None)

    def Present(self):
        self.Widget.present()

    def Add(self, Widget):
        self.Widget.set_child(Widget)

    def AddWindow(self, Window: GWindow):
        self.Widget.add_window(window=Window)


class GFrame(GWidget):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.Frame()

    def SetLabel(self, Label: str):
        self.Widget.set_label(Label)

    def SetLabelWidget(self, LabelWidget: GWidget):
        self.Widget.set_label_widget(LabelWidget)

    def SetLabelAlign(self, Xalign: float, Yalign: float):
        self.Widget.set_label_align(xalign=Xalign, yalign=Yalign)

    def SetShadow(self, Shadow: GShadowType or int):
        self.Widget.set_shadow_type(Shadow)

    def GetLabel(self):
        return self.Widget.get_label()

    def GetLabelWidget(self):
        return self.Widget.get_label_widget()

    def GetLabelAlign(self):
        return self.Widget.get_label_align()

    def GetShadow(self):
        return self.Widget.get_shadow_type()


class GBox(GWidget):
    def __init__(self, Spacing: int = 0):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Box(spacing=Spacing)

    def PackStart(self, Widget: GWidget, Expand: bool = False, Fill: bool = False, Padding: int = 0):
        self.Widget.pack_start(child=Widget.Get(), expand=Expand, fill=Fill, padding=Padding)

    def PackEnd(self, Widget: GWidget, Expand: bool = False, Fill: bool = False, Padding: int = 0):
        self.Widget.pack_end(child=Widget.Get(), expand=Expand, fill=Fill, padding=Padding)


class GHBox(GBox):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.HBox()


class GVBox(GBox):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.VBox()


class GButtonBox(GBox):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.ButtonBox()

    def SetChildNonHomogeneous(self, Child: GWidget, NonHomogeneous: bool):
        self.Widget.set_child_non_homogeneous(child=Child, non_homogeneous=NonHomogeneous)

    def SetChildSecondary(self, Child, IsSecondary: bool):
        self.Widget.set_child_secondary(Child, is_secondary=IsSecondary)

    def SetLayout(self, ButtonBoxLayout: GButtonBoxLayout or int):
        self.Widget.set_layout(layout_style=ButtonBoxLayout)

    def GetChildNonHomogeneous(self, Child: GWidget):
        return self.Widget.get_child_non_homogeneous(child=Child.Get())

    def GetChildSecondary(self, Child: GWidget):
        return self.Widget.get_child_secondary(child=Child.Get())

    def GetLayout(self):
        return self.Widget.get_layout()


class GPaned(GWidget):
    def __init__(self, Pos: int = 0, PosSet: bool = True):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.Paned(position=Pos, position_set=PosSet)

    def AddLeft(self, Widget: GWidget or None):
        self.Widget.add1(Widget.Get())

    def AddRight(self, Widget: GWidget or None):
        self.Widget.add2(Widget.Get())

    def PackLeft(self, Widget, Resize: bool = False, Shrink: bool = False):
        self.Widget.pack1(child=Widget, resize=Resize, shrink=Shrink)

    def PackRight(self, Widget, Resize: bool = False, Shrink: bool = False):
        self.Widget.pack2(child=Widget, resize=Resize, shrink=Shrink)

    def SetPosition(self, Pos: int):
        self.Widget.set_position(Pos)

    def GetLeft(self):
        return self.Widget.get_child1()

    def GetRight(self):
        return self.Widget.get_child2()

    def GetPosition(self):
        return self.Widget.get_position()


class Grid(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Grid()

    def Attach(self, Widget: GWidget, Left: int, Top: int, Width: int, Height: int):
        self.Widget.attach(child=Widget.Get(), left=Left, top=Top, width=Width, height=Height)

    def AttchNextTo(self, Child: GWidget, Sibling: GWidget or None, Side: GPosition, Width: int, Height: int):
        self.Widget.attach_next_to(child=Child, sibling=Sibling, side=Side, width=Width, height=Height)

    def GetWidget(self, Left: int, Top: int):
        return self.Widget.get_child_at(left=Left, top=Top)

    def GetColumnSpacing(self):
        return self.Widget.get_column_spacing()


class GNoteBook(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Notebook()

    def AddPage(self, Widget: GWidget or None, Label: GWidget):
        self.Widget.append_page(child=Widget.Get(), tab_label=Label.Get())

    def AddPages(self, Widget: GWidget or None, Label: str = "Gib.GWidgets.GNoteBook"):
        from gi.repository import Gtk
        self.Widget.append_page(child=Widget.Get(), tab_label=Gtk.Label(label=Label))

    def AddPageMenu(self, Widget: GWidget or None, Label: GWidget,
                    MenuLabel: str = "Gib.GWidgets.GNoteBook"):
        self.Widget.append_page_menu(child=Widget.Get(), tab_label=Label.Get(), menu_label=MenuLabel)

    def SetPos(self, Position: GPosition or int = 2):
        self.Widget.set_tab_pos(Position)

    def SetPageDetachable(self, Widget: GWidget, Detachable: bool):
        self.Widget.set_tab_detachable(Widget.Get(), Detachable)

    def SetPageLabel(self, Widget: GWidget, Label: str):
        self.Widget.set_menu_label(child=Widget.Get(), menu_label=Label)

    def SetPageShow(self, Value: bool):
        self.Widget.set_show_tabs(show_tabs=Value)

    def SetScrollable(self, Value: bool):
        self.Widget.set_scrollable(scrollable=Value)

    def GetPos(self):
        return self.Widget.get_tab_pos()

    def RemovePage(self, Page: int = 0):
        self.Widget.remove_page(page_num=Page)

    def DeletePage(self, Widget: GWidget):
        self.Widget.detach_tab(child=Widget.Get())


class GFixed(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Fixed()

    def Put(self, Widget: GWidget, X: int, Y: int):
        self.Widget.put(widget=Widget, x=X, y=Y)

    def Move(self, Widget: GWidget, X: int, Y: int):
        self.Widget.move(widget=Widget, x=X, y=Y)


class GOverlay(GWidget):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.Overlay()

    def AddOverlay(self, Widget: GWidget):
        self.Widget.add_overlay(Widget)


# GModule
# -------------------------------------------------------------
class GDate(object):
    def __init__(self):
        self.Date = dict()

    def AddDate(self, DateName, DateValue):
        self.Date[DateName] = DateValue

    def SetDate(self, DateName, DateValue):
        self.AddDate(DateName, DateValue)

    def GetDate(self, DateName):
        return self.Date[DateName]


class GProject(object):
    def __init__(self):
        self.Date = GDate()

    def AddWindow(self, WindowId, Window: GWindow):
        self.Date.AddDate(DateName=WindowId, DateValue=Window)

    def SetWindow(self, WindowId, Window: GWindow):
        self.Date.SetDate(DateName=WindowId, DateValue=Window)

    def GetWindow(self, WindowId):
        return self.Date.GetDate(DateName=WindowId)

    def RunWindow(self, WindowId):
        Window = self.GetWindow(WindowId)
        return Window.Get()


class GBuilder(object):
    def __init__(self):
        from gi import require_version
        require_version("Gtk", "3.0")
        from gi.repository import Gtk

        self.Window = None
        self.Widget = Gtk.Builder()

    def AddFile(self, File):
        self.Widget.add_from_file(File)

    def AddString(self, String: str):
        self.Widget.add_from_string(String)

    def SetApplication(self, Application: GApplication):
        self.Widget.set_application(Application.Get())

    def GetObject(self, Object: str):
        return self.Widget.get_object(Object)

    def Get(self):
        return self.Widget

    def GetObjectList(self):
        return self.Widget.get_objects()

    def Run(self, WindowID):
        from gi.repository import Gtk

        self.Window = self.GetObject(WindowID)
        self.Window.show_all()
        self.Window.connect("delete-event", Gtk.main_quit)

        Gtk.main()

    def HandleBind(self, Class):
        self.Widget.connect_signals(Class)


# GWidgets
# -------------------------------------------------------------
class GLabel(GWidget):
    def __init__(self, Text: str = "Gib.Control.GLabel", Version: float = 3.0):
        super().__init__()
        self.SetVersion(Version)
        from gi.repository import Gtk
        self.Widget = Gtk.Label()
        self.SetText(Text)

    def SetText(self, Text: str):
        self.Widget.set_label(Text)

    def SetSelectable(self, Value: bool):
        self.Widget.set_selectable(Value)

    def GetText(self):
        return self.Widget.get_label()


class GEntry(GEditable):
    def __init__(self, Text: str = "Gib.Gibox.GEntry", Editable: bool = True, EnableEmojiCompletion: bool = False,
                 ShowEmojiIcon: bool = False):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Entry(text=Text, editable=Editable, enable_emoji_completion=EnableEmojiCompletion,
                                show_emoji_icon=ShowEmojiIcon)

    def SetText(self, Text: str):
        self.Widget.set_text(Text)

    def SetProgress(self, Value: int):
        self.Widget.set_progress_pulse_step(fraction=Value)

    def SetEnableEmojiCompletion(self, EnableEmojiCompletion: bool = False):
        self.Widget.set_enable_emoji_completion(EnableEmojiCompletion)

    def SetIcon(self, Icon: str or None = None, IconPos: int = 0):
        self.Widget.set_icon_from_gicon(icon_pos=IconPos, icon=Icon)

    def GetText(self):
        return self.Widget.get_text()

    def GetProgress(self):
        return self.Widget.get_progress_pulse_setp()

    def GetTextLength(self):
        return self.Widget.get_text_length()

    def GetIcon(self, IconPos: int = 0):
        self.Widget.get_icon_gicon(icon_pos=IconPos)


class SearchEntry(GEntry):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.SearchEntry()


class GSwitch(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Switch()

    def SetActive(self, Active: bool):
        self.Widget.get_active(is_state=Active)

    def SetState(self, State: bool):
        self.Widget.set_state(state=State)

    def DoActivate(self):
        self.Widget.do_activate()

    def GetActive(self):
        return self.Widget.get_active()

    def GetState(self):
        return self.Widget.get_state()


class GComboBox(GWidget):
    def __init__(self, Model: str = "<<Option>>", Additional: GWidget = None):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.ComboBox()

    def GetTearOffTitle(self):
        self.Widget.get_title()

    def SetTearOffTitle(self, Title: str = "Gib.GControl.GComboBox"):
        self.Widget.set_title(title=Title)

    def HidePop(self):
        self.Widget.popdown()

    def Popup(self):
        self.Widget.popup()


class GComboBoxText(GComboBox):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.ComboBoxText()


class GPopover(GComboBox):
    def __init__(self, Modal: bool = False, Position: GPosition or int = 3):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Popover(modal=Modal, position=Position)

    def SetConstrain(self, Constraint: int):
        self.Widget.set_constrain_to(Constraint)

    def SetPosition(self, Position: GPosition or int = 3):
        self.Widget.set_position(position=Position)

    def SetModal(self, Modal: bool):
        self.Widget.set_modal(modal=Modal)

    def GetConstrain(self):
        return self.Widget.get_constrain_to()

    def GetPosition(self):
        return self.Widget.get_position()

    def GetModal(self):
        return self.Widget.get_modal()


class GPopoverMenu(GPopover):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.PopoverMenu()

    def OpenSubmenu(self, Name: str):
        self.Widget.open_submenu(name=Name)


class GButton(GWidget):
    def __init__(self, Label: str = "Gib.GControl.GButton", Relief: int = 0, Version: float = 3.0):
        super().__init__()
        self.SetVersion(Version)
        from gi.repository import Gtk
        self.Widget = Gtk.Button(label=Label, relief=Relief)

    def SetLabel(self, Label: str):
        self.Widget.set_label(Label)

    def SetShortcutKeyWithLabel(self, Label: str):
        self.Widget.new_with_mnemonic(label="_" + Label)

    def SetImage(self, Image: GWidget or None):
        self.Widget.set_image(image=Image.Get())

    def SetImagePos(self, Pos: GPosition):
        self.Widget.set_image_position(Pos)

    def SetRelief(self, Relief: int = 0):
        self.Widget.set_relief(relief=Relief)

    def SetAlwaysShowImage(self, AlwaysShow: bool):
        self.Widget.set_always_show_image(always_show=AlwaysShow)

    def GetLabel(self):
        return self.Widget.get_label()

    def GetIcon(self):
        """Gtk 4.X"""
        return self.Widget.set_icon_name(icon_name)

    def Click(self, EventFunc):
        self.Widget.connect("clicked", EventFunc)

    def Activate(self, EventFunc):
        self.Widget.connect("activate", EventFunc)

    def Enter(self, EventFunc):
        self.Widget.connect("enter", EventFunc)

    def Leave(self, EventFunc):
        self.Widget.connect("leave", EventFunc)

    def Pressed(self, EventFunc):
        self.Widget.connect("pressed", EventFunc)

    def Released(self, EventFunc):
        self.Widget.connect("released", EventFunc)

    def Clicked(self):
        self.Widget.clicked()

    def ClickedDo(self):
        self.Widget.do_clicked()


class GMenuButton(GWidget):
    def __init__(self, Popover: GPopover, Label: str = "Gib.GControl.GMenuButton"):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.MenuButton(popover=Popover.Get(), label=Label)

    def GetParent(self):
        return self.Widget.get_align_widget()

    def GetMenuModel(self):
        return self.Widget.get_menu_model()

    def GetPopover(self):
        return self.Widget.get_popover()

    def GetPopup(self):
        return self.Widget.get_popup()

    def GetUsePopover(self):
        return self.Widget.get_use_popover()


class GModelButton(GButton):
    def __init__(self, MenuName: str = "Gib.Gibox.GModelButton", Text: str = ""):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.ModelButton(menu_name=MenuName, text=Text)


class GToggleButton(GButton):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.ToggleButton()

    def SetActive(self, Active: bool):
        self.Widget.set_active(is_active=Active)

    def SetMode(self, Mode: bool):
        self.Widget.set_mode(draw_indicator=Mode)

    def GetActive(self):
        return self.Widget.get_active()

    def GetMode(self):
        return self.Widget.get_mode()

    def Toggled(self, Func):
        self.Widget.connect("toggled", Func)


class GScaleButton(GButton):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.ScaleButton()

    def SetIcons(self, Icons: str):
        self.Widget.set_icons(Icons)

    def SetValue(self, Value: int):
        self.Widget.set_value(Value)

    def GetValue(self):
        return self.Widget.get_value()


class GVolumeButton(GScaleButton):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.VolumeButton()


class GAppChooserButton(GAppChooser):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.AppChooserButton()

    def AddCustomItem(self, Name: str, Label: str, Icon):
        self.Widget.append_custiom_item(name=Name, label=Label, icon=Icon)

    def AddSeparator(self):
        self.Widget.append_separator()

    def GetHeading(self):
        return self.Widget.get_heading()

    def GetShowDefaultItem(self):
        return self.Widget.get_show_default_item()

    def GetShowDialogItem(self):
        return self.Widget.get_show_dialog_item()

    def SetActiveCustomItem(self, Name: str):
        self.Widget.set_active_custom_item(name=Name)


class GSalendar(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Calendar()

    def ClearMarks(self):
        self.Widget.clear_marks()

    def SelectDay(self, Day: int):
        self.Widget.select_day(Day)

    def SelectMonth(self, Year: int, Month: int):
        self.Widget.select_day(Month, Year)

    def GetDate(self):
        return self.Widget.get_date()

    def GetDayIsMarked(self, Day: int):
        return self.Widget.get_day_is_marked(day=Day)


class GSeparator(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Separator()


class GCheckButton(GToggleButton):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.CheckButton()


class GRadioButton(GCheckButton):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.RadioButton()

    def SetGroup(self, Group: GWidget):
        self.Widget.set_group(group=Group)

    def GetGroup(self):
        return self.Widget.get_group()

    def JoinGroup(self, GroupSource: GWidget):
        self.Widget.join_group(group_source=GroupSource)


class GListStore(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.ListStore()

    def Append(self, Row=None):
        self.Widget.append(row=Row)

    def Clear(self):
        self.Widget.clear()

    def Insert(self, Position: int, Row=None):
        self.Widget.insert(position=Position, row=Row)


class GTextView(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.TextView()

    def SetWrapMode(self, WrapMode: int = 0):
        self.Widget.set_wrap_mode(WrapMode)

    def SetJustification(self, Justification: int = 0):
        self.Widget.set_justification(Justification)

    def GetWrapMode(self):
        return self.Widget.get_wrap_mode()

    def GetJustification(self):
        return self.Widget.get_justification()


class GToolTip(GObject):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.Tooltip()

    def SetIcon(self, Icon: str, Size: int):
        self.Widget.set_icon_from_icon_name(icon_name=Icon, size=Size)

    def SetText(self, Text: str):
        self.Widget.set_text(text=Text)

    def SetMarkup(self, Markup: str):
        self.Widget.set_markup(markup=Markup)

    def SetCustom(self, CustomWidget: GWidget):
        self.Widget.set_custom(custom_widget=CustomWidget)


class GProgressBar(GWidget):
    def __init__(self, ShowText: bool = False, Text: str = "Gib.Gibox.GProgressBar"):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.ProgressBar(show_text=ShowText, text=Text)

    def SetPulseStep(self, Fraction: float):
        self.Widget.set_pulse_step(fraction=Fraction)

    def SetText(self, Text: str):
        self.Widget.set_text(Text)

    def SetFraction(self, Fraction: float):
        self.Widget.set_fraction(fraction=Fraction)

    def SetEllipsize(self, Mode: GEllipsizeMode or int):
        self.Widget.set_ellipsize(mode=Mode)

    def SetInverted(self, Inverted: bool):
        self.Widget.set_inverted(inverted=Inverted)

    def GetPulseStep(self):
        return self.Widget.get_pulse_step()

    def GetText(self):
        return self.Widget.get_text()

    def GetFraction(self):
        return self.Widget.get_fraction()

    def GetEllipsize(self):
        return self.Widget.get_ellipsize()

    def GetInverted(self):
        return self.Widget.get_inverted()

    def Pulse(self):
        self.Widget.pulse()


class GHeaderBar(GWidget):
    def __init__(self, Title: str = "Gib.Gibox.GHeaderBar",
                 CustomTitle: GWidget or None = None,
                 DecorationLayoutSet: bool = True,
                 DecorationLayout: str = "menu:minimize,maximize,close",
                 Subtitle: bool = True,
                 ShowCloseButton: bool = True, Spacing: int = 6):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.HeaderBar(title=Title,
                                    custom_title=CustomTitle,
                                    decoration_layout_set=DecorationLayoutSet,
                                    decoration_layout=DecorationLayout,
                                    has_subtitle=Subtitle,
                                    show_close_button=ShowCloseButton,
                                    spacing=Spacing)

    def PackEnd(self, Widget: GWidget):
        self.Widget.pack_end(child=Widget.Get())

    def PackStart(self, Widget: GWidget):
        self.Widget.pack_start(child=Widget.Get())

    def SetCustomTitle(self, CustomTitle: GWidget or None):
        self.Widget.set_custom_title(title_widget=CustomTitle)

    def SetDecorationLayout(self, Layout: str):
        self.Widget.set_decoration_layout(layout=Layout)

    def SetHasSubTitle(self, Subtitle: bool):
        self.Widget.set_has_subtitle(setting=Subtitle)

    def SetShowCloseButton(self, Setting: bool):
        self.Widget.set_show_close_button(setting=Setting)

    def SetSubTitle(self, SubTitle: str):
        self.Widget.set_subtitle(subtitle=SubTitle)

    def SetTitle(self, Title: str):
        self.Widget.set_title(title=Title)

    def GetCustomTitle(self):
        return self.Widget.get_custom_title()

    def GetDecorationLayout(self):
        return self.Widget.get_decoration_layout()

    def GetHasSubTitle(self):
        return self.Widget.get_has_subtitle()

    def GetShowCloseButton(self):
        return elf.Widget.get_show_close_button()

    def GtSubTitle(self):
        return self.Widget.get_subtitle()

    def GetTitle(self):
        return self.Widget.get_title()


class GInfoBar(GBox):
    def __init__(self, ShowCloseButton: bool = True, Message: int = 0):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.InfoBar(show_close_button=ShowCloseButton, message_type=Message)

    def AddAction(self, Action: GWidget, Number: int):
        self.Widget.add_action_widget(Action, Number)

    def AddButton(self, ButtonText: str, Number: int):
        self.Widget.add_button(ButtonText, Number)

    def Close(self, BindFunc):
        self.Event("close", BindFunc)


class GScrolledWindow(GWidget):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.ScrolledWindow()

    def GetHScrollbar(self):
        return self.Widget.get_hscrollbar()

    def GetVScrollbar(self):
        return self.Widget.get_vscrollbar()

    def GetMinContentHeight(self):
        return self.Widget.get_min_content_height()

    def GetMinContentWidth(self):
        return self.Widget.get_min_content_width()

    def GetMaxContentHeight(self):
        return self.Widget.get_max_content_height()

    def GetMaxContentWidth(self):
        return self.Widget.get_max_content_width()

    def SetMinContentHeight(self):
        return self.Widget.set_min_content_height()

    def SetMinContentWidth(self):
        return self.Widget.set_min_content_width()

    def SetMaxContentHeight(self):
        return self.Widget.set_max_content_height()

    def SetMaxContentWidth(self):
        return self.Widget.set_max_content_width()


class GPlacesSideBar(GScrolledWindow):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.PlacesSidebar()

    def ShowDesktop(self, Show: bool):
        self.Widget.show_desktop(Show)


class GTreeView(GWidget):
    def __init__(self):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.TreeView()


class GEventBox(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.EventBox()

    def ConnectEvent(self, EventName: str, EventFunc, EventWidget: GWidget):
        self.Widget.connect(EventWidget, EventFunc, EventWidget)


class GStatusBar(GBox):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Statusbar()


# GMenus
# -------------------------------------------------------------
class GMenuShell(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = None

    def AddMenu(self, Widget: GWidget):
        self.Widget.append(child=Widget.Get())

    def AddMenuItem(self, Widget: GWidget):
        self.Widget.prepend(child=Widget.Get())

    def Insert(self, Widget: GWidget, Pos: int):
        self.Widget.insert(child=Widget.Get(), position=Pos)

    def Select(self, Func):
        self.Event("select", Func)

    def Deactivate(self):
        self.Widget.deactivate()

    def Deselect(self):
        self.Widget.deselect()

    def GetParent(self):
        return self.Widget.get_parent_shell()

    def GetSelectItem(self):
        return self.Widget.get_selected_item()

    def Canel(self):
        self.Widget.cancel()


class GMenuBar(GMenuShell):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.MenuBar()


class GMenu(GMenuShell):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Menu()

    def SetTearOff(self, State: bool = False):
        self.Widget.set_tearoff_state(torn_off=State)

    def SetTitle(self, Title: str = "Gib.GMenus.GMenu"):
        self.Widget.set_title(title=Title)

    def Detach(self):
        self.Widget.detach()

    def DeleteMenu(self):
        self.Widget.popdown()


class GMenuItem(GMenuShell):
    def __init__(self, Label: str = "Gib.Gibox.GMenuItem", SubMenu: GWidget = None):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.MenuItem(label=Label, submenu=SubMenu)

    def SetLabel(self, Label: str):
        self.Widget.set_label(label=Label)

    def SetSubMenu(self, Widget: GWidget):
        self.Widget.set_submenu(Widget.Get())


# GTools
# -------------------------------------------------------------
class GToolShell(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = None

    def SetIconSize(self, IconSize: int):
        self.Widget.set_icon_size(IconSize)

    def RebuildMenu(self):
        self.Widget.rebuild_menu()


class GToolItem(GWidget):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.ToolItem()

    def SetExpand(self, Expand: bool):
        self.Widget.set_expand(expand=Expand)

    def SetHomogeneous(self, Homogeneous: bool):
        self.Widget.set_homogeneous(homogeneous=Homogeneous)

    def GetExpand(self):
        return self.Widget.get_expand()

    def GetHomegeneous(self):
        return self.Widget.get_homegeneous()


class GToolBar(GToolItem):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.Toolbar()

    def SetToolStyle(self, Style: int):
        self.Widget.set_style(Style)

    def GetToolStyle(self):
        return self.Widget.get_style()

    def Insert(self, Item: GToolItem, Pos: int):
        self.Widget.insert(item=Item.Get(), pos=Pos)


class GToolButton(GToolItem, GButton):
    def __init__(self, Label: str = "Gib.Gibox.GToolButton", Icon: str = ""):
        super().__init__()
        from gi.repository import Gtk
        self.Widget = Gtk.ToolButton(label=Label, icon_name=Icon)

    def SetLabel(self, Label: str):
        self.Widget.set_label(label=Label)

    def SetIcon(self, Icon: str):
        self.Widget.set_icon_name(icon_name=Icon)


class GToggleToolButton(GToolButton, GToggleButton):
    def __init__(self):
        super().__init__()
        self.Init()
        from gi.repository import Gtk
        self.Widget = Gtk.ToggleToolButton()

    def SetActive(self, Active: bool):
        self.Widget.set_active(is_active=Active)

    def GetActive(self):
        return self.Widget.get_active()
