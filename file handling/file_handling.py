# f = open('about.txt', mode= 'r')
# print('file name is: ', f.name)
# print("encoding is: ", f.encoding)
# print('mode is: ', f.mode)
# print('is file closed: ', f.closed)
# f.close()
# print('is file closed: ', f.closed)
# import os 
# if os.path.isfile("abou.txt"):
#     f = open("about.txt")
#     print(f) 
# else:
#     print("FILE LOCATION NOT FOUND")

# f = open("about.txt",mode="r")
# data = f.read()
# print(data)
# f.close()

# ------bro code----------------
# import os
# path = "E:\\HtmlTools.txt"  
# if os.path.exists(path):
#     print("This location exists!")
#     if os.path.isfile(path):
#         print("This file Exists!")
#     else:
#         print("This location Exists, But File don't Exists")
# else:
#     print("This location does't Exists")

# try:

#     with open ("E:\\python programs\\file handling\\typing.txt") as file:
#         print(file.read())

# except FileNotFoundError :
#     print("That file was not found")

# with open("E:\\python programs\\file handling\\test.txt","a") as file:
#     print(file.write("\nHi this a new text!"))

# ---------Copy file-----------
# import shutil

# shutil.copyfile("E:\\python programs\\file handling\\about.txt", "copy.txt")
    
# ---------------- moving a file-----------------

# import os
# source = "E:\html\practice_sites\\test.txt"
# destination = "E:\\python programs\\file handling\\test.txt" 
# try :
#     if os.path.exists(destination):
#         print("file already exists")
#     else:
#         os.replace(source,destination)
#         print(source+ " was movied")
# except FileNotFoundError:
#     print(source + " was not found")

# ------------opening multiple files-----------------
file_names = ["file1.txt","test.txt","typing.txt"]
for files in file_names:
    try:
        with open(files, encoding="utf-8") as file:
            content = file.read()
            print(f'content of "{files}" : "{content}"')
    except FileNotFoundError:
        print(f'The file, {files} is not found')