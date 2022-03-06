# Gib
___
#### `Gib` 是`PyGobject`的超级工具包，语法简单快捷，还将各个组件进行了分类（如`GContainer`、`GControl`、`GMenus`、`GQuick`等）。

### Gib与Gtk的区别：

#### 从实现窗口来看对比
#### Gtk：
```python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
Window = Gtk.Window()
Window.show_all()
Window.connect("delete-event", Gtk.main_quit)
Gtk.main()
```

#### Gib:
```python
from Gib.Gibox import GWindow
Window = GWindow()
Window.Run()
```

#### 是不是简单了许多，我们将许多函数都封装到了``GWindow.Run()``上面。

#### 让我们举个例子，使用Gtk和Gib制作最经典的HelloWorld程序
#### Gtk:
```python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    @staticmethod
    def on_button_clicked(self, widget):
        print("Hello World")
        

def main():
    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
```

#### Gib:
```python
from Gib.GContainer import *
from Gib.GControl import *


class App(GWindow):
    def __init__(self):
        GWindow.__init__(self, Title="Hello,World")

        self.Button = GButton(Label="Click Here")
        self.Button.Widget.connect("clicked", self.Click)
        self.Add(self.Button)

    @staticmethod
    def Click(self):
        print("Hello World")


def main():
    Window = App()
    Window.Run()


if __name__ == '__main__':
    main()
```
## Gib安装教程
___
#### 之前我们有讲过，``Gib``是``PyGobject``的工具包，那么说``Gib``的依赖库是``PyGobject``，所以安装Gib之前要知道如何安装``PyGobject``。
>以下安装方法仅支持Windows系统
#### 1.先进 [Msys2](https://www.msys2.org/) 官网安装Msys2
>[Msys2下载地址](https://github.com/msys2/msys2-installer/releases/download/2021-11-30/msys2-x86_64-20211130.exe)
#### 2.安装好Msys2后打开MSYS2 MSYS程序。首先安装Gtk的依赖库。在MSYS2 MSYS程序里输入以下代码后，等待安装好。
>>pacman -S mingw-w64-x86_64-gtk3
> 
> 注意：在在中途会提示是否安装gtk,请输入`Y`即可继续安装。
#### 3.安装好Gtk后可以再安装一个Glade设计器。在MSYS2 MSYS程序里输入以下代码安装。
>>pacman -S mingw-w64-x86_64-glade
> 
> 注意：在在中途会提示是否安装glade,请输入`Y`即可继续安装。
> 
#### 4.安装由Gtk绑定后的Python解释器。请输入以下代码进行安装。

>Python2.x绑定
>>pacman -S mingw-w64-x86_64-python2-gobject
>
> Python3.x绑定
>>pacman -S mingw-w64-x86_64-python3-gobject
>
> 注意：在在中途会提示是否安装glade,请输入`Y`即可继续安装。

#### 5.安装好后进入``MSYS2``文件夹的``mingw64/bin``文件夹中找到``python.exe``（文件地址：`.\Msys2\mingw64\bin\python.exe`），这就是绑定后的解释器。还可以在这个文件夹里找到Glade设计器的执行程序（文件地址：`.\Msys2\mingw64\bin\glade.exe`）
