import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")

x = 1
y = 1
z = 1

# pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[1, 1, 1])
pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[x, y, z])

# Finish
pyrosim.End()