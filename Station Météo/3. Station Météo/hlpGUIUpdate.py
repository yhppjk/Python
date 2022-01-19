#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpGUIUpdate - Helper for updating GUI content                                      JYC-2021
#-----------------------------------------------------------------------------------------------------------------------

import datetime
from tkinter.ttk import Progressbar
from hlpGUIGraph import ChartPlot, GraphPlot, PeakPlot

GraphHumidite  : GraphPlot = None
ChartGirouette : ChartPlot = None
PeakVitesse    : PeakPlot  = None
valtrue : int=0


def GUIUpdate(root, w, EMes, PMes, ErMes):
    global GraphHumidite, ChartGirouette,PeakVitesse

    # create three graphs on GUI at the first call
    if GraphHumidite  == None: GraphHumidite  = GraphPlot(root, w.EGraphHumidite)
    if ChartGirouette == None: ChartGirouette = ChartPlot(root, w.EChartGirouette, 100)
    if PeakVitesse    == None: PeakVitesse    = PeakPlot (root, w.PPeakVitesse,    100)

    # ===ToDo===  fullfill PeakPlot class in hlpGUIGraph.py and create PPeakVitesse canvas on GUI
    #
    #if PeakVitesse    == None: PeakVitesse    = PeakPlot (root, w.PPeakVitesse,    100)




    # solve Encodeur
    EMes.Encodeur


    # update electrical measures
    w.EHumidimetre  ["text"]  = "{:.0f} Hz".format(EMes.Humidimetre)
    w.EGirouette    ["text"]  = "{:.3f} V" .format(EMes.Girouette)
    w.EThermometre  ["text"]  = "{:.3f} V" .format(EMes.Thermometre)
    w.ELuxmetre     ["text"]  = "{:.3f} V" .format(EMes.Luxmetre)
    w.EPluviometre  ["text"]  = "{:.0f}"   .format(EMes.Pluviometre)
    w.EEncodeur     ["text"]  = "{:.0f}"   .format(EMes.Encodeur)
    w.EAnemometre   ["text"]  = "{:.0f}"   .format(EMes.Anemometre)
    w.EDureeMesures ["text"]  = "{:.0f} ms".format(EMes.DureeMesures)
    w.ETempsBoucleR ["text"]  = "{:.0f} ms".format(EMes.TempsBoucleR)
    w.ETempsBoucleL ["text"]  = "{:.0f} ms".format(EMes.TempsBoucleL)

    # ===ToDo=== set Encodeur boolean indicators (background color value : light if bit true, dark else)
    #use this model   : x = ValTrue  if (condition)  else ValFalse
    # use named colors : https://matplotlib.org/stable/gallery/color/named_colors.html




    w.EP1_0["bg"] = '#FFD700' if EMes.Encodeur & 0b0001 else '#f9f9f9'
    w.EP1_1["bg"] ='#FFD700' if EMes.Encodeur & 0b0010 else '#f9f9f9'
    w.EP1_2["bg"] ='#FFD700' if EMes.Encodeur & 0b0100 else '#f9f9f9'
    w.EP1_3["bg"] ='#FFD700' if EMes.Encodeur & 0b1000 else '#f9f9f9'




    now = datetime.datetime.now()
    GraphHumidite.Plot (EMes.HumidimetreAX, EMes.HumidimetreAY)
    ChartGirouette.Plot(EMes.Girouette)
    PeakVitesse.Plot(now,PMes.Vitesse,PMes.Direction)




    # update physical measures
    #
    # ===ToDo=== copy physical measures to indicators
    #
    # use "format" function as electrical measures
    w.PDirection    ["text"]  ="{:s} ".format(PMes.Direction)
    w.PVitesse      ["text"]  ="{:.0f} km/h".format(PMes.Vitesse)
    w.PTemperature  ["text"]  ="{:.0f} °C".format(PMes.Temperature)
    w.PHumidite     ["text"]  ="{:.0f} %".format(PMes.Humidite)
    w.PLuminosite   ["text"]  ="{:.0f} k lux".format(PMes.Luminosite)
    w.PPluviometrie ["text"]  ="{:.0f} ".format(PMes.Pluviometrie)
    w.PStation      ["text"]  ="{:.0f} ".format(PMes.Station)
    # w.PeakVitesse      ["text"]  ="{:.0f} ".format(PMes.PeakVitesse)

    #
    # create the "clamp" function to constraint data into limits
    #


    w.PBVitesse      ["value"] = clamp(int(PMes.Vitesse),      0, 30)
    w.PBTemperature  ["value"] = clamp(int(PMes.Temperature),  0, 50)
    w.PBLuminosite   ["value"] = clamp(int(PMes.Luminosite),  0, 150)
    w.PBHumidite     ["value"] = clamp(int(PMes.Humidite),     0, 100)
    w.PBPluviometrie ["value"] = clamp(int(PMes.Pluviometrie), 0, 10)
    #

    peak_list = PeakVitesse.Plot(now, PMes.Vitesse, PMes.Direction)
    #
    # ToDo : - update Label PListeVitesse with peak_list
    #        - save peak_list in text file


    w.PListeVitesse ["text"] =peak_list
    for i in reversed(range(0,len(peak_list))):
        file =  open("peak","a")
        if peak_list != None:
           file.write(str(peak_list[i]))
           file.write('\r\n')
           del peak_list[i]
        file.close()



    # update status message
    if not ErMes.ErrorFlag:
        w.Etat       ['text'] = "Mesures en cours ..."
    else:
        w.Etat       ['text'] = "Function: {:s}  Code: {:d}  Type: {:s}".format(ErMes.ErrorFunctionName, ErMes.ErrorCode, ErMes.ErrorType)

def GUICenter(win):
    win.update_idletasks()

    width        = win.winfo_width()
    frm_width    = win.winfo_rootx() - win.winfo_x()
    win_width    = width + 2 * frm_width
    height       = win.winfo_height()
    title_height = win.winfo_rooty() - win.winfo_y()
    win_height   = height + title_height + frm_width

    x = win.winfo_screenwidth()  // 2 - win_width  // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def clamp(value, min, max):
    i = (100*value)/max

    return i
