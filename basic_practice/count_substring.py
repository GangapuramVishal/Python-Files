'''Return the count of a given substring from a string
   Write a program to find how many times substring “Emma” 
   appears in the given string.

str = input('Enter the string: ')
str_x = str.split(" ")
# print(str)
# print(str_x)
count = 0
sub_str = input("enter the sub string: ")

for i in str_x:
    # print(i)
    if sub_str == i:
        count += 1
print(f'{sub_str} appeared {count} times') '''

'''str_x = input('Enter the string: ')
cnt = str_x.count("vishal")
print(cnt)'''


string = input("enter main string : ")
sub_string = input("enter sub string: ")
count = 0 
for i in range(len(string)-len(sub_string) + 1):
    if (string[i:i+ len(sub_string)] == sub_string):
        count+=1
print(count)