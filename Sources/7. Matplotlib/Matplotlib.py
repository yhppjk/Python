import nidaqmx
from nidaqmx.constants import TerminalConfiguration, AcquisitionType

with nidaqmx.Task() as task:
    NbSamples  = 200
    RateTiming = 5000
    task.ai_channels.add_ai_voltage_chan(physical_channel = "dev1/ai2", terminal_config = TerminalConfiguration.RSE)
    task.timing.cfg_samp_clk_timing     (rate = RateTiming, sample_mode = AcquisitionType.FINITE, samps_per_chan = NbSamples)
    Samples = task.read                 (number_of_samples_per_channel = NbSamples)
    
import matplotlib.pyplot as plt
plt.figure("Humidity sensor - AI2")
plt.xlabel("Samples")
plt.ylabel("Volts")
plt.plot  (Samples)
plt.show  ()
