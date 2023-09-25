import tkinter as tk
root = tk.Tk()
root.title("猜数字")
root.geometry("500x250")


import random

random_number = random.randint(0, 100)  # 生成一个随机数，并将其存储在变量random_number中
print("猜数字小游戏")
input_number = int(input("输入一个整数："))

while input_number != random_number:
    if input_number > random_number:
        print("大了")
    else:
        print("小了")
    
    input_number = int(input("再次输入一个整数："))  # 读取用户的输入，并将其存储在input_number中

print("Yes, you're right!")