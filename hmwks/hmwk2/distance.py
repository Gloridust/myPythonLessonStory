# 输入第一个点的坐标
x1 = input("请输入第一个点的 x 坐标: ")
y1 = input("请输入第一个点的 y 坐标: ")

# 输入第二个点的坐标
x2 = input("请输入第二个点的 x 坐标: ")
y2 = input("请输入第二个点的 y 坐标: ")

# 计算曼哈顿距离
distance = abs(x1 - x2) + abs(y1 - y2)

# 输出距离
print("两点之间的距离为:", distance)
