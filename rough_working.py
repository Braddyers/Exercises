user_input = "1 2 3"

numbers = user_input.split()

revese_numbers = numbers[::-1]

first_element = numbers[0:1]

last_element = numbers[-1:]

new_list = first_element + numbers + revese_numbers + last_element

res_list = new_list * 2

"""
print(numbers)
print(revese_numbers)
print(first_element)
print(last_element)
print(new_list)
"""

print(res_list)