# 外层循环，迭代变量a从0到1000
for a in range(1001):
    # 中层循环，嵌套在外层循环内，迭代变量b从0到1000
    for b in range(1001):
        # 内层循环，嵌套在中层循环内，迭代变量c从0到1000
        for c in range(1001):
            # 检查当前a、b、c是否满足两个条件：
            # 1. a + b + c等于1000
            # 2. a的平方加上b的平方等于c的平方（满足勾股定理）
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                # 如果条件满足，打印输出a、b、c的值
                # print("a = ",a, "b = ",b, "c = ",c)
                print(f"a = {a}, b = {b}, c = {c}")

