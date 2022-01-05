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
        # convert EMes.Girouette    Voltage  to integer position    (0 to 7)
        # if(self.EMes.Girouette < 3.8 and self.EMes.Girouette > 3.3): self.PMes.Direction    = 0         #North
        # if(self.EMes.Girouette < 2.3 and self.EMes.Girouette > 2): self.PMes.Direction    = 1         #Northeast

        # if(self.EMes.Girouette < 0.48 and self.EMes.Girouette > 0.33): self.PMes.Direction    = 2         #east
        # if(self.EMes.Girouette < 0.92 and self.EMes.Girouette > 0.6): self.PMes.Direction    = 3         #Southeast


        # if(self.EMes.Girouette < 1.43 and self.EMes.Girouette > 1.2): self.PMes.Direction    = 4         #South
        # if(self.EMes.Girouette < 3.1 and self.EMes.Girouette > 2.9): self.PMes.Direction    = 5        #SouthWest

        # if(self.EMes.Girouette  > 4.4): self.PMes.Direction    = 6         #West
        # if(self.EMes.Girouette < 4.2 and self.EMes.Girouette > 3.8): self.PMes.Direction    = 7         #Northwest





        self.PMes.Direction    = "North"
        self.PMes.Station      = 0   # convert EMes.Encodeur     GrayCode to integer position    (0 to 15)
        self.PMes.Humidite     = 0   # convert EMes.Humidimetre  25Hz : 100% / 100Hz : 0%        (constraint in the range 0-100)
        self.PMes.Temperature  = 0   # convert EMes.Thermometre  °C = (Vcapteur x 100) - 273,15
        self.PMes.Luminosite   = 0   # convert EMes.Luxmetre     4,8V : 0 lux / 0V : 150000 lux  (constraint in the range 0-150000)
        self.PMes.Pluviometrie = 0   # convert EMes.Pluviometre  1 imp. = 0,2794mm
        self.PMes.Vitesse      = 0   # convert EMes.Anemometre   1 imp./s = 2,4km/h
