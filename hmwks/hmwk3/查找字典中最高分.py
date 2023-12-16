# 定义字典
scores = {
    "Alice": 92,
    "Bob": 87,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 72,
    "Frank": 88,
    "Grace": 98
}

# 计算
max_score = max(scores.values())
min_score = min(scores.values())
average_score = sum(scores.values()) / len(scores)

# 查找
top_students = [name for name, score in scores.items() if score == max_score]

print(top_students)