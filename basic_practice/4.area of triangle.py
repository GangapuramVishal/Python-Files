## AREA OF TRIANGLE
a = float(input('enter the num: '))
b = float(input('enter the num: '))
c = float(input('enter the num: '))
s = (a+b+c)/2
#area of triangle=(s*(s-a)*(s-b)*(s-c))**0.5
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f' the area of triangle is {area}')
