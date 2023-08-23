#check if your number is odd or even

number = int(input("Enter the number to determine if odd or even?"))

num1 = number / 2 == 1
num2 = number /2 == 0
if num1==1:
    print("This number is odd")
elif num2 == 0:
    print("This number is even")