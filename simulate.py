import pybullet as p
import time as t
import pybullet_data
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

# simulated world
for i in range(1000):
    p.stepSimulation()
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    t.sleep(1 / 60)

p.disconnect()
