import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# test_times = 5
# for i in range(test_times):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
