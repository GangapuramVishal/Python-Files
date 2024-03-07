'''Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each iteration,
 print the sum of the current and previous number.'''


print("Printing current and previous number and their sum in a range(N)")

N = int(input("Enter the range of a numbers: "))
previous_num = 0 

for i in range(N):
    sum = previous_num + i
    print("Current number: ", i,"previous number: ",previous_num, "Sum: ", sum)
    previous_num = i
    

