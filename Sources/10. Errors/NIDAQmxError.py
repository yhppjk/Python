import nidaqmx
import nidaqmx.system
from nidaqmx.task import Task
from nidaqmx.constants import TerminalConfiguration

vTask : Task = None

import os; os.system('cls')

try:
    DevName = ""
    for device in nidaqmx.system.System.local().devices:
        if device.product_type.find("USB-600") != -1:
            DevName = device.name
            break
    if DevName == "": raise(nidaqmx.DaqError("Device auto-search failed", -200220, "No task"))

    vTask = nidaqmx.Task                   ("VoltTask")
    vTask.ai_channels.add_ai_voltage_chan  (physical_channel = DevName+"/ai0", terminal_config = TerminalConfiguration.RSE)

    print("Volt = ", vTask.read())

    vTask.close()
except nidaqmx.DaqError as e:
    print(e.__str__())
    if vTask != None: vTask.close()

