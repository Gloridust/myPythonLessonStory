def filter_strings(data):
    # 过滤
    filtered_data = []

    for string in data:
        # 统计每个字符出现的次数
        char_counts = {}
        for char in string:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # 检查是否有超过一半长度的重复字符
        if all(count <= len(string) / 2 for count in char_counts.values()):
            filtered_data.append(string)

    return filtered_data

# 定义示例列表
data = ['aadd','asd','anb','aaas']

# 过滤字符串
filtered_strings = filter_strings(data)
print(filtered_strings)

