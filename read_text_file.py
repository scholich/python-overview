from pylab import np

with open('testfile.txt') as f:
    arr = np.array([float(item) for item in f.readlines()])
    print(arr)