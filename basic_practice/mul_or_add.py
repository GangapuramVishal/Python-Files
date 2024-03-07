'''Calculate the multiplication and sum of two numbers

Given two integer numbers, return their product only if the product
is equal to or lower than 1000. Otherwise, return their sum.

'''
#Global Variables 
number1 = int(input("Enter the number1: "))
number2 = int(input("Enter the number2: "))
#function
def multiplication_or_addition():
    product = number1 * number2
    if product <= 1000:
        print("The product of two numbers is ", product)
    else:
        print("The addition of two numbers is ", number1+number2)
    
multiplication_or_addition()
