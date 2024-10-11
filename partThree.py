userinputforgrade = -1
try:

    userinputforgrade = int(input("Please enter a numerical value between 1 and 100 for a grade."))

    match userinputforgrade:
        case userinputforgrade if 90 <= userinputforgrade <= 100:
            print("The grade is A.")
        case userinputforgrade if userinputforgrade >= 80:
            print("The grade is B.")
        case userinputforgrade if userinputforgrade >= 70:
            print("The grade is C.")
        case userinputforgrade if userinputforgrade >= 60:
            print("The grade is D.")
        case userinputforgrade if 0 <= userinputforgrade < 60:
            print("The grade is F.")
        case _:
            print("The grade you have entered is invalid.")
except:
    print("You have not entered a numerical grade, please try again.")
    