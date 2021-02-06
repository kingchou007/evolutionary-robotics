import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)

# pybullet (remember, we shortened it to p at the top of this file) to read in the world called box.
p.loadSDF("box.sdf")

# simulated world
for i in range(1000):
    p.stepSimulation()
    t.sleep(1/60)

p.disconnect()

