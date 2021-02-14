import pyrosim.pyrosim as pyrosim

# box
pyrosim.Start_SDF("box.sdf")

# size
length = 1
width = 1
height = 1


# position
x = 0
y = 0
z = 0.5

# tower
for i in range(10):
    for x in range(6):
        for y in range(5):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
            y = y + 1
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
        x = x + 1
    # pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    z = z + 1
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9

# Finish
pyrosim.End()

