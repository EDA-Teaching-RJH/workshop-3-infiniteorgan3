"""'''import re
quit = False
allowedoperators = ['+','-','*','/','%']
while quit == False:
    operation = input("Please enter a valid operation between two numbers.").strip().lower().replace(" ", "")
    operator = ""
    operand1 = ""
    operand2 = ""
    pattern = re.compile(r"\d+[\\+|-|\\*|/|%]\d+")

    if (bool(re.search(pattern,operation)) == True):
        for i in range(operation.len()):
            if (operation[i] in allowedoperators):
                operator = operation[i]
            elif (operator == ""):
                operand1 += operation[i]
            else:
                operand2 += operation[i]
    elif (operation == "quit"):
        quit = True
        break
    else:
        print("This operation is invalid.")

    match operator:
        case "/":
            if int(operand2) == 0:
                print("This operation is invalid.")
            else:
                print("The answer is: " + str(int(operand1) / int(operand2)) + ".")
        case "+":
            print("The answer is: " + str(int(operand1) + int(operand2)) + ".")
        case "-":
            print("The answer is: " + str(int(operand1) - int(operand2)) + ".")
        case "*":
            print("The answer is: " + str(int(operand1) * int(operand2)) + ".")
        case "%":
            print("The answer is: " + str(int(operand1) % int(operand2)) + ".")'''"""

quit = False
while quit == False:

    try:
        operand1 = int(input("Please enter the first number."))
        operand2 = int(input("Please enter the second number."))
    except:
          print("Those are invalid numbers, please try again.")
          continue2 = input("Would you like to continue? y/n ").strip().lower()
          if (continue2 == "y"):
            continue
          else:
                quit = True
                break
    operator = input("What is the operator you are using?")
    match operator:
        case "/":
            if int(operand2) == 0:
                print("This operation is invalid.")
            else:
                print("The answer is: " + str(operand1 / operand2) + ".")
        case "+":
                print("The answer is: " + str(operand1 + operand2) + ".")
        case "-":
                print("The answer is: " + str(operand1 - operand2) + ".")
        case "*":
                print("The answer is: " + str(operand1 * operand2) + ".")
        case "%":
                print("The answer is: " + str(operand1 % operand2) + ".")
        case "quit":
                quit = True
                break