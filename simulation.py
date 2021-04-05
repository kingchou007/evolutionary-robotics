import constants as c
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import time as t


class SIMULATION:
    def __init__(self, directOrGui, solutionID):
        self.directOrGui = directOrGui
        self.id = solutionID

        if directOrGui == "DIRECT":

            self.physicsClient = p.connect(p.DIRECT)

        elif directOrGui == "GUI":

            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):

        for i in range(400):
            if self.directOrGui == 'GUI':
                t.sleep(1 / 500)
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

    def Get_Fitness(self):

        self.robot.Get_Fitness(self.id)

    def __del__(self):

        p.disconnect()
