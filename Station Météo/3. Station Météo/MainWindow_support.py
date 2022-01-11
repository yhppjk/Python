import tkinter as tk
import tkinter.ttk as ttk

#-- Custom part ----------------------------------
from hlpDataStruct import EMes, PMes, ErMes
import hlpGUIUpdate

def GUIBtnReset(p1):
    global EMes
    EMes.BtnReset = True

def GUIDisplay():
    global root, w, EMes, PMes, ErMes

    hlpGUIUpdate.GUIUpdate(root, w, EMes, PMes, ErMes)
    w.PPluviometrie["text"] = "{0:d}".format(EMes.Pluviometre)
    root.after(200, GUIDisplay)     # run everty 200ms

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
    top.resizable(0, 0)
    hlpGUIUpdate.GUICenter(top)
    GUIDisplay()
    #---------------------------------------------

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import MainWindow
    MainWindow.vp_start_gui()





