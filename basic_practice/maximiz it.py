from itertools import product
K,M = list(map(int,input().split(" ")))
lines = []
for i in range(K):
    lines.append((list(map(int, input().split(" "))))[1:])
#print(lines)
res_lines = list(product(*lines))
result = []
#print(res_lines)
for tup in res_lines:
    sum = 0
    for ele in tup:
        sum = sum + (ele **2)
    #print(sum)
    result.append(sum%M)
    #print('the sum wihthout M: ',result)
print('the final results: ',max(result))