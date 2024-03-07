import time 
hr = int(time.strftime('%H'))
print(hr,"hr")
hr = int(input("Enter the hours: "))
min = time.strftime('%M')
print(min,"mins")
sec= time.strftime('%S')
print(sec,"sec")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if (hr >= 0 and hr <= 12) :
    print("Good Morning")
elif (12 <= hr <= 17):
    print("Good Afternoon")
elif (hr >= 17 and hr <= 20):
    print("Good evening")
else:
    print("Good Night")


