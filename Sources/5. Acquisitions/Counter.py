import nidaqmx
from nidaqmx.constants import Edge
import time


with nidaqmx.Task() as task:
    task.ci_channels.add_ci_count_edges_chan(counter="dev1/ctr0", edge=Edge.FALLING).ci_count_edges_term = "/dev1/pfi0"
    task.start()
    time.sleep(1)
    data = task.read()
    print("Frequency= ", data , " Hz")


