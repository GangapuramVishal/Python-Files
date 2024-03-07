# def feboo():
#     N = int(input('enter the range: '))
#     a = 0
#     b = 1
#     for i in range(N):
#         print(a, end=" ")
#         c=a                                 
#         a=b                          
#         b=c+b

# feboo()

fib_series = [0,1]
def fib(N):
    while len(fib_series) < N:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series

result = fib(10)
print(result)