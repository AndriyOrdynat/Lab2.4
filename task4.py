import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

a_val = list(range(30, -30, -1))
result = pd.DataFrame({'a': a_val, 'x1': [None]*len(a_val), 'x2': [None]*len(a_val), 'x3': [None]*len(a_val), 'x4': [None]*len(a_val)})
result.set_index('a', inplace=True)

for a in a_val:
    A = np.array([[1, -4, 3, -1],[1,2,5,-1],[2,-3,0,4],[-1,-2,-3,-4]])
    b = np.array([a, 2, 5, -5])
    x = np.linalg.solve(A, b)
    result.loc[a, ['x1', 'x2', 'x3', 'x4']] = x

print(result)