import matplotlib.pyplot
import numpy
import os.path

# load back leg data
backLegSensorValues = numpy.load(os.path.join('data', 'backLegSensorValues.npy'))
# load front leg data
frontLegSensorValues = numpy.load(os.path.join('data', 'frontLegSensorValues.npy'))

# Visualization
matplotlib.pyplot.plot(backLegSensorValues, label='back leg', linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues, label='front leg')
matplotlib.pyplot.title('Visualization')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

