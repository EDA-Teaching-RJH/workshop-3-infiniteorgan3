isstudent = ""
while (isstudent != "y" and isstudent != "n"):
    isstudent = input("Are you a student? y/n \n").strip().lower()

if (isstudent == "y"):
    isstudent = True
else:
    isstudent = False

try:
    personage = int(input("What is your age?"))
except:
    print("An error has occurred with the input given for your age.")
else:
    if (personage < 12 or personage >= 65):
        print("The price is £5.")
    elif (isstudent == True):
        print("The price is £8.")
    else:
        print("The price is £10.")