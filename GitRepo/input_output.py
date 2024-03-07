# # Accept numbers from a user
# number = int(input('Enetr the number: '))
# print(number)

# Display three string “Name”, “Is”, “James” as “Name**Is**James”
# Hint: Use the sep parameter of the print() function to define the separator symbol between each word.
# print('my', 'name', 'is', 'Vishal', sep = "_")

# Convert Decimal number to octal using print() output formatting
# num = int(input("enter the number: "))
# print(f'octal num:' '%o' %num)

# Display float number with 2 decimal places using print()
# Use the %.2f formatting code in print() function to format float number to two decimal places.
# number = float(input("entee float number: "))
# print('%.2f' % number)

# Accept a list of 5 float numbers as an input from the user
num = []
for i in range(5):
    x = float(input("enter num: "))
    num.append(x)
print(num)
