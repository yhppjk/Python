import nidaqmx
from nidaqmx.constants import TerminalConfiguration, AcquisitionType
import math
from statistics import mean





def GetArrayPeriod(trigger, data):
    for i in range(0, len(data)):
        if data[i] < trigger : break       #finding low state
    if i == len(data)-1 : return math.nan  #'NaN' if not found

    j=i

    for i in range(j, len(data)):
        if data[i] > trigger : break
    if i == len(data)-1 : return math.nan
                                           #finding first rising edge
                                           #'NaN' if not found
    FirstEdge = i

    j=i
    for i in range(j, len(data)):
        if data[i] < trigger : break
    if i == len(data)-1 : return math.nan
                                           #finding low state
    j=i                                       #'NaN' if not found
    for i in range(j, len(data)):
        if data[i] > trigger : break
    if i == len(data)-1 : return math.nan
                                           #finding second rising edge
                                           #'NaN' if not found
    SecondEdge = i

    return (SecondEdge - FirstEdge)


with nidaqmx.Task() as task:
    NbSamples  = 200
    RateTiming = 5000
    SampleTime = 1 / RateTiming
    task.ai_channels.add_ai_voltage_chan(physical_channel = "dev1/ai2:3", terminal_config = TerminalConfiguration.RSE)
    task.timing.cfg_samp_clk_timing     (rate = RateTiming, sample_mode = AcquisitionType.FINITE, samps_per_chan = NbSamples)
    Samples = task.read                 (number_of_samples_per_channel = NbSamples)



Frequency = 1 / (GetArrayPeriod(trigger=2, data=Samples[0]) * SampleTime)
Average   = mean(Samples[1])

import os; os.system('cls')
print((GetArrayPeriod(trigger=2, data=Samples[0]) * SampleTime))

print("Humidite  : ", "{:.0f}".format(Frequency), " Hz")
print("Girouette : ", "{:.2f}".format(Average),   " V" )
