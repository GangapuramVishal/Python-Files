ui = input("Enter the value between 1-10:\n")

if (ui=="quit" or ui =="Quit"):

    print("You choose to quit the program...\nSo we can't proceed further...!!")

elif ((int(ui)<1) or (int(ui)>10)):

    raise ValueError("You need to enter valid value between 1-10!!")

else:

    print("We can proceed further..")

