import pybullet as p
import time as t

# This creates an object, physicsClient, which handles the physics,
# and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)

# simulated world
for i in range(1000):
    # increases the physics inside the world for a small amount
    p.stepSimulation()
    t.sleep(0.01666666666)

p.disconnect()

