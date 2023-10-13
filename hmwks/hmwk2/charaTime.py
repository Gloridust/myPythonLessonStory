# 输入两个字符串
text = input("请输入要检查的文本字符串: ")
characters = input("请输入要查找的字符集合: ")

# 初始化一个字典用于统计字符出现的次数
char_count = {}

# 遍历输入字符串中的每个字符
for char in text:
    # 如果字符在字符集合中，增加字符计数
    if char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# 统计字符出现次数之和
total_count = 0
for char in char_count:
    total_count += char_count[char]

# 输出字符集合中字符出现的总次数
print(f"字符集合中字符出现的总次数为: {total_count}")
