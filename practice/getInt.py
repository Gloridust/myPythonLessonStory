input = input("请输入一个三位以上的整数：")
try:
    number = int(input)
    if number < 100:
        print("输入的数字不是三位以上的整数。")
    else:
        digit = (number // 100) % 10
        print("百位以上的数字是：", digit)
except ValueError:
    print("输入无效，请输入一个有效的整数。")

