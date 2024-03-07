'''Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. 
If numbers are different then return False.

'''

N = int(input("Enter the total num of elements: "))
x = []
for i in range(N):
    y = input("enter the list elements: ")
    x.append(y)
print(x)
if (x[0] == x[-1]):
    print("True! first and last num are same")
else:
    print("False! first and last num aren't same")

