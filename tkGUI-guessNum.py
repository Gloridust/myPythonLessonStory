import tkinter as tk    # 导入Tkinter库，用于创建GUI界面
import random   # 导入random用于生成随机数

# 生成随机数
random_number = random.randint(0, 100)

# 初始化GUI窗口
root = tk.Tk()
root.title("猜数字")
root.geometry("300x150")

# 创建标签，用于显示游戏标题
title_label = tk.Label(root, text="猜数字小游戏")
title_label.pack()  #将标签放置到主窗口中，使其在默认位置垂直堆叠在其他GUI元素之上

# 创建输入框，用于接收用户输入
input_entry = tk.Entry(root)
input_entry.pack()  #将输入框放置到主窗口中，使其在默认位置垂直堆叠在其他GUI元素之上

# 创建按钮，用于提交用户的猜测
submit_button = tk.Button(root, text="提交", command=lambda: check_guess())
submit_button.pack()

# 创建标签，用于显示游戏结果
result_label = tk.Label(root, text="")
result_label.pack()

# 定义检查猜测的函数
def check_guess():
    user_guess = input_entry.get()  # 获取用户输入
    try:
        user_guess = int(user_guess)  # 尝试将用户输入转换为整数
        if user_guess > random_number:
            result_label.config(text="大了")
        elif user_guess < random_number:
            result_label.config(text="小了")
        else:
            result_label.config(text="Yes, you're right!")  # 用户猜中数字
    except ValueError:
        result_label.config(text="请输入一个整数")  # 处理用户输入非整数的情况

# 运行GUI应用程序的主循环
root.mainloop()

# 建议：
# 1. 如果你打算在GUI界面中实现这个游戏，可以考虑将用户输入的部分替换为GUI元素，而不是使用文本输入和打印消息。
# 2. 对于Tkinter GUI，你可以创建一个输入框和一个文本标签来处理用户输入和显示消息，而不是使用命令行的input和print。
# 3. 如果用户输入非整数，代码会引发异常。可以添加异常处理来处理这种情况，以确保程序不会崩溃。