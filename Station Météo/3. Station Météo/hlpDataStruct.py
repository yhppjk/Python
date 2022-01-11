#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpDataStruct - Helper Data Exchange Model-Controller                               JYC-2021
#-----------------------------------------------------------------------------------------------------------------------


from tkinter.constants import CHAR


class ElectricalMeasures:
    # ===ToDo===  add a flag to Reset Pluviometre
    #
    # set by MainWindow_support\GUIDisplay\BtnReset-event - used by hlpDataMeasure\FastRead

    Humidimetre   : float = 0
    HumidimetreAX : float = []
    HumidimetreAY : float = []
    Girouette     : float = 0
    Thermometre   : float = 0
    Luxmetre      : float = 0
    Pluviometre   : int   = 50
    Encodeur      : int   = 0
    Anemometre    : int   = 0
    DureeMesures  : int   = 0
    TempsBoucleR  : int   = 0
    TempsBoucleL  : int   = 0
    BtnReset : bool = False

class PhysicalMeasures:
    Direction    : str = "0"
    Vitesse      : float = 0
    Temperature  : float = 0
    Luminosite   : float = 0
    Humidite     : float = 0
    Pluviometrie : float = 0
    Station      : int   = 0

class ErrorMeasures:
    CurrentCode       = 0
    ErrorFlag         = False
    ErrorFunctionName = ""
    ErrorCode         = 0
    ErrorType         = ""
    ErrorMessage      = ""

EMes  = ElectricalMeasures()
PMes  = PhysicalMeasures()
ErMes = ErrorMeasures()

