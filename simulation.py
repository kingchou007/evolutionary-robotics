import constants as c
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import time as t


class SIMULATION:
    def __init__(self, directOrGui):

        if directOrGui == "DIRECT":

            self.physicsClient = p.connect(p.DIRECT)

        elif directOrGui == "GUI":

            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):

        for i in range(350):

            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            t.sleep(1 / 500)

    def Get_Fitness(self):

        self.robot.Get_Fitness()

    def __del__(self):

        p.disconnect()
