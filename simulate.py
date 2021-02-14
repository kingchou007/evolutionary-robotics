import pybullet as p
import time as t
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Forces
p.setGravity(0, 0, -9.8)

# add floor
planedId = p.loadURDF("plane.urdf")

# the robot body
planedId = p.loadURDF("body.urdf")

# world
p.loadSDF("world.sdf")


# simulated world
for i in range(1000):
    p.stepSimulation()
    t.sleep(1 / 60)

p.disconnect()
