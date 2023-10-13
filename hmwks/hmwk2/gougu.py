import math

x1 = float(input("请输入第一个点的 x 坐标: "))
y1 = float(input("请输入第一个点的 y 坐标: "))

x2 = float(input("请输入第二个点的 x 坐标: "))
y2 = float(input("请输入第二个点的 y 坐标: "))

mdistance = abs(x1 - x2) + abs(y1 - y2)

print("两点之间的曼哈顿距离为:", mdistance)
