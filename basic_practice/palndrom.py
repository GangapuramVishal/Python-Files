n = int(input("enter num : "))
temp = n
rev_num = 0
while n>0:
    r = n%10
    rev_num = rev_num*10 + r
    n = n//10
if rev_num == temp :
    print(f'{rev_num} is a palndrom num')
else :
    print(f'{rev_num} is not a palndrom num') 