student_name = input('enter student name :')
marks = {'vishal': 80 , 'honey' : 99 , 'bobby' : 87}
for i in marks:
    if i == student_name.lower():
        print(marks[i])
        break
else:
  print('no entry with this name')
