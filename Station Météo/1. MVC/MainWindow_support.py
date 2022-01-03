import tkinter as tk
import tkinter.ttk as ttk

#-- Custom part ----------------------------------
GUIBtnReset = False
GUINum      = 0

def GUIDisplay():
    w.TextNum["text"] = "{0:d}".format(GUINum)
    root.after(300, GUIDisplay)

def GUIStart():
    import MainWindow
    MainWindow.vp_start_gui()
#-------------------------------------------------

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

    #-- Custom part ------------------------------
    GUIDisplay()
    #---------------------------------------------

def BtnReset(p1):
    #-- Custom part ------------------------------
    global GUIBtnReset
    GUIBtnReset = True
    #---------------------------------------------

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import MainWindow
    MainWindow.vp_start_gui()
