import os
from hillclimber import HILL_CLIMBER

# test_times = 5
# for i in range(test_times):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()
