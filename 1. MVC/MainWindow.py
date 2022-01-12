import sys

import tkinter as tk
import tkinter.ttk as ttk

import MainWindow_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Main (root)
    MainWindow_support.init(root, top)
    root.mainloop()

w = None
def create_Main(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Main(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Main (w)
    MainWindow_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Main():
    global w
    w.destroy()
    w = None

class Main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("215x134+270+100")
        top.minsize(116, 1)
        top.maxsize(2110, 1418)
        top.resizable(0,  0)
        top.title("Pluviomètre")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.BtnReset = tk.Button(top)
        self.BtnReset.place(x=70, y=70, height=24, width=75)
        self.BtnReset.configure(activebackground="#ececec")
        self.BtnReset.configure(activeforeground="#000000")
        self.BtnReset.configure(background="#d9d9d9")
        self.BtnReset.configure(disabledforeground="#a3a3a3")
        self.BtnReset.configure(font="-family {Segoe UI} -size 9")
        self.BtnReset.configure(foreground="#000000")
        self.BtnReset.configure(highlightbackground="#d9d9d9")
        self.BtnReset.configure(highlightcolor="black")
        self.BtnReset.configure(pady="0")
        self.BtnReset.configure(text='''Reset''')
        self.BtnReset.bind('<ButtonRelease-1>',lambda e:MainWindow_support.BtnReset(e))

        self.TextNum = tk.Label(top)
        self.TextNum.place(x=70, y=30, height=21, width=74)
        self.TextNum.configure(activebackground="#f9f9f9")
        self.TextNum.configure(activeforeground="black")
        self.TextNum.configure(background="#d9d9d9")
        self.TextNum.configure(disabledforeground="#a3a3a3")
        self.TextNum.configure(font="-family {Segoe UI} -size 9")
        self.TextNum.configure(foreground="#000000")
        self.TextNum.configure(highlightbackground="#d9d9d9")
        self.TextNum.configure(highlightcolor="black")
        self.TextNum.configure(relief="sunken")
        self.TextNum.configure(text='''0''')

if __name__ == '__main__':
    vp_start_gui()
