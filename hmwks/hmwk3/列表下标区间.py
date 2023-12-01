def get_sublist(lst, start, end):  
    return lst[start-1:end]  # Python的索引是从0开始的，所以要减1  
  
# 测试代码  
lst = [1, 2, 3, 4, 5, 6]  
start = 2  
end = 5  
print(get_sublist(lst, start, end))  # 输出：[3, 4, 5, 6]