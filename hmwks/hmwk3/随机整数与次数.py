import random  
from collections import Counter  
  
# 生成1000个0~100的随机整数  
numbers = [random.randint(0, 100) for _ in range(1000)]  
  
# 使用Counter来统计每个元素的出现次数  
counts = Counter(numbers)  
  
# 打印每个元素及其出现次数  
for num, count in counts.items():  
    print(f"数字 {num} 出现了 {count} 次")