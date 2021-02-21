import os.path
import pybullet as p
import time as t
import pybullet_data
import numpy
from pyrosim import pyrosim


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# gravity
p.setGravity(0, 0, -9.8)

# add floor
planedId = p.loadURDF("plane.urdf")
# the robot body data
planedId = p.loadURDF("body.urdf")

# world
p.loadSDF("world.sdf")

# pyrosim setup
pyrosim.Prepare_To_Simulate("body.urdf")

# numpy vector
backLegSensorValues = numpy.zeros(10000)


# simulated world
for i in range(1000):
    p.stepSimulation()
    # Adding a touch sensor to the back leg
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    # print sensor values
    print(backLegTouch)
    t.sleep(1 / 60)

p.disconnect()

numpy.save(os.path.join('data', 'backLegSensorValues.npy'), backLegSensorValues)
print(backLegSensorValues)

