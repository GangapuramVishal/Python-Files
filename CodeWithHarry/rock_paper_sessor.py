import random
def check(comp, user):

    if (comp == user):
        return 0
    if (comp== 1 and user == 2 ):
        return 1
    if (comp == 2 and user == 3):
        return 1
    if (comp== 3 and user == 1):
        return 1
    return -1
    
comp = random.randint(1,3)
user = int(input(" 1. Rock \n 2. Paper \n 3. sessor \n Enter your choice:\n "))

choice ={1:"rock", 2:"paper", 3: "sessor"}
user_choice = choice[user]
comp_choice = choice[comp]
print("User choice: ", user_choice)
print("computer_choice: ", comp_choice)

score = check(comp, user)
if(score == 0):
    print("it's Draw")
elif(score == -1):
    print("You loose")
else:
    print("you Won") 