import numpy as np

# 创建一个示例矩阵
matrix = np.array([[1, 2, 3],
                  [2, 4, 5],
                  [3, 5, 9]])

# 计算矩阵的迹
trace = np.trace(matrix)

print("矩阵的迹为:", trace)