import tkinter as tk
import tkinter.ttk as ttk

#-- graph functions ----------------------------------------------------------------------------------------------------
from   matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from   matplotlib.figure import Figure

def ChartInit():
    global ChartSubPlot, ChartCanvas, ChartNbPoints,  ChartHistoric

    ChartNbPoints = 100
    ChartHistoric = []

    fig = Figure(dpi=100)
    fig.set_tight_layout({'pad' : 1})
    ChartSubPlot = fig.add_subplot()

    ChartCanvas = FigureCanvasTkAgg(fig, master=root)
    ChartCanvas.get_tk_widget().place(in_=w.Canvas1, relwidth=1, relheight=1)

def ChartPlot(value):
    global ChartSubPlot, ChartCanvas, ChartNbPoints, ChartHistoric

    if len(ChartHistoric) >= ChartNbPoints:
        ChartHistoric.pop(0)
    ChartHistoric.append(value)

    ChartSubPlot.clear()
    ChartSubPlot.plot(ChartHistoric)
    ChartSubPlot.set(xlabel="Points", ylabel="Volts", autoscalex_on=False, xlim=(0, ChartNbPoints), autoscaley_on=False, ylim=(-0.1, 5.2))
    ChartCanvas.draw()

#-- daqmx functions -----------------------------------------------------------------------------------------------------
import nidaqmx
from   nidaqmx.constants import TerminalConfiguration

def DAQmxOpen():
    global AnalogTask

    AnalogTask = nidaqmx.Task()
    AnalogTask.ai_channels.add_ai_voltage_chan(physical_channel = "dev1/ai3", terminal_config = TerminalConfiguration.RSE)

def DAQmxRead():
    global AnalogTask, OneMeasure

    OneMeasure = AnalogTask.read()

def DAQmxClose():
    global AnalogTask

    if AnalogTask is not None: AnalogTask.close()
    AnalogTask = None

#-- timed loop functions -----------------------------------------------------------------------------------------------
import continuous_threading

def TimedLoopStart():
    global th

    DAQmxOpen()
    ChartInit()

    th = continuous_threading.PeriodicThread(0.1, TimedLoopJob)  # create thread looped every 100 ms
    th.start()

def TimedLoopJob():  # 100ms loop
    global OneMeasure

    DAQmxRead()
    ChartPlot(OneMeasure)

def TimedLoopStop():
    global th

    th.join()
    DAQmxClose()

#-- window functions ---------------------------------------------------------------------------------------------------
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    TimedLoopStart()

def close(p1):
    TimedLoopStop()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import ChartGUI
    import os; os.system('cls')
    ChartGUI.vp_start_gui()
