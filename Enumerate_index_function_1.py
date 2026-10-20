# Below is function that returns 2 lists (index list and numbers list) which 
# meet the following criteria:

# If the number in the list is < 50
# OR
# If the number in the list is divisible by 3

def index_function(lst):
    indices_lst = []
    num_lst = []
    for index, num in enumerate(lst):
        if num < 50 or num % 3 == 0:
            indices_lst.append(index)
            num_lst.append(num)
    return indices_lst, num_lst

# Example list:
lst = [80, 4, 99, 36, 34]

lst_index, lst_num = index_function(lst)

print(lst_index)
print(lst_num)