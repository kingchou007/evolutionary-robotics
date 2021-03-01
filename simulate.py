import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# gravity
p.setGravity(0, 0, -9.8)

# add floor
planedId = p.loadURDF("plane.urdf")
# the robot body data
robot = p.loadURDF("body.urdf")

# world
p.loadSDF("world.sdf")

# pyrosim setup
pyrosim.Prepare_To_Simulate("body.urdf")

# numpy vector
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

backLegAmplitude = numpy.pi/4
backLegFrequency = 10
backLegPhaseOffset = 0

frontLegAmplitude = numpy.pi/6
frontLegFrequency = 10
frontLegPhaseOffset = numpy.pi/2.9

# unique motor values for front leg and back leg
backLegTargetAngles = backLegAmplitude * \
                      numpy.sin(numpy.linspace(-backLegFrequency * numpy.pi + backLegPhaseOffset,
                                               backLegFrequency * numpy.pi + backLegPhaseOffset, num=1000))
frontLegTargetAngles = frontLegAmplitude * \
                       numpy.sin(numpy.linspace(-frontLegFrequency*numpy.pi + frontLegPhaseOffset,
                                                frontLegFrequency * numpy.pi+frontLegPhaseOffset, num=1000))

# simulated world
for i in range(1000):
    p.stepSimulation()
    # Adding a touch sensor to the back leg
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    # Adding a touch sensor to the front leg
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # add back leg motors
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=backLegTargetAngles[i],
        maxForce=25)

    # add front leg motors
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robot,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=frontLegTargetAngles[i],
        maxForce=25)

    t.sleep(1 / 60)

p.disconnect()
