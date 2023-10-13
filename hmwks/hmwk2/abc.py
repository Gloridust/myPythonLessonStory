# 输入三个英文单词
word1 = input("请输入第一个单词: ")
word2 = input("请输入第二个单词: ")
word3 = input("请输入第三个单词: ")

# 将单词放入一个列表
words = [word1, word2, word3]

# 使用sorted()函数对单词列表进行排序
sorted_words = sorted(words)

# 输出排序后的单词
print("按字母表顺序排序后的单词:")
for word in sorted_words:
    print(word)