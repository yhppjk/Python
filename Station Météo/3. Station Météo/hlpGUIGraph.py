#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpGUIGraph - Helper for plotting Graph & Chart on GUI                              JYC-2021
#-----------------------------------------------------------------------------------------------------------------------

from dataclasses import dataclass
from datetime import datetime
import time

from matplotlib.pyplot import plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#-----------------------------------------------------------------------------------------------------------------------
class GraphPlot:
    def __init__(self, root, canvas):
        fig = Figure(dpi=100)
        fig.set_tight_layout({"pad" : 1})
        self.subplot = fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().place(in_=canvas, relwidth=1, relheight=1)

    def Plot(self, ax, ay):
        self.subplot.clear()
        self.subplot.plot(ax, ay)
        self.subplot.set(xlabel="Temps (ms)", ylabel="Volts", autoscaley_on=False, ylim=(-0.1, 5.2))
        self.canvas.draw()

#-----------------------------------------------------------------------------------------------------------------------
class ChartPlot:
    def __init__(self, root, canvas, nbpoints):
        self.nbpoints : int   = nbpoints
        self.historic : float = []

        fig = Figure(dpi=100)
        fig.set_tight_layout({"pad" : 1})
        self.subplot = fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().place(in_=canvas, relwidth=1, relheight=1)

    def Plot(self, value):
        if len(self.historic) >= self.nbpoints:
            self.historic.pop(0)
        self.historic.append(value)

        self.subplot.clear()
        self.subplot.plot(self.historic)
        self.subplot.set(ylabel="Volts", autoscalex_on=False, xlim=(0, self.nbpoints), autoscaley_on=False, ylim=(-0.1, 5.2))
        self.canvas.draw()

#-----------------------------------------------------------------------------------------------------------------------
# ===ToDo===  fullfill this class
def PeakDetect(Values, delta = 5 ):
    max_x : int = []
    po_x : int
    modemax = True
    max = -9999
    min = 9999
    for i in range(len(Values)):
        if modemax:
            if Values[i] > max:
                max = Values[i]
                po_x = i
            if Values[i] < max-delta:
                max_x.append(po_x)
                max = -9999
                modemax = False



        else:
            if Values[i] < min:
                min = Values[i]
            if Values[i] > min+delta:
                modemax = True
                min  = 9999
    return max_x



class PeakPlot:

    def __init__(self, root, canvas, nbpoints):
        self.nbpoints : int   = nbpoints
        self.historic : float = []

        fig = Figure(dpi=100)
        fig.set_tight_layout({"pad" : 1})
        self.subplot = fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.get_tk_widget().place(in_=canvas, relwidth=1, relheight=1)

    def Plot(self, t:datetime, v:float, d:str):

        if len(self.historic) >= self.nbpoints:
            self.historic.pop(0)
        self.historic.append(Pointpeak(t, v, d))

        values = [i.vitesse  for i in self.historic]
        position_x = PeakDetect(values)
        position_y = [values[i] for i in position_x]



        self.subplot.clear()
        self.subplot.plot(values)
        self.subplot.scatter(position_x, position_y, color = 'r', s = 50, marker = 'D', label = 'Peaks')
        self.subplot.set(ylabel="km/s", autoscalex_on=False, xlim=(0, self.nbpoints), autoscaley_on=False, ylim=(0,50))
        self.canvas.draw()

        # print(position_x)

        return [self.historic[p].output for p in position_x]

@dataclass (frozen = True)
class Pointpeak:
    # def __init__(self, time, vitesse, direction):
        time : datetime
        vitesse : float
        direction : str
        def output(self):
            return str(self.time)
            # return f'{self.time:%d/%m/%Y %H:%M:%S} - {int(self.vitesse):2d} km/h - {self.direction}'

#-----------------------------------------------------------------------------------------------------------------------

