import math

# 获取输入数据，假设数据以空格分隔
data = input("输入要计算几何平均数的数据（用空格分隔）: ")
# 将输入数据分割成单独的数字
nums = [float(x) for x in data.split()]

# 计算几何平均数
def geometric_mean(nums):
    product = 1.0
    for num in nums:
        product *= num
    geometric_mean = math.pow(product, 1.0 / len(nums))
    return geometric_mean

# 调用函数计算几何平均数
result = geometric_mean(nums)
print("几何平均数为:",result)