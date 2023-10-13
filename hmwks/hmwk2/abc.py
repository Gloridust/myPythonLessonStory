word1 = input("请输入第一个单词: ")
word2 = input("请输入第二个单词: ")
word3 = input("请输入第三个单词: ")

words = [word1, word2, word3]

# 对单词列表进行排序
sorted = sorted(words)

# 输出排序后的单词
print("按字母表顺序排序后的单词:")
for word in sorted:
    print(word)