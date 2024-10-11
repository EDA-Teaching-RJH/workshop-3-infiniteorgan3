username = input("Please enter a username: ")
password = input("Please enter a password: ")

correctusername = "admin"
correctpassword = "password9"

if (username == correctusername and password == correctpassword):
    print("Access granted.")
else:
    print("Error, access denied.")
