import numpy as np

matrix = np.array([[1, 2, 3],
                  [2, 4, 5],
                  [3, 5, 9]])

itis = np.allclose(matrix, matrix.T)

if itis:
    print("输入的矩阵是对称矩阵")
else:
    print("输入的矩阵不是对称矩阵")

# matrix是输入的矩阵。
# matrix.T是矩阵的转置，它是一个新的矩阵，通过交换原矩阵的行和列得到。
# np.allclose(a, b)是NumPy函数，用于比较两个数组或矩阵a和b是否非常接近，通常使用默认的数值容差。
# 如果matrix和matrix.T非常接近，np.allclose返回True，否则返回False。