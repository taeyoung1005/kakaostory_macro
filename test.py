import pyperclip

stra_list = [1, 2, 3, 4, 5, 6, 7, 8]
str_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in str_list:
    for j in stra_list:
        if j not in str_list:
            str_list.append(j)
        else:
            stra_list.pop(0)
    print(i)