import continuous_threading
import time

import os; os.system('cls')

def TimedLoopFast():
    print("TimedLoop Fast")

def TimedLoopSlow():
    print("TimedLoop Slow")

tf = continuous_threading.PeriodicThread(0.2, TimedLoopFast)
ts = continuous_threading.PeriodicThread(1.0, TimedLoopSlow)

print("Begin")
tf.start()
ts.start()

time.sleep(2.2)

tf.join()
ts.join()
print("End")
