#

def create_pattern(numbers, repeats):
    doubled = numbers + numbers
    final_pattern = doubled * repeats
    return final_pattern

numbers = [1, 2, 3]
repeats = 2

#numbers = [4, 5]
#repeats = 3

#numbers = [10]
#repeats = 1

final_pattern = create_pattern(numbers, repeats)

print(final_pattern)

