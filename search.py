import os

# test times
test_times = 5

# run
for i in range(test_times):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")