import random  
  
# 生成包含20个随机数的列表  
numbers = [random.randint(0, 100) for _ in range(20)]  
print("原始列表：", numbers)  
  
# 将前10个元素升序排列，后10个元素降序排列  
numbers[:10] = sorted(numbers[:10])  
numbers[10:] = sorted(numbers[10:], reverse=True)  
print("排列后的列表：", numbers)