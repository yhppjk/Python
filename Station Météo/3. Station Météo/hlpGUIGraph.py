#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpGUIGraph - Helper for plotting Graph & Chart on GUI                              JYC-2021
#-----------------------------------------------------------------------------------------------------------------------

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
def PeakDetect(Values):
    max_y : float = []
    for i in range(1, len(Values)-2):
        if(Values[i-1] < Values[i] and Values[i+1] < Values[i]):
                max_y.append(Values[i])
    #for i in range(0, len(max_x)-):
    # for i in reversed(range(len(max_x)-2)):
    #     if(max_x[i+1]-max_x[i] == 2 ):
    #            if (Values[i] >= Values[i+1]):
    #                   #max_x.remove(max_x[i+1])
    #                   del max_x[i+1]
    #            else:
    #                   #max_x.remove(max_x[i])
    #                   del max_x[i]
    return max_y



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
        self.historic.append(v)
        position_y = PeakDetect(self.historic)
        position_x = range(len(position_y))

        self.subplot.clear()
        self.subplot.plot(self.historic)
        self.subplot.scatter(position_x, position_y, color = 'r', s = 50, marker = 'D', label = 'Peaks')
        self.subplot.set(ylabel="km/s", autoscalex_on=False, xlim=(0, self.nbpoints), autoscaley_on=False, ylim=(0,50))
        self.canvas.draw()

        print(t)
        print(v)

        pass


#-----------------------------------------------------------------------------------------------------------------------
# class PeakPlot:

#     def __init__(self, root, canvas, nbpoints):
#         self.nbpoints : int   = nbpoints
#         self.historic : float = []
#         self.time : float =[]
#         self.direction : str = []
#         self.peak_time    : float   = []
#         self.peak_v : float = []

#         fig = Figure(dpi=100)
#         fig.set_tight_layout({"pad" : 1})
#         self.subplot = fig.add_subplot()

#         self.canvas = FigureCanvasTkAgg(fig, master=root)
#         self.canvas.get_tk_widget().place(in_=canvas, relwidth=1, relheight=1)

#     def Plot(self, t:float, v:float, d:str):

#         if len(self.historic) >= self.nbpoints:
#             self.historic.pop(0)
#         self.historic.append(v)
#         self.time.append(t)
#         self.direction.append(d)
#         self.subplot.clear()
#         self.subplot.plot(self.historic)

#         self.peak_time = PeakDetect(Values=self.historic)
#         for item in self.peak_time :
#             self.peak_v.append(self.historic[item])

#         # self.subplot.plot(self.peak_time, self.peak_v)

#         self.subplot.scatter(self.time, self.peak_v, color = 'r', s = 50, marker = 'D', label = 'Peaks')

#         self.subplot.set(ylabel="km/s", autoscalex_on=False, xlim=(0, self.nbpoints), autoscaley_on=False, ylim=(0,50))
#         self.canvas.draw()
