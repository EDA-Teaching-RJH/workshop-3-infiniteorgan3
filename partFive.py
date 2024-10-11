dayoftheweek = input("Enter a day of the week (in English): ").title()
daysoftheweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if (dayoftheweek not in daysoftheweek):
    print("You have not entered a day of the week.")
elif (dayoftheweek == "Saturday" or dayoftheweek == "Sunday"):
    print("It is the weekend.")
else:
    print("It is a weekday.")
