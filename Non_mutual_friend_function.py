list3 = []
list4 = []

def not_mutual_friends(list1, list2):
    for name in list1:
        if name not in list2:
            list3.append(name)
    for name in list2:
        if name not in list1:
            list4.append(name)
    final_list = list3 + list4
    return final_list

list1 = ["John", "Emma", "Mike", "Sarah"]
list2 = ["Emma", "Tom", "Sarah", "Peter"]

res_list = not_mutual_friends(list1, list2)

print(res_list)
