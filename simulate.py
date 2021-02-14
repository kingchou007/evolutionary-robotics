import pybullet as p
import time as t
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# add floor
planedId = p.loadURDF("plane.urdf")

# read in the world called box.
p.loadSDF("box.sdf")

# simulated world
for i in range(1000):
    p.stepSimulation()
    t.sleep(1 / 60)

p.disconnect()
