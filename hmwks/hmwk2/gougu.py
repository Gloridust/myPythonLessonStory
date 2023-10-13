import math

# 输入已知的两边长度和夹角（以度为单位）
a = float(input("请输入第一边的长度: "))
b = float(input("请输入第二边的长度: "))
angle_degrees = float(input("请输入两边之间的夹角（度）: "))

# 将夹角从度转换为弧度
angle_radians = math.radians(angle_degrees)

# 使用余弦定理计算第三边的长度
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_radians))

# 输出第三边的长度
print("第三边的长度为:", c)