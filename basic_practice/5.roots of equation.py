#QUADRATIC EQUATION SOLVING
# the qua equation is
#ax2+bx+c=0
a = float(input('enter num: '))
b = float(input('enter num: '))
c = float(input('enter num: '))
d = (-b+(b**2-4*a*c)**0.5)/2*a
e = (-b-(b**2-4*a*c)**0.5)/2*a
x1 = d
x2 = e
print(f'the roots of the equations are {x1} and {x2}')
