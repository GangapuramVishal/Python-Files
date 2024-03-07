'''Write a function to find the longest common prefix string 
amongst an array of strings.
If there is no common prefix, return an empty string " " .'''

def longestCommonPrefix(strs):
    prefix = ''
    for i in strs:
        if len(i)<len(prefix) or prefix=='':
            prefix=i
    need = len(strs)
    count = 0
    result=''
    while(need!=count):
        count =0
        for i in strs:
            if(prefix == i[:len(prefix)]):
                count+=1
        result = prefix
        prefix = prefix[:-1]
    if(need == count):
        return result
    else:
        return ''
result = longestCommonPrefix(['flower','flow','flight'])
print(result)
