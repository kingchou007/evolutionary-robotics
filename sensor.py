import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import os.path


class SENSOR:
    def __init__(self, link_name):
        self.linkName = link_name
        self.values = numpy.zeros(c.timeSteps)

    def Get_Value(self, time_step):
        self.values[time_step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save(os.path.join('data', 'SensorValues.npy'), self.values)
