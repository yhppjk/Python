#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpDataProcess - Helper providing physical data from electrical measures            JYC-2021
#-----------------------------------------------------------------------------------------------------------------------

from hlpDataStruct import ElectricalMeasures, PhysicalMeasures

class PhysicalConversions:
    PMes = PhysicalMeasures()

    def ConvertToPhysical(self, EMes:ElectricalMeasures):
        #
        # ===ToDo===
        #
        self.PMes.Direction    = 0   # convert EMes.Girouette    Voltage  to integer position    (0 to 7)
        self.PMes.Station      = 0   # convert EMes.Encodeur     GrayCode to integer position    (0 to 15)
        self.PMes.Humidite     = 0   # convert EMes.Humidimetre  25Hz : 100% / 100Hz : 0%        (constraint in the range 0-100)
        self.PMes.Temperature  = 0   # convert EMes.Thermometre  °C = (Vcapteur x 100) - 273,15
        self.PMes.Luminosite   = 0   # convert EMes.Luxmetre     4,8V : 0 lux / 0V : 150000 lux  (constraint in the range 0-150000)
        self.PMes.Pluviometrie = 0   # convert EMes.Pluviometre  1 imp. = 0,2794mm
        self.PMes.Vitesse      = 0   # convert EMes.Anemometre   1 imp./s = 2,4km/h
