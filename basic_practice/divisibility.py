'''Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers 
which are divisible by 5'''

try:
    my_list = []

    while True:
        my_list.append(int(input("Enter the list ")))
    
except:
    print("Given list is", my_list)

print("Divisible by 5")
for i in my_list:
    if i%5 == 0:
        print(i)
