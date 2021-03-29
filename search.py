import os
from hillclimber import HILLCLIMBER

# test_times = 5
# for i in range(test_times):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

hc = HILLCLIMBER()
hc.Evolve()
