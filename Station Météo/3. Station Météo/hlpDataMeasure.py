#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpDataMeasure - Helper providing data from sensors measuring                       JYC-2021
#-----------------------------------------------------------------------------------------------------------------------
# Sensors :
# --------------------
# Humidity     AI2
# Wind Vane    AI3
# Temperature  AI6
# Brightness   AI7
# Rain Gauge   P0.7
# Encoder      P1.0..3
# Anemometer   PFI0
#-----------------------------------------------------------------------------------------------------------------------

import nidaqmx
import nidaqmx.system

from nidaqmx.task import Task
from hlpDataStruct import ElectricalMeasures, ErrorMeasures

class DataMeasure:
    wTask : Task = None
    bTask : Task = None
    nTask : Task = None
    cTask : Task = None

    NbSamples    = 200
    RateTiming   = 5000
    SampleTime   = 1 / RateTiming
    PrevPluv     = True

    ErMes = ErrorMeasures()
    EMes  = ElectricalMeasures()

    #-------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.EMes.HumidimetreAX = [0.0] * self.NbSamples
        self.EMes.HumidimetreAY = [0.0] * self.NbSamples
        for i in range(0, len(self.EMes.HumidimetreAX)): self.EMes.HumidimetreAX[i] = (self.SampleTime * i) * 1000

    #-------------------------------------------------------------------------------------------------------------------
    def RegError(self, e : nidaqmx.DaqError):
        import inspect

        self.ErMes.CurrentCode = e.error_code

        if self.ErMes.ErrorFlag: return

        self.ErMes.ErrorFlag         = True
        self.ErMes.ErrorFunctionName = __name__+"\\"+inspect.currentframe().f_back.f_code.co_name    # get caller function name
        self.ErMes.ErrorCode         = e.error_code
        self.ErMes.ErrorType         = e.error_type
        self.ErMes.ErrorMessage      = e.__str__().replace('\n', '  ')

    #-------------------------------------------------------------------------------------------------------------------
    def ClearError(self):
        self.ErMes.CurrentCode       = 0
        self.ErMes.ErrorFlag         = False
        self.ErMes.ErrorFunctionName = ""
        self.ErMes.ErrorCode         = 0
        self.ErMes.ErrorType         = ""
        self.ErMes.ErrorMessage      = ""

    #-------------------------------------------------------------------------------------------------------------------
    def Open(self):
        from nidaqmx.constants import TerminalConfiguration, AcquisitionType, LineGrouping, Edge

        try:
            #...........................................................................................................
            DevName = ""
            for device in nidaqmx.system.System.local().devices:
                if device.product_type.find("USB-600") != -1:
                    DevName = device.name
                    break
            if DevName == "": raise(nidaqmx.DaqError("Device auto-search failed", -200220, "No task"))
            #...........................................................................................................
            self.wTask = nidaqmx.Task                      ("WaveformTask")
            self.wTask.ai_channels.add_ai_voltage_chan     (physical_channel = DevName+"/ai2:3, "+DevName+"/ai6:7", terminal_config = TerminalConfiguration.RSE)
            self.wTask.timing.cfg_samp_clk_timing          (rate= self.RateTiming, sample_mode = AcquisitionType.FINITE, samps_per_chan = self.NbSamples)
            #...........................................................................................................
            self.bTask = nidaqmx.Task                      ("BitTask")
            self.bTask.di_channels.add_di_chan             (lines = DevName+"/port0/line7", line_grouping = LineGrouping.CHAN_PER_LINE)
            #...........................................................................................................
            self.nTask = nidaqmx.Task                      ("iNtegerTask")
            self.nTask.di_channels.add_di_chan             (lines = DevName+"/port1/line0:3", line_grouping = LineGrouping.CHAN_FOR_ALL_LINES)
            #...........................................................................................................
            self.cTask = nidaqmx.Task                      ("CounterTask")
            self.cTask.ci_channels.add_ci_count_edges_chan (counter = DevName+"/ctr0", edge = Edge.FALLING).ci_count_edges_term = "/"+DevName+"/pfi0"
            self.cTask.start()
            #...........................................................................................................
            self.ErMes.CurrentCode = 0
        except nidaqmx.DaqError as e:
            self.RegError(e)

    #-------------------------------------------------------------------------------------------------------------------
    def FastRead(self):
        from statistics import mean

        try:
            #...........................................................................................................
            if self.wTask == None: raise(nidaqmx.DaqError("Task doesn't exist", -200088, "WaveformTask"))

            Samples = self.wTask.read(number_of_samples_per_channel=self.NbSamples)
            self.wTask.wait_until_done()

            ew = self.GetEdgesWidth(trigger=2, data=Samples[0])
            if ew > 0: self.EMes.Humidimetre = self.RateTiming / ew

            self.EMes.HumidimetreAY = Samples[0]

            self.EMes.Girouette   = mean(Samples[1])
            self.EMes.Thermometre = mean(Samples[2])
            self.EMes.Luxmetre    = mean(Samples[3])

            #...........................................................................................................
            if self.bTask == None: raise(nidaqmx.DaqError("Task doesn't exist", -200088, "BitTask"))

            b = self.bTask.read()
            self.bTask.wait_until_done()

            if (self.PrevPluv and (not b)) : self.EMes.Pluviometre += 1  # +1 if falling edge (1 --> 0)
            self.PrevPluv = b

            # ===ToDo===   reset EMes.Pluviometre if BtnReset pressed

            #...........................................................................................................
            if self.nTask == None: raise(nidaqmx.DaqError("Task doesn't exist", -200088, "iNtegerTask"))

            self.EMes.Encodeur = self.nTask.read()
            self.nTask.wait_until_done()
            #...........................................................................................................
            self.ErMes.CurrentCode = 0
        except nidaqmx.DaqError as e:
            self.RegError(e)

    #-------------------------------------------------------------------------------------------------------------------
    def SlowRead(self):
        try:
            if self.cTask == None: raise(nidaqmx.DaqError("Task doesn't exist", -200088, "CounterTask"))

            self.EMes.Anemometre = self.cTask.read()
            self.cTask.wait_until_done()
            self.cTask.stop()
            self.cTask.start()

            self.ErMes.CurrentCode = 0
        except nidaqmx.DaqError as e:
            self.RegError(e)

    #-------------------------------------------------------------------------------------------------------------------
    def Close(self):
        try:
            if self.wTask != None: self.wTask.close()
            if self.bTask != None: self.bTask.close()
            if self.nTask != None: self.nTask.close()
            if self.cTask != None: self.cTask.close()

            self.wTask = None
            self.bTask = None
            self.nTask = None
            self.cTask = None

            self.ErMes.CurrentCode = 0
        except nidaqmx.DaqError as e:
            self.RegError(e)

    #-------------------------------------------------------------------------------------------------------------------
    def GetEdgesWidth(self, trigger, data):
        for i in range(0, len(data)):
            if data[i] < trigger : break       # finding low state
        if i == len(data)-1 : return -1        # -1  if not found

        j = i
        for i in range(j, len(data)):
            if data[i] > trigger : break       # finding first rising edge
        if i == len(data)-1 : return -1        # -1  if not found
        FirstEdge = i

        j = i
        for i in range(j, len(data)):
            if data[i] < trigger : break       # finding low state
        if i == len(data)-1 : return -1        # -1  if not found

        j = i
        for i in range(j, len(data)):
            if data[i] > trigger : break       # finding second rising edge
        if i == len(data)-1 : return -1        # -1  if not found
        SecondEdge = i

        return (SecondEdge - FirstEdge)
