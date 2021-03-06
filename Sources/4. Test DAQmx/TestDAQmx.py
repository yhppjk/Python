#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.1
#  in conjunction with Tcl version 8.6
#    May 14, 2021 10:55:16 AM CEST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import TestDAQmx_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TesDAQmx (root)
    TestDAQmx_support.init(root, top)
    root.mainloop()

w = None
def create_TesDAQmx(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_TesDAQmx(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = TesDAQmx (w)
    TestDAQmx_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_TesDAQmx():
    global w
    w.destroy()
    w = None

class TesDAQmx:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 9"
        font14 = "-family {Segoe UI} -size 9"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font=font11)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("209x159+268+96")
        top.minsize(116, 1)
        top.maxsize(2110, 1418)
        top.resizable(1,  1)
        top.title("Test DAQmx")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.AI0 = tk.Label(top)
        self.AI0.place(x=110, y=30, height=21, width=37)
        self.AI0.configure(activebackground="#f9f9f9")
        self.AI0.configure(activeforeground="black")
        self.AI0.configure(anchor='e')
        self.AI0.configure(background="#ffffff")
        self.AI0.configure(disabledforeground="#a3a3a3")
        self.AI0.configure(font="-family {Segoe UI} -size 9")
        self.AI0.configure(foreground="#000000")
        self.AI0.configure(highlightbackground="#d9d9d9")
        self.AI0.configure(highlightcolor="black")
        self.AI0.configure(justify='right')
        self.AI0.configure(text='''0.00''')

        self.AI1 = tk.Label(top)
        self.AI1.place(x=110, y=60, height=21, width=37)
        self.AI1.configure(activebackground="#f9f9f9")
        self.AI1.configure(activeforeground="black")
        self.AI1.configure(anchor='e')
        self.AI1.configure(background="#ffffff")
        self.AI1.configure(disabledforeground="#a3a3a3")
        self.AI1.configure(font="-family {Segoe UI} -size 9")
        self.AI1.configure(foreground="#000000")
        self.AI1.configure(highlightbackground="#d9d9d9")
        self.AI1.configure(highlightcolor="black")
        self.AI1.configure(justify='right')
        self.AI1.configure(text='''0.00''')

        self.BtnRead = ttk.Button(top)
        self.BtnRead.place(x=50, y=100, height=25, width=96)
        self.BtnRead.configure(takefocus="")
        self.BtnRead.configure(text='''READ''')
        self.BtnRead.bind('<ButtonRelease-1>',lambda e:TestDAQmx_support.BtnReadRelease(e))

        self.AI0name = tk.Message(top)
        self.AI0name.place(x=50, y=30, height=23, width=37)
        self.AI0name.configure(anchor='w')
        self.AI0name.configure(background="#d9d9d9")
        self.AI0name.configure(font="-family {Segoe UI} -size 9")
        self.AI0name.configure(foreground="#000000")
        self.AI0name.configure(highlightbackground="#d9d9d9")
        self.AI0name.configure(highlightcolor="black")
        self.AI0name.configure(text='''AI0 :''')
        self.AI0name.configure(width=60)

        self.AI0name_1 = tk.Message(top)
        self.AI0name_1.place(x=50, y=60, height=23, width=33)
        self.AI0name_1.configure(anchor='w')
        self.AI0name_1.configure(background="#d9d9d9")
        self.AI0name_1.configure(font="-family {Segoe UI} -size 9")
        self.AI0name_1.configure(foreground="#000000")
        self.AI0name_1.configure(highlightbackground="#d9d9d9")
        self.AI0name_1.configure(highlightcolor="black")
        self.AI0name_1.configure(text='''AI1 :''')
        self.AI0name_1.configure(width=33)

        self.menubar = tk.Menu(top, font="-family {Segoe UI} -size 9", bg=_bgcolor
                ,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()





