'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

def isValid(s):
    open_bracket = ['(','[','{']
    close_bracket= [')',']','}']
    d = dict(zip(close_bracket,open_bracket))
    if (s[0] in close_bracket or s[-1] in open_bracket):
        return False
    ind = 0
    result = []
    while(ind<len(s)):
        if(s[ind] in open_bracket):
            result.append(s[ind])
        else:
            need =d[s[ind]]
            if (len(result)>0 and result[-1]== need):
                result.pop()
            else:
                return False
        ind+=1
    if(len(result)==0):
        return True
    else :
        return False
isValid("()")
        