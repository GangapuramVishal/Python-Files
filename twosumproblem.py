'''The Two Sum problem asks us to find two numbers in an array that
 sum up to a given target value.
 We need to return the indices of these two numbers.'''

# Code to take input of a list
# from the user.

# Take input of the size of the list
N = int(input("enter the total number of elements in a list: "))
# Declare an empty list
list=[]
# Iterate for n times take inputs
for k in range(N):
    x = int(input("enter the elements of the list: "))  # Take input of kth element as x.
    list.append(x)  # Append 'x' to the list.
print("List: ",list)
target = int(input("enter the target sum: "))

for i in range(N-1):
    for j in range(i+1,N):
        if list[i] + list[j]== target:
            print(i,j)

