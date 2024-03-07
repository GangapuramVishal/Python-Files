''' Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

 Coding:
 if the word contains atleast 3 characters, remove the first letter and append it at the end
   now append three random characters at the starting and the end
 else:
   simply reverse the string

 Decoding:
 if the word contains less than 3 characters, reverse it
 else:
   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

 Your program should ask whether you want to code or decode'''

import random
import string

words = string.ascii_letters
# print(words)
# words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
temp1= random.sample(words,3)
temp2= random.sample(words,3)
# print(str(temp1))
# print(str(temp2))
rnd_word1 = ""
rnd_word2 = ""
for ele in temp1:
    rnd_word1 += ele
# print(rnd_word1)
for ele in temp2:
    rnd_word2 += ele
# print(rnd_word2)



option = int(input("enter the option 1. convert to code 2. decode "))
if option == 1:
  secret_message = input("enter the message to convert: ")
  words = secret_message.split(" ")
  code_word = ""
  for word in words:
    if len(word)>= 3:
      temp = " " + rnd_word1 + word[1:] + word[0] + rnd_word2 + " "
      code_word += temp
    else:
      code_word += " "+ word[::-1] + " "
  print(code_word)
else:
  encoded_message = input("enter the encoded meaage: ")
  words = encoded_message.split(" ")
  code_word = ""
  for word in words:
    if len(word)>= 3:
      temp = word[3:-3]
      temp = " " +  temp[-1] + temp[:-1] + " "
      code_word += temp
    else:
      code_word += " "+ word[::-1] + " "
  print(code_word)
