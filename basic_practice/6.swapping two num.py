#swap two variables
a = input('a=: ')
b = input('b=: ')
temp = a
a = b
b = temp
print(f'the value of a&b after swapping is a = {a} and b = {b}')

# SWAP TWO NUM USING +&-
a = int(input('a=: '))
b = int(input('b=: '))
a = a+b
b = a-b
a = a-b
print(f'the value of a&b after swapping is a = {a} and b = {b}')
