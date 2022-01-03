#-----------------------------------------------------------------------------------------------------------------------
import MainWindow_support

#-- DAQmx functions ----------------------------------------------------------------------------------------------------
import nidaqmx
from nidaqmx.constants import Edge, TerminalConfiguration, AcquisitionType, LineGrouping

def DAQmxOpen():
    global bTask, bPrevRead   

    MainWindow_support.GUIBtnReset = False
    MainWindow_support.GUINum      = 0
    bPrevRead                      = True

    DevName = ""
    for device in nidaqmx.system.System.local().devices:
        if device.product_type.find("USB-600") != -1:
            DevName = device.name
            break

    bTask = nidaqmx.Task()
    bTask.di_channels.add_di_chan(lines = DevName+"/port0/line7", line_grouping = LineGrouping.CHAN_PER_LINE)

def DAQmxRead():
    global bPrevRead
    
    if MainWindow_support.GUIBtnReset:                                 # reset <Num> if button-reset pressed
        MainWindow_support.GUIBtnReset = False
        MainWindow_support.GUINum      = 0
    else:
        b = bTask.read()
        if (bPrevRead and (not b)) : MainWindow_support.GUINum += 1    # increment <Num> if falling edge (1 --> 0)
        bPrevRead = b

def DAQmxClose():
    global bTask
    bTask.close()

#-- Timed Loop functions -----------------------------------------------------------------------------------------------
import continuous_threading

def TimedLoopStart():
    global th

    DAQmxOpen()
    th = continuous_threading.PeriodicThread(0.1, TimedLoopJob)  # create thread looped every 100 ms
    th.start()

def TimedLoopJob():  # 100ms loop
    DAQmxRead()

def TimedLoopStop():
    th.join()
    DAQmxClose()

#-- Application start/stop ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    TimedLoopStart()
    MainWindow_support.GUIStart()
    TimedLoopStop()

#-----------------------------------------------------------------------------------------------------------------------
