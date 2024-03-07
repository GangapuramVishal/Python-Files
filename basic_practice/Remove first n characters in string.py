'''Remove first n characters from a string

Write a program to remove characters from a string starting from
 zero up to n and return a new string.'''

# N = int(input("Enter the num of strings to remove: "))
# word = input("Enter the word: ")
# new_word = ""
# if (N <= len(word)):
#     new_word = word[N:]
#     print(new_word)


def remove_chars(word,n):
    print('Original string is ', word)
    x = word[n:]
    return x

print("Removing characters from a string")

print(remove_chars("gangapuram",4))