import nidaqmx
from nidaqmx.constants import LineGrouping

import os; os.system('cls')


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan(lines = "Dev1/port0/line0:7", line_grouping = LineGrouping.CHAN_PER_LINE)

    data = task.read()
    print("8 bits read: ", data)


with nidaqmx.Task() as task:
    task.di_channels.add_di_chan(lines = "Dev1/port0/line0:7", line_grouping = LineGrouping.CHAN_FOR_ALL_LINES)

    data = task.read()
    print("1 byte read: ", data)
