def mergeTwoLists():
    N = int(input("enter the num of elements: "))
    list1 = []
    list2 = []
    for i in range(N):
        num1 = int(input("enter the elements: "))
        list1.append(num1)
    print("List1: ", list1)

    N2 = int(input("enter the num of elements: "))
    list2 = []
    for i in range(N2):
        num2 = int(input("enter the elements: "))
        list2.append(num2)
    print("List2: ", list2)

    M = list1 + list2
    print(M)
    M.sort()
    print(M)
        
mergeTwoLists()





