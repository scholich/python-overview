from pylab import np

with open('ML Sample Data/RL 1k/TIME/Gaussian F=0.400 DC=50 A=0.50 TIME [2019-01-18 13_58_52.56].csv') as f:
    arr = np.array([float(item) for item in f.readlines()])
    print(arr)