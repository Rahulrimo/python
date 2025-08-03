num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

operator = input("Enter an operator : ")
match operator:
    case"+":
       print("The sum is:", num1 + num2)
    case"-":
       print("The difference is:", num1 - num2)
    case"*":
       print("The product is:", num1 * num2)
    case"/":
       print("The quotient is:", num1 / num2)
    case _ :
       print("enter a valid operator")