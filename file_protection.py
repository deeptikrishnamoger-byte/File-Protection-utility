import os

password = "1234"

user_password = input("Enter password: ")

if user_password == password:
    print("Access granted")
    file = input("Enter file name to open: ")
    if os.path.exists(file):
        print("File found")
    else:
        print("File not found")
else:
    print("Wrong password")