# def maximum(a,b):
#     if a > b :
#         return a
#     else :
#         return b
# x = input("num1 : ")
# y = input("num2 : ")
# print(maximum(x,y))

#USING LAMBDA FUNCTION

a = int(input("enter the number1: "))
b = int(input("enter the number2: "))
 
get_min = lambda x,y : x if x>y else y
print(get_min(a,b)) 



 