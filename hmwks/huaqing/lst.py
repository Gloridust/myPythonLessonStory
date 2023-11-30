list = [2,6,8,0,4,9,3]
i = 0

while i < len(list):
    for j in range(i+1, len(list)):
        if list[j] < list[i]:
            list[i], list[j] = list[j], list[i]
    i += 1

print(list)
