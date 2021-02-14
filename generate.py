import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

x = 1
y = 1
z = 1

pyrosim.Send_Cube(name="Box", pos=[0, 0, 0], size=[x, y, z])
pyrosim.Send_Cube(name="Box2", pos=[0.5, 0, 1], size=[x, y, z])

# Finish
pyrosim.End()
