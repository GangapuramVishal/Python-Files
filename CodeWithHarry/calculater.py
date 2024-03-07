number1 = int(input("enter number:\n"))
operator = input("enter operater: ")
number2 = int(input("enter number: "))
#print(number1,operator,number2,-)
if operator == "+":
    print(number1,operator,number2,"=",number1+number2)

elif operator== "-":
    print(number1,operator,number2,"=",number1-number2)

elif operator== "*":
    print(number1,operator,number2,"=",number1*number2)

elif operator== "/":
    print(number1,operator,number2,"=",number1/number2)

elif operator== "%":
    print(number1,operator,number2,"=",number1%number2)
else:
    print('please enter valid num or operator')


