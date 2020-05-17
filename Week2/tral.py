import numpy as np
import pandas as pd
data = pd.read_csv('ex1data2.txt', sep = ',', header = None)
X = data.iloc[:,0:2]                                                    # read first two columns into X
y = data.iloc[:,2]                                                      # read the third column into y
print(y)
m = len(y)                                                              # no. of training samples
print(data.head())                                                      # view first few rows of the data
ones = np.ones((m,1))                                                   # initializing an array of 1s as value for intercept terms
X = np.hstack((ones, X))
alpha = 0.01
iterations = 500
theta = np.zeros((3,1))
y = y[:,np.newaxis]
