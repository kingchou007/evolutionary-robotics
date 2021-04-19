from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c


class ROBOT:
    def __init__(self, solutionID):
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        # self.nn = NEURAL_NETWORK("brain.nndf")
        nndfFile = "brain" + str(solutionID) + ".nndf"
        self.nn = NEURAL_NETWORK(nndfFile)
        os.system("rm " + nndfFile)

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, time_step):
        for i in self.sensors:
            self.sensors[i].Get_Value(time_step)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, time_step):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                # self.motors[jointName].Set_Value(self.robot, desiredAngle)
                self.motors[jointName].Set_Value(self.robot, desiredAngle * c.motorJointRange)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self, solutionID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        print(xPosition)

        # file
        file = "tmp" + str(solutionID) + ".txt"
        f = open(file, "w")
        # f = open("fitness.txt", "w")
        # f.write(str(xCoordinateOfLinkZero))
        f.write(str(xPosition))
        f.close()
        os.system("mv " + file + " " + "fitness" + str(solutionID) + ".txt")
