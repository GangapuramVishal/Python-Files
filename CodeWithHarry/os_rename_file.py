import os
files = os.listdir("file name")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"filepath",f"filepath/{i.png}")
        i +=1



'''import os

files = os.listdir("clutteredFolder")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
    i = i + 1'''
        