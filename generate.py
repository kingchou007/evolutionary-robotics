import pyrosim.pyrosim as pyrosim

# size
length = 1
width = 1
height = 1


def Create_World():
    # box
    pyrosim.Start_SDF("world.sdf")
    # the world
    pyrosim.Send_Cube(name="Box", pos=[-2, 2, 0.5], size=[length, width, height])
    # End
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    # Robot Torso
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
    # Connect BackLeg to Torso with one joint
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position="2.0 0.0 1.0")
    # Robot FrontLeg
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
    # Connect FrontLeg to Torso with a second joint.
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position="1.0 0.0 1.0")
    # The other BackLeg
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])

    # End
    pyrosim.End()


Create_World()
Create_Robot()
