lst = ["cat", "dog", "bird", "fish", "hamster", "snake", "rabbit", "turtle"]

lst_mid = len(lst) // 2

if len(lst) % 2 == 0:
    sliced_lst = lst[lst_mid - 1: lst_mid + 1]
else:
    sliced_lst = lst[lst_mid - 1: lst_mid + 2]


print(len(lst))
print(lst_mid)
print(sliced_lst)

