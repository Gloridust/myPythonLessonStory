text = input("请输入要检查的文本字符串: ")
characters = input("请输入要查找的字符集合: ")

# 初始化字典用于次数统计
char_count = {}

# 遍历输入字符串中的每个字符
for char in text:
    # 如果字符在字符集合中，增加字符计数
    if char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# 输出次数
for char, count in char_count.items():
    print(f"'{char}' 出现 {count} 次")
