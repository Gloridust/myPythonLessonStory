# 获取用户输入的学号
student_id = input("请输入你的学号: ")

# 使用字符串切片提取班级号
class_number = student_id[4:6]

# 输出班级号
print("你的班级号是 " + class_number)
