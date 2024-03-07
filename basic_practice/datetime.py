from datetime import datetime
import time
a = datetime.now()
current_date = a.date()
print("date: ", current_date)
current_time = a.time()
print("time: ", current_time)
print("year: ", a.year)
print("time: ", a.month)
print("time: ", a.day)

# x = datetime.now()
# print(x)

b = time.ctime(time.time())
print("time: ",b)