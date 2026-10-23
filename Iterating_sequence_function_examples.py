# Functions:

# enumerate() function:
text = "HeY"

print("E.g. without enumerate():")
for i in range(len(text)):
    print(f"Position {i}: {text[i]}")

print("E.g. with emumerate():")
for index, letter in enumerate(text):
    print(f"Position {index}: {letter}")

# Output:
# Position 0: H
# Position 1: e
# Position 2: y

# .lower() function:

print("E.g. .lower() function:")
text = "ApPle BanAna oRaNge"
fruits = text.lower()
print(fruits)

# Output:
# apple banana cherry

# .split() function:

# E.g. 1
print("E.g.1 .split() function:")
text = "apple banana orange"
fruits = text.split()
print(fruits)

# Output:
# ['apple', 'banana', 'orange']

# E.g. 2
print("E.g.2 .split() function:")
text = "apple;banana;orange"
fruits = text.split(";")
print(fruits)

# Output
# ['apple', 'banana', 'orange']

# .join() function:

print("E.g.1 .join() function:")
text = ["apple", "banana", "orange"]
fruits = ' '.join(text)
print(text)

# Output
# ['apple', 'banana', 'orange']

print("E.g.2 .join() function:")
text = ["apple", "banana", "orange"]
fruits = '+'.join(text)
print(fruits)

# Output
# apple+banana+orange
