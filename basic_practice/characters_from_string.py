'''Print characters from a string that are present at 
an even index number

Write a program to accept a string from the user and display characters
that are present at an even index number.

'''

# Word = input("Enter a Word: ")
# N = len(Word)
# for i in range(0, N-1, 2):
#     print(Word[i])
        

word = input("enter the word: ")
size = len(word)
x = list(word)
print(x)
for i in x[0::2]:
    print(i)