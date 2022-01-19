#-----------------------------------------------------------------------------------------------------------------------
# Weather Station Project - hlpDataProcess - Helper providing physical data from electrical measures            JYC-2021
#-----------------------------------------------------------------------------------------------------------------------

from hlpDataStruct import ElectricalMeasures, PhysicalMeasures
from hlpDataMeasure import DataMeasure

class PhysicalConversions:
    PMes = PhysicalMeasures()

    def ConvertToPhysical(self, EMes:ElectricalMeasures):
        #
        # ===ToDo===
        #
        # convert EMes.Girouette    Voltage  to integer position    (0 to 7)
        if(EMes.Girouette < 3.8 and EMes.Girouette > 3.3): self.PMes.Direction    = "north"         #North
        if(EMes.Girouette < 2.3 and EMes.Girouette > 2): self.PMes.Direction    = "Northeast"         #Northeast

        if(EMes.Girouette < 0.48 and EMes.Girouette > 0.33): self.PMes.Direction    = "east"         #east
        if(EMes.Girouette < 0.92 and EMes.Girouette > 0.6): self.PMes.Direction    = "Southeast"         #Southeast


        if(EMes.Girouette < 1.43 and EMes.Girouette > 1.2): self.PMes.Direction    = "South"        #South
        if(EMes.Girouette < 3.1 and EMes.Girouette > 2.9): self.PMes.Direction    = "SouthWest"        #SouthWest

        if(EMes.Girouette  > 4.4): self.PMes.Direction    = "west"         #West
        if(EMes.Girouette < 4.2 and EMes.Girouette > 3.8): self.PMes.Direction    = "Northwest"        #Northwest







        self.PMes.Station      = EMes.Encodeur  # convert EMes.Encodeur     GrayCode to integer position    (0 to 15)
        self.PMes.Humidite     = (100-EMes.Humidimetre)*100/75   # convert EMes.Humidimetre  25Hz : 100% / 100Hz : 0%        (constraint in the range 0-100)
        self.PMes.Temperature  = (EMes.Thermometre *100)-273.15  # convert EMes.Thermometre  °C = (Vcapteur x 100) - 273,15

        self.PMes.Luminosite   = (4.8- EMes.Luxmetre )*150/4.8   # convert EMes.Luxmetre     4,8V : 0 lux / 0V : 150000 lux  (constraint in the range 0-150000)
        self.PMes.Pluviometrie = EMes.Pluviometre * 0.2794   # convert EMes.Pluviometre  1 imp. = 0,2794mm
        self.PMes.Vitesse      = EMes.Anemometre * 2.4   # convert EMes.Anemometre   1 imp./s = 2,4km/h
