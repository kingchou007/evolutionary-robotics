import pyrosim.pyrosim as pyrosim

# size
length = 1
width = 1
height = 1


def Create_World():
    # box
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[length, width, height])
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.5], size=[length, width, height])
    pyrosim.End()


Create_World()
Create_Robot()