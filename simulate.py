from simulation import SIMULATION
import sys

directOrGui = sys.argv[1]
simulationID = sys.argv[2]
simulation = SIMULATION(directOrGui, solutionID)
simulation.Run()
simulation.Get_Fitness()