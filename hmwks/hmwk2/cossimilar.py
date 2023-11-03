import numpy as np

# 定义两个示例向量
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# 计算余弦相似度
dot_product = np.dot(vector1, vector2)
magnitude1 = np.linalg.norm(vector1)
magnitude2 = np.linalg.norm(vector2)

cosine_similarity = dot_product / (magnitude1 * magnitude2)

print("余弦相似度:", cosine_similarity)