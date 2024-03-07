def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1/num2

while True:
    
    print("Select an Operation: \n")
    print("1. Addition \n" "2. subraction \n" "3. Multition \n" "4. Division \n" "5. To exit \n")

    Operation = int(input("Select from 1, 2, 3, 4, 5 : "))

    
    if (Operation == 1):
        number1 = float(input("Enter a number: "))
        number2 = float(input("Enter a number: "))
        print(f'{number1} + {number2} = ', add(number1, number2), "\n")

    elif (Operation == 2):
        number1 = float(input("Enter a number: "))
        number2 = float(input("Enter a number: "))
        print(f'{number1} - {number2} = ', sub(number1, number2), "\n")

    elif (Operation == 3):
        number1 = float(input("Enter a number: "))
        number2 = float(input("Enter a number: "))
        print(f'{number1} * {number2} = ', mul(number1, number2),"\n")

    elif (Operation == 4):
        number1 = float(input("Enter a number: "))
        number2 = float(input("Enter a number: "))
        print(f'{number1} / {number2} = ', div(number1, number2 ),"\n")

    elif (Operation == 5):
        print("Program Ended")
        quit()
