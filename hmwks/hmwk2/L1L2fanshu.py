import numpy as np

a = np.array([1, 2, 3, 4, 5])

L1_norm = np.linalg.norm(a, ord=1)  
print("L1 norm:", L1_norm)

L2_norm = np.linalg.norm(a, ord=2)  
print("L2 norm:", L2_norm)
