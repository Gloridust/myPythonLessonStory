# 用户输入
source = input("输入用于检查的字符串：")
target = input("输入被检查的字符串：")  

# 遍历字典
def count_occurrences(source, target):  
    # 创建一个字典来存储字符及其出现次数
    char_count = {}  
      
    # 遍历目标字符串中的所有字符
    for char in target:  
        # 计数  
        if char in source:  
            if char in char_count:  
                char_count[char] += 1
            else:  
                char_count[char] = 1
      
    return char_count  
  
# 结果
result = count_occurrences(source, target)  
print(result) 



# source = input("输入用于检查的字符串："): 这行代码用于获取用户的输入，要求用户输入一个字符串，然后将用户输入的字符串存储在变量 source 中。

# target = input("输入被检查的字符串："): 这行代码也用于获取用户的输入，要求用户输入另一个字符串，然后将用户输入的字符串存储在变量 target 中。

# def count_occurrences(source, target):: 这行代码定义了一个名为 count_occurrences 的函数，该函数接受两个参数，source 和 target，这两个参数分别表示要检查的源字符串和被检查的目标字符串。

# char_count = {}: 在函数内部，创建了一个空的字典，用于存储字符及其出现次数的统计信息。字典的变量名为 char_count。

# for char in target:: 这是一个循环，它用来遍历目标字符串 target 中的每个字符。在每次迭代中，当前字符被赋值给变量 char。

# if char in source:: 这是一个条件语句，它检查当前字符 char 是否存在于源字符串 source 中。

# 如果条件成立，表示字符 char 在源字符串中存在，然后执行下面的代码块：

# if char in char_count:: 这是另一个条件语句，它检查当前字符 char 是否已经在 char_count 字典中存在。
# 如果条件成立，表示字符 char 在 char_count 字典中已经有统计信息，那么将该字符的出现次数加一。
# 如果条件不成立，表示字符 char 还没有被统计过，那么在 char_count 字典中创建一个新的键值对，键是字符 char，值初始化为1。
# return char_count: 函数返回存储了字符及其出现次数统计信息的 char_count 字典。

# result = count_occurrences(source, target): 这行代码调用了 count_occurrences 函数，传递了用户输入的源字符串 source 和目标字符串 target 作为参数，并将函数返回的结果存储在 result 变量中。

# print(result): 最后，将统计结果（char_count 字典）打印到屏幕上，显示字符在目标字符串中出现的次数。