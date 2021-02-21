import matplotlib.pyplot
import numpy as np
import os.path

backLegSensorValues = np.load(os.path.join('data', 'backLegSensorValues.npy'))
# print(backLegSensorValues)
matplotlib.pyplot.show(backLegSensorValues)