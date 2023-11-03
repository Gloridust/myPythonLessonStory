import numpy as np

# 输入向量
vector = np.array([1, 2, 3, 4, 5])

# 权向量
weights = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

# 计算加权平均
weighted_average = np.dot(vector, weights)

print("加权平均:", weighted_average)