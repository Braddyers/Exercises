
lst1 = "1,2,3,4,5"

lst2 = "2,4,6"

lst1 = lst1.split(",")
lst2 = lst2.split(",")

lst3 = []

for number in lst1:
    if number not in lst2:
        lst3.append(number)

print(lst3)