# numbers = input("Input string of numbers: ")
# prefix = input("Input prefix string: ")
# Expected output: +1123 +1456 +1789
numbers = "123 456 789"
prefix = "+1"
string_2 = []

string_1 = numbers.split()

for i in range(len(string_1)):
    new_num = prefix + string_1[i] 
    string_2.append(new_num)
    numbers_2 = " ".join(string_2)

print(numbers_2)

# do the same but with enumerate() function
