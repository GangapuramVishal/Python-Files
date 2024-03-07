'''For a STRING'''
# METHOD-1
# word = input("enter the word: ")
# lst_wrd = list(word)
# rev_word= reversed(word)
# lst_rev_wrd = list(rev_word)
# print(lst_wrd)
# print(lst_rev_wrd)
# if lst_wrd == lst_rev_wrd:
#     print(word, "is a palindrome")
# else:
#     print(word, "is not a palindrome")

#METHOD-2
# word = input("enter the word: ")
# rev_word = word[::-1]
# print(rev_word)
# print(bool(word==rev_word))


# ''' for a numeric value'''

num = int(input("enter the num: "))
temp = num
rev = 0
while temp > 0:
    r = temp % 10
    rev = rev * 10 + r
    temp = temp//10
print("Reverse of a given number is",rev)
if rev == num:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")



