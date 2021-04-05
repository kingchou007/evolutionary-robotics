from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system("rm tmp*.txt")
        self.nextAvailableID = 0
        self.parents = dict()
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        for i in range(c.populationSize):
            self.parents[i].Start_Simulation("DIRECT")

        for i in range(c.populationSize):
            self.parents[i].Wait_For_Simulation_To_End()

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        pass
        # self.Spawn()
        # self.Mutate()
        # self.child.Evaluate("DIRECT")
        # self.Print()
        # self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def Print(self):
        print("-------------------------------------------------------")
        print("Parent: " + str(self.parent.fitness), " ", "Child: " + str(self.child.fitness))
        print("-------------------------------------------------------")

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass
