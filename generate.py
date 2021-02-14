import pyrosim.pyrosim as pyrosim

# size
length = 1
width = 1
height = 1


def Create_World():
    # box
    pyrosim.Start_SDF("world.sdf")
    # the world
    pyrosim.Send_Cube(name="Box", pos=[0, 0, 0.5], size=[length, width, height])
    # End
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    # Robot Torso
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 0.5], size=[length, width, height])
    # Add a joint that connects Leg to Torso
    pyrosim.Send_Joint(name="Torso_Leg", parent="Torso", child="Leg", type="revolute", position="0.5 0 1.0")
    # Robot Leg
    pyrosim.Send_Cube(name="Leg", pos=[1, 0, 1.5], size=[length, width, height])
    # End
    pyrosim.End()


Create_World()
Create_Robot()
