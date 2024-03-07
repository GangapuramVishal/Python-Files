print('\n WELCOME TO THE "AVENGERS KBC"')
questions = [
    ["1.WHO KILLED THONAS FIRST?","Ironman","Thor","Flash","Superman","None",2],

    ["2.WHO WAS THE FIRST AVENGERS WHO TRAVEL THROW MULTIVERSE?","American jarvis","Wong","Docter strange","Wanda","None",3],

    ["3.WHO BUILD THE AVENGERS?","Batman","Tony stark","Captain america","Spiderman","None",2],

    ["4.WHO WAS THE FIRST AVENGER?","Spiderman","Captain america","Antman","Bucky","None",2],

    ["5.WHO WAS THE FIRST ONE TO WEAR IRONMAN GAUNTLET?","Ionman","Vision","Thor","Bruce Banner","None",4],

    ["6.WHO WAS THE BROTHER OF THOR?","Peter parker","Antman","Steven strange","Loki","none",4],

    ["7.WHO IS THE MOST POWERFUL AVENGER","Steve rogers","Thor","Hulk","Rocket","None",5],

    ["8.WHO WAS KILL IN AVENGERS ENDGAME FOR SOUL STONE?","Black widow","Clint","Nebula","Black Panther","None",1],

    ["9.WHO WAS THE GENIOUS ONE IN AVENGERS?","Bruce banner","Vision","Tony Stark","Wanda","None",3],

    ["10.WHO SAVE EVERYONE IN AVENGERS ENDGAME?","Captain america","Bruce banner","Captain marvel","Tony Stark","None",4],

]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0 
for i in range(0,len(questions)):
    question = questions[i]
    print(f'\n --> Question for Rs. {levels[i]} is ')
    print(f'\n {question[0]}\n')
    print(f'1.{question[1]}  2.{question[2]}')
    print(f'3.{question[3]}  4.{question[4]}')
    print(f'5.{question[5]}')

    reply = int(input("enter your oprtion from 1-5 or 0 to quit: "))

    if reply == question[6]:
        print(f'correct option, you have won Rs. {levels[i]}')
    elif reply== 0:
        money = levels[i-1]
        print(f'your take home money is {money}')
        break
    else:
        print("Wrong Answer!")
        print(f'your take home money is {money}\n')
        break
    if i == 3:
        money = 5000
    elif i == 7 :
        money = 80000
    elif i == 9:
        money = 320000
        print(f"WINNER WINNER CHICKEN DINNER,YOU WON YOUR FINAL AMOUNT IS : {1600002}")
    

