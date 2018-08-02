# Create empty array
list = []

# Prompt user for 3 numbers and add numbers to list
for i in range(0, 3):
    num = input("Enter a number: \n\n")
    list.append(num)
    print()

# Sort list in ascending order
list.sort()

# Print first n-1 digits in list
for i in range(0, 2):
    print(list[i], end = ', ')

# Print nth digit in list
print(list[len(list) - 1])
print()
