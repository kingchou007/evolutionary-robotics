import numpy
# back leg
backLegAmplitude = numpy.pi/4
backLegFrequency = 10
backLegPhaseOffset = 0

# front leg
frontLegAmplitude = -numpy.pi/4
frontLegFrequency = 10
frontLegPhaseOffset = 0

motorForce = 25

timeSteps = 1000
gravity = -9.8
sleepTime = 1.0/300.0

numberOfGenerations = 20

# define population size
populationSize = 20

# number of motors
numMotorNeurons = 4

# number of sensors
numSensorNeurons = 8

motorJointRange = 1
