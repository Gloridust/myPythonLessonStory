# 读取正整数n
n = int(input())

# 对于每个输入的十六进制数，进行转换并输出
for _ in range(n):
    hex_number = input()  # 读取十六进制数
    decimal_number = int(hex_number, 16)  # 将十六进制数转换为十进制数
    octal_number = oct(decimal_number)[2:]  # 将十进制数转换为八进制数，并去除前缀'0o'
    print(octal_number)
