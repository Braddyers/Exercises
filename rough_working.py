"""
lst_1 = [1, 2, 3, 4, 5, 6]
lst_2 = [10, 20, 30, 40]

spliced_lst_1 = lst_1[0:2] + lst_1[-2:]

spliced_lst_2 = lst_2[0:1] + lst_2[-1:]

print(spliced_lst_1)
print(spliced_lst_2)
"""

input_list = [1, 2, 3, 4]

if len(input_list) >= 5:
    spliced_lst = input_list[0:2] + input_list[-2:]
else:
    spliced_lst = input_list[0:1] + input_list[-1:]

print(spliced_lst)