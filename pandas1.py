import pandas as pd

data = {'Name': ['A', 'B'], 'Age': [20, 25]}
df = pd.DataFrame(data)
print(df)


from scipy.linalg import inv
import numpy as np

A = np.array([[1, 2], [3, 4]])
A_inv = inv(A)

print(A_inv)
