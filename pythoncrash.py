#our basic calculator
#our basic calculator
# additions, subtraction, multiplication, division, modulo

number_1 = int(input("Enter the first number"))
number_2 = int(input("Enter the second number"))
operation = input("What operation do you want to perform? +, -, /, %,* ,done") #this line would take the operator
addition = number_1 + number_2
subtraction = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2
modulo = number_1 % number_2

#IF STATEMENTS
#What operation do you want to perform
a = 0
while a<1:
    if operation == ("+"):
        print(number_1, "+", number_2, "=", addition)
    elif operation == ("-"):
        print(number_1, "-", number_2, "=", subtraction)
    elif operation == ("*"):
        print(number_1, "*", number_2, "=", multiplication)
    elif operation == ("%"):
        print(number_1, "%", number_2, "=", modulo)
    elif operation == ("/"):
        print(number_1, "/", number_2, "=", division)
    elif operation == ("done"):
        print("Goodbye")
        break
    else:
        print("operator invalid")
    break

