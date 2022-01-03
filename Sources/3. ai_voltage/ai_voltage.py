import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import time

#-------------------------------------------------------------------------------------
tic = time.perf_counter()
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("dev1/ai0:3", "", TerminalConfiguration.RSE)

    print('\n4 Channels 1 Sample Read: ')
    data = task.read()
    print(data)
print((time.perf_counter() - tic) * 1000, " ms\n")

#-------------------------------------------------------------------------------------
def TaskOpen():
    global task
    task = nidaqmx.Task()
    task.ai_channels.add_ai_voltage_chan("dev1/ai0:3", "", TerminalConfiguration.RSE)

def TaskRead():
    global task
    return task.read()

def TaskClose():
    global task
    task.close()

TaskOpen()

tic = time.perf_counter()
print('\n4 Channels 1 Sample Read: ')
print(TaskRead())
print((time.perf_counter() - tic) * 1000, " ms\n")

TaskClose()
