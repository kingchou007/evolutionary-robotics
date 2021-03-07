import numpy
# back leg
backLegAmplitude = numpy.pi/4
backLegFrequency = 10
backLegPhaseOffset = 0

# front leg
frontLegAmplitude = numpy.pi/4
frontLegFrequency = 5
frontLegPhaseOffset = 0

motorForce = 15  # what is this? 重力不同，运行情况就会不同

timeSteps = 1000
gravity = -9.8
sleepTime = 1.0/60.0
