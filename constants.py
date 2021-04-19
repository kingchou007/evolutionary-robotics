import numpy
# back leg
backLegAmplitude = numpy.pi/6
backLegFrequency = 10
backLegPhaseOffset = 0

# front leg
frontLegAmplitude = -numpy.pi/6
frontLegFrequency = 10
frontLegPhaseOffset = 0

motorForce = 55

timeSteps = 3000
gravity = -9.8
sleepTime = 1.0/300.0

numberOfGenerations = 20

# define population size
populationSize = 20

# number of motors
numMotorNeurons = 4

# number of sensors
numSensorNeurons = 8

motorJointRange = 0.27
