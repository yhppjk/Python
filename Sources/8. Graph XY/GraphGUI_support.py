import tkinter as tk
import tkinter.ttk as ttk

#-- graph functions ----------------------------------------------------------------------------------------------------
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def GraphInit():
    global GraphSubPlot, GraphCanvas

    fig = Figure(dpi=100)
    fig.set_tight_layout({'pad' : 1})
    GraphSubPlot = fig.add_subplot()

    GraphCanvas = FigureCanvasTkAgg(fig, master=root)
    GraphCanvas.get_tk_widget().place(in_=w.Canvas1, relwidth=1, relheight=1)

def GraphPlot(ax, ay):
    global GraphSubPlot, GraphCanvas

    GraphSubPlot.clear()
    GraphSubPlot.plot(ax, ay)
    GraphSubPlot.set(xlabel="Time (ms)", ylabel="Volts", autoscaley_on=False, ylim=(-0.1, 5.2))  # autoscalex_on=False, xlim=(0,10)
    GraphCanvas.draw()

#-- daqmx functions -----------------------------------------------------------------------------------------------------
import nidaqmx
from   nidaqmx.constants import TerminalConfiguration, AcquisitionType

def DAQmxOpen():
    global WaveformNbSamples, WaveformX, WaveformTask

    WaveformNbSamples  = 200
    RateTiming         = 5000
    SampleTime         = 1 / RateTiming

    WaveformX = [0.0] * WaveformNbSamples
    for i in range(0, len(WaveformX)): WaveformX[i] = (SampleTime * i) * 1000

    WaveformTask = nidaqmx.Task()
    WaveformTask.ai_channels.add_ai_voltage_chan(physical_channel = "dev1/ai2", terminal_config = TerminalConfiguration.RSE)
    WaveformTask.timing.cfg_samp_clk_timing     (rate = RateTiming, sample_mode = AcquisitionType.FINITE, samps_per_chan = WaveformNbSamples)

def DAQmxRead():
    global WaveformTask, WaveformNbSamples, WaveformY

    WaveformY = WaveformTask.read(number_of_samples_per_channel = WaveformNbSamples)

def DAQmxClose():
    global WaveformTask

    if WaveformTask is not None: WaveformTask.close()
    WaveformTask = None

#-- timed loop functions -----------------------------------------------------------------------------------------------
import continuous_threading

def TimedLoopStart():
    global th

    DAQmxOpen()
    GraphInit()

    th = continuous_threading.PeriodicThread(0.1, TimedLoopJob)  # create thread looped every 100 ms
    th.start()

def TimedLoopJob():  # 100ms loop
    global WaveformX, WaveformY

    DAQmxRead()
    GraphPlot(WaveformX, WaveformY)

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
    import GraphGUI
    GraphGUI.vp_start_gui()
