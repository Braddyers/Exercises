fruits = ["apple", "banana", "orange"]
index = 0
place_in_list = 0

for fruit in fruits:
    index += 1
    
    if index == 1:
        place_in_list = "first"
    elif index == 2:
        place_in_list = "second"
    elif index == 3:
        place_in_list = "third"
    
    print(f"The {place_in_list} fruit is {fruit} and has a character length of {len(fruit)}.")

print(f"The number of fruit in the list is therefore {len(fruits)}.")
