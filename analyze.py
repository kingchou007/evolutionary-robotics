import matplotlib.pyplot
import numpy
import os.path

backLegSensorValues = numpy.load(os.path.join('data', 'backLegSensorValues.npy'))
frontLegSensorValues = numpy.load(os.path.join('data', 'frontLegSensorValues.npy'))

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()